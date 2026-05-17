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
2. Color Contrast: Are background and text colors highly legible and accessible?
3. Template Compile State: Are there any unreplaced double-bracket tokens (e.g., [[bg_color]] or [[title]]) left in the source code?
4. Aesthetic Elegance: Does the overall layout feel like a premium, wow-factor landing page or portfolio?

You must respond with a JSON object following this exact schema:
{
  "score": 95, // An integer between 0 and 100
  "passed": true, // Boolean (true if score >= 85 and no critical issues exist, otherwise false)
  "critiques": [
    "Detail any visual alignment issues,Low contrast warnings, or unreplaced tokens. If perfect, leave empty."
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

        # 2. Content Redundancy Audit
        file_paths = list(contents.keys())
        for i in range(len(file_paths)):
            for j in range(i + 1, len(file_paths)):
                if contents[file_paths[i]] == contents[file_paths[j]] and len(contents[file_paths[i]]) > 0:
                    self.issues.append(f"CRITICAL REDUNDANCY: Pages {file_paths[i]} and {file_paths[j]} contain identical features.")

        # 3. LLM Cognitive Visual Audit
        if generated_files and self.keys:
            self.issues.extend(self.audit_project_cognitively(generated_files))

        return len(self.issues) == 0

    def audit_file_heuristics(self, file_path, html):
        """Standard strict regex validation rules."""
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

    def audit_project_cognitively(self, generated_files):
        """Utilizes Gemini to inspect the compiled HTML and critique design flaws."""
        critique_errors = []
        key = self._get_next_key()
        if not key:
            return []

        # Audit only the index page (representative of the styling theme) to save tokens & latency
        index_file = [f for f in generated_files if "index.html" in f]
        if not index_file:
            index_file = [generated_files[0]]
            
        try:
            with open(index_file[0], "r", errors="ignore") as f:
                html_sample = f.read()

            logger.info("Initializing Cognitive Design Audit via Gemini...")
            genai.configure(api_key=key)
            model = genai.GenerativeModel(
                model_name="models/gemini-2.5-flash",
                system_instruction=SYSTEM_AUDIT_PROMPT
            )
            
            response = model.generate_content(
                f"Please perform a design and UX audit on this compiled page HTML/CSS:\n\n{html_sample[:4000]}",
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
                        
        except Exception as e:
            logger.warning(f"Cognitive Audit failed: {e}. Skipping LLM critique.")
            
        return critique_errors

    def report_issues(self):
        for issue in self.issues:
            print(f"🚨 SENTRY ALERT: {issue}")
