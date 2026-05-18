import os
import re
import json
import logging
import google.generativeai as genai
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

SYSTEM_AUDIT_PROMPT = """
You are the ANIMUS Quality Sentry AI.
Your task is to inspect the generated HTML pages and evaluate their design quality, visual harmony, typography, and UX flow.
Evaluate strictly on the following metrics:
1. Visual Overlaps & Layering: Are there any overlapping elements, or is the WebGL shader hidden under an opaque layer?
2. Color Contrast: Are background and text colors highly legible and accessible? Light backgrounds must have dark text; dark backgrounds must have light text.
3. Template Compile State: Are there any unreplaced double-bracket tokens (e.g., [[bg_color]] or [[title]]) left in the source code?
4. Aesthetic Elegance & Video backdrop: Does the overall layout feel like a premium, wow-factor landing page with an active video element and stunning dynamic flow?

You must respond with a JSON object following this exact schema:
{
  "score": 95, // An integer between 0 and 100
  "passed": true, // Boolean (true if score >= 85 and no critical issues exist, otherwise false)
  "critiques": [
    "Detail any visual alignment issues, low contrast warnings, or unreplaced tokens. If perfect, leave empty."
  ]
}
"""

class AnimusSentry:
    """
    The 'Cognitive Quality Auditor' of the Animus Engine.
    Combines rule-based syntax tests with an LLM-driven visual/UX layout critique loop.
    """
    def __init__(self):
        self.issues = []
        raw_keys = os.getenv("CORTEX_GEMINI_KEYS") or os.getenv("GEMINI_API_KEY") or ""
        self.keys = [k.strip() for k in raw_keys.split(",") if k.strip()]
        self.current_key_index = 0

    def _get_next_key(self):
        if not self.keys:
            return None
        key = self.keys[self.current_key_index]
        self.current_key_index = (self.current_key_index + 1) % len(self.keys)
        return key

    def audit_project(self, generated_files):
        """
        Performs a full project audit:
        1. Local syntactic heuristics (nav active, z-indexes).
        2. Content redundancy check.
        3. LLM Cognitive Visual Design Audit.
        """
        self.issues = []
        contents = {}
        
        # 1. Syntactic audits
        for file_path in generated_files:
            try:
                with open(file_path, "r", errors="ignore") as f:
                    html = f.read()
                features = re.findall(r'<h3.*?>(.*?)</h3>', html)
                contents[file_path] = features
                self.audit_file_heuristics(file_path, html)
            except Exception as e:
                self.issues.append(f"Failed to read file for heuristic audit: {e}")

        # 2. Content Redundant Audit
        file_paths = list(contents.keys())
        for i in range(len(file_paths)):
            for j in range(i + 1, len(file_paths)):
                if contents[file_paths[i]] == contents[file_paths[j]] and len(contents[file_paths[i]]) > 0:
                    self.issues.append(f"CRITICAL REDUNDANCY: Pages {file_paths[i]} and {file_paths[j]} contain identical features.")

        # 3. LLM Cognitive Visual Audit (utilizing full rotating keys resilient loop)
        if generated_files:
            self.issues.extend(self.audit_project_cognitively(generated_files))

        return len(self.issues) == 0

    def _calculate_hex_luminance(self, hex_color):
        hex_color = hex_color.strip("#")
        try:
            if len(hex_color) == 3:
                hex_color = "".join([c*2 for c in hex_color])
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            return (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
        except Exception:
            return 0.0

    def audit_file_heuristics(self, file_path, html):
        """Standard strict regex validation rules with contrast and video backdrop validation."""
        # Unreplaced tokens check
        unreplaced = re.findall(r'\[\[[a-zA-Z0-9_]+\]\]', html)
        if unreplaced:
            self.issues.append(f"Syntax Error in {file_path}: Unreplaced styling tokens found: {unreplaced}")

        # Visual Overlap Audit
        if 'z-index: -100' in html and 'background: transparent' not in html and 'background: rgba' not in html:
            self.issues.append(f"Visual Error in {file_path}: Opaque background blocks the WebGL shader layer.")

        # Nav Active State Audit
        if 'class="nav-item active"' not in html and 'class="nav-item  active"' not in html:
            self.issues.append(f"UX Error in {file_path}: Navigation bar has no active page indicator.")

        # Color Contrast Heuristic Check
        bg_match = re.search(r'--bg-color:\s*(#[0-9a-fA-F]{3,6})', html)
        text_match = re.search(r'--text-color:\s*(#[0-9a-fA-F]{3,6})', html)
        if bg_match and text_match:
            bg_lum = self._calculate_hex_luminance(bg_match.group(1))
            text_lum = self._calculate_hex_luminance(text_match.group(1))
            contrast_diff = abs(bg_lum - text_lum)
            if contrast_diff < 0.4:
                self.issues.append(f"CONTRAST CLASH in {file_path}: Background ({bg_match.group(1)}) and Text ({text_match.group(1)}) colors are too similar (luminance diff: {contrast_diff:.2f}).")

        # Video Backdrop Integrity Check
        if '<video' in html:
            src_match = re.search(r'<source\s+src="([^"]*)"', html)
            if not src_match or not (src_match.group(1).startswith("http") or src_match.group(1).startswith("/static/") or src_match.group(1).startswith("./") or src_match.group(1).startswith("../")):
                self.issues.append(f"VIDEO FAULT in {file_path}: Video element lacks a valid public streaming or local video source URL.")

    def audit_project_cognitively(self, generated_files):
        """Utilizes Gemini to inspect compiled HTML, rotating resiliently through all API keys on failures."""
        critique_errors = []
        if not self.keys:
            logger.warning("No API keys found in cortex environment. Skipping cognitive visual audit.")
            return []

        # Audit only the index page to preserve rate-limits & performance
        index_file = [f for f in generated_files if "index.html" in f]
        if not index_file:
            index_file = [generated_files[0]]
            
        try:
            with open(index_file[0], "r", errors="ignore") as f:
                html_sample = f.read()
        except Exception as e:
            logger.error(f"Failed to read index file for cognitive audit: {e}")
            return []

        attempts = 0
        max_attempts = len(self.keys)

        while attempts < max_attempts:
            key = self._get_next_key()
            if not key:
                break
            
            try:
                logger.info(f"Initializing Cognitive Design Audit via Gemini (Attempt {attempts + 1}/{max_attempts})...")
                genai.configure(api_key=key)
                
                # Check rotating model options
                models = ["models/gemini-2.5-flash", "models/gemini-2.0-flash", "models/gemini-1.5-flash"]
                for model_name in models:
                    try:
                        model = genai.GenerativeModel(
                            model_name=model_name,
                            system_instruction=SYSTEM_AUDIT_PROMPT
                        )
                        response = model.generate_content(
                            f"Please perform a design and UX audit on this compiled page HTML/CSS:\n\n{html_sample}",
                            generation_config={"response_mime_type": "application/json"}
                        )
                        
                        if response and response.text:
                            audit_result = json.loads(response.text.strip())
                            score = audit_result.get("score", 100)
                            passed = audit_result.get("passed", True)
                            critiques = audit_result.get("critiques", [])
                            
                            logger.info(f"Cognitive Design Audit complete. Score: {score}/100 | Passed: {passed}")
                            if not passed or score < 85:
                                for critique in critiques:
                                    critique_errors.append(f"COGNITIVE CRITIQUE (Score {score}): {critique}")
                            return critique_errors
                    except Exception as model_err:
                        logger.warning(f"Model {model_name} failed: {model_err}")
                        continue
            except Exception as key_err:
                logger.warning(f"Key index {self.current_key_index} encountered error: {key_err}")
            
            attempts += 1

        logger.warning("All Gemini key attempts failed or were rate-limited. Falling back strictly to local heuristic audits.")
        return critique_errors

    def report_issues(self):
        for issue in self.issues:
            print(f"🚨 SENTRY ALERT: {issue}")
