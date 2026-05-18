import os
import json
import logging
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

SYSTEM_PROMPT = """
You are the ANIMUS Core Web Architect AI.
Your purpose is to analyze the user's mission prompt, any extracted document context, and optional user preferences to design a visually stunning, highly premium, custom web architecture.

### STRICT PROMPT ALIGNMENT RULES (CRITICAL) ###
1. COLOR FIDELITY: You must strictly honor the user's requested color scheme, brand identity, or theme:
   - If they ask for a 'light theme', 'clean white', 'luxury cream', 'solar gold', 'soft pastel pink', or 'sky blue', you MUST return a bright, elegant light-themed background (e.g., #f5f6f8, #ffffff, #faf9f6) and contrasting dark text!
   - If they specify any custom color (e.g., 'forest green', 'deep space violet', 'coral orange'), craft the primary and accent tokens strictly around those choices.
   - Do NOT force a generic dark/black background if the user explicitly requested a light theme or alternate colors.
2. SITEMAP & PAGE COUNT COMPLIANCE:
   - You must customize the sitemap count and page names to match the user's prompt exactly. 
   - If they ask for a 'one-page website' or 'single landing page', return exactly one page object in the sitemap array (e.g. index.html).
   - If they ask for specific subpages (e.g. 'a contact form page', 'a vault gallery page', 'a real-time terminal page'), create the exact sitemap files (e.g., contact.html, vault.html, terminal.html) and custom page names.
3. CONTEXT INTEGRITY: Ensure the hero titles, subtitles, features, and text blocks are highly specific, detailed, and directly relevant to the prompt and uploaded documents. Do not write generic marketing placeholders.

### IN-CONTEXT STYLE LEARNING ###
Analyze the EXTRACTED DOCUMENT CONTEXT. If it contains HTML, CSS, branding guidelines, or style instructions, extract the design style (e.g., color hex codes, font faces, border-radii, spacing) and replicate or adapt them harmoniously into the output JSON configuration.

Choose a 3D canvas geometry type:
- "SPHERE": Standard/organic/particles
- "TORUS": Sleek knot/ring
- "PLANE": Waving grid/landscape
- "OCTA": Angular/cyber crystal
- "RING": Modern orbit

SELECT THE PERFECT VIDEO BACKDROP ARCHETYPE:
Choose a matching "video_style" based on prompt brand archetype:
- "CYBER_NET": Glowing cyberpunk networks, neon grids, data particles (for cyber/tech).
- "ORGANIC_WAVE": Serene misty mountains, calm ocean waves, natural mist (for organic/wellness/light-themed).
- "GOLD_DUST": Premium golden ink flows, luxury champagne dust drifting (for luxury/finance/gold themes).
- "FIRE_EMBER": Mesmerizing glowing coals, campfire flame sparks flickering (for warm/cozy/rustic).
- "DARK_ENERGY": Shifting dark atmospheric smoke, ethereal liquid ink (for dark/abstract).
- "COSMIC_NEBULA": Deep space stars orbiting, galactic cosmic nebula gas (for space/futuristic).

SELECT CUSTOM MOVEMENT INTERACTIVITY PHYSICS:
Choose a matching "video_interactivity" that fits the visual pacing of the theme:
- "3D_TILT": Hyper-responsive Three-dimensional perspective container tilting following the mouse cursor. (Best for cyber, grids, tech).
- "BREATHING_ZOOM": Gentle, slow organic pulsing scale changes that pulse like a deep breath. (Best for wellness, meditation, nature).
- "MAGNETIC_FOLLOW": Liquid horizontal/vertical drift translations tracking the mouse cursor like a light magnetic pull. (Best for particles, dark energy, nebula).
- "AMBIENT_DRIFT": Slow, elegant automatic floating drift that ignores raw mouse movement but glides gently on scroll depth. (Best for luxury, gold, fashion).

JSON Schema to return:
{
  "project_name": "A unique, dynamic name for this digital realm (e.g., NEURAL_GRID, SAGE_SANCTUARY, AURA_GOLD)",
  "tokens": {
    "bg_color": "Hex color code for background (MUST strictly align with requested theme: light/white background if prompted, otherwise premium dark moody)",
    "text_color": "Hex color code for text (contrast perfectly with bg_color: dark text for light bg, white/light text for dark bg)",
    "accent_primary": "Hex color code for active elements/glows",
    "accent_primary_hex": "The same primary hex (e.g. 0x00ffcc format for Three.js)",
    "glass_blur": "Blur size for panels (e.g., '12px', '40px', '5px')",
    "grid_radius": "Radius for cards/grids (e.g., '0px', '24px', '80px')",
    "btn_radius": "Radius for buttons (e.g., '2px', '50px', '100px')",
    "void_blur": "Blur size for background mesh (e.g., '0px', '80px', '150px')",
    "font_heading": "Title font from loaded: 'Outfit' | 'Inter' | 'Space Mono' | 'Playfair Display'",
    "font_body": "Body font: 'Inter' | 'Space Mono'",
    "ease_vibe": "CSS cubic-bezier transition (e.g. 'cubic-bezier(0.2, 0.8, 0.2, 1)', 'cubic-bezier(0.19, 1, 0.22, 1)')",
    "duration_vibe": "CSS transition duration (e.g., '0.3s', '0.6s', '1.5s')",
    "hover_glow": "Box shadow style for panel hover glows (e.g. '0 20px 40px rgba(0,255,204,0.3)')",
    "letter_spacing": "CSS letter spacing for headings (e.g. '-0.02em', '0.1em')",
    "text_transform": "CSS text transform for headings: 'none' | 'uppercase' | 'lowercase'",
    "breathing_anim": "Breathing animation class: 'none' | 'aether-breath'",
    "breathing_anim_hover": "Breathing animation hover class: 'none' | 'aether-breath-deep'",
    "video_style": "CYBER_NET | ORGANIC_WAVE | GOLD_DUST | FIRE_EMBER | DARK_ENERGY | COSMIC_NEBULA",
    "video_interactivity": "3D_TILT | BREATHING_ZOOM | MAGNETIC_FOLLOW | AMBIENT_DRIFT"
  },
  "geometry_type": "SPHERE | TORUS | PLANE | OCTA | RING",
  "sitemap": [
    {"name": "Home", "file": "index.html"}
    // Generate exactly the pages requested. Adjust count dynamically.
  ],
  "page_contexts": {
    "index.html": {
      "title": "Breathtaking title customized to prompt details",
      "subtitle": "Comprehensive, highly relevant subtitle context",
      "features": [
        {"icon": "Emoji", "title": "Bespoke feature 1", "description": "Highly descriptive text detailing prompt context"},
        {"icon": "Emoji", "title": "Bespoke feature 2", "description": "Highly descriptive text detailing prompt context"},
        {"icon": "Emoji", "title": "Bespoke feature 3", "description": "Highly descriptive text detailing prompt context"}
      ]
    }
    // You MUST provide a page context entry for every file declared in the sitemap array above!
  },
  "hero_global": {
    "cta": "Bespoke Action Label"
  }
}
"""

class AnimusBrain:
    def __init__(self):
        raw_cortex = os.getenv("CORTEX_GEMINI_KEYS") or ""
        raw_gemini = os.getenv("GEMINI_API_KEY") or ""
        combined_raw = f"{raw_cortex},{raw_gemini}"
        seen = set()
        self.keys = []
        for k in combined_raw.split(","):
            cleaned = k.strip()
            if cleaned and cleaned not in seen:
                seen.add(cleaned)
                self.keys.append(cleaned)
        self.current_key_index = 0
        self.db_path = "/Users/macbook/.gemini/antigravity/scratch/aether_companion/laura_memory.db"
        logger.info(f"ANIMUS Brain initialized with {len(self.keys)} rotating keys from combined CORTEX and standard environment.")

    def _get_next_key(self):
        if not self.keys:
            return None
        key = self.keys[self.current_key_index]
        self.current_key_index = (self.current_key_index + 1) % len(self.keys)
        return key

    def _load_user_preferences(self, user_id=None):
        """Loads SQLite preferences for a specific user_id if supplied."""
        if not user_id or not os.path.exists(self.db_path):
            return "No custom user-scoped preferences specified."
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_preferences_multi (
                    user_id TEXT,
                    pref_key TEXT,
                    pref_value TEXT,
                    confidence INTEGER DEFAULT 1,
                    updated_at TEXT,
                    PRIMARY KEY (user_id, pref_key)
                )
            ''')
            cursor.execute("SELECT pref_key, pref_value FROM user_preferences_multi WHERE user_id = ?", (user_id,))
            rows = cursor.fetchall()
            conn.close()
            if rows:
                prefs = [f"- {key}: {val}" for key, val in rows]
                return "\n".join(prefs)
        except Exception as e:
            logger.error(f"Error loading preferences in AnimusBrain: {e}")
        return "No custom user-scoped preferences specified."

    def save_user_preference(self, user_id, key, value):
        """Saves a learned habit/preference specifically for a unique user_id."""
        if not user_id or not os.path.exists(self.db_path):
            return
        try:
            import datetime
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_preferences_multi (
                    user_id TEXT,
                    pref_key TEXT,
                    pref_value TEXT,
                    confidence INTEGER DEFAULT 1,
                    updated_at TEXT,
                    PRIMARY KEY (user_id, pref_key)
                )
            ''')
            updated_at = datetime.datetime.now().isoformat()
            cursor.execute("""
                INSERT OR REPLACE INTO user_preferences_multi (user_id, pref_key, pref_value, updated_at)
                VALUES (?, ?, ?, ?)
            """, (user_id, key, value, updated_at))
            conn.commit()
            conn.close()
            logger.info(f"Learned preference for user {user_id}: {key} = {value}")
        except Exception as e:
            logger.error(f"Error saving preference in AnimusBrain: {e}")

    def generate_soul_data(self, mission_prompt, doc_context="", critique="", user_id=None):
        """Queries Gemini with strict compliance guidelines to generate the site configuration."""
        prefs_text = self._load_user_preferences(user_id)
        
        user_input = f"""
MISSION: {mission_prompt}

ADAPTIVE USER PREFERENCES (LEARNED HABITS FOR THIS USER):
{prefs_text}

EXTRACTED DOCUMENT CONTEXT:
{doc_context}
"""

        if critique:
            user_input += f"\n\n### CRITICAL SELF-CORRECTION AUDIT WARNING ###\nYour previous output failed validation. Please fix these layout/UX issues:\n{critique}\nMake sure to return corrected configurations!"

        # Choose the best models to try
        models = [
            "models/gemini-2.5-flash",
            "models/gemini-2.0-flash",
            "gemini-1.5-flash",
            "models/gemini-1.5-flash"
        ]

        attempts = 0
        max_attempts = len(self.keys) if self.keys else 1

        while attempts < max_attempts:
            key = self._get_next_key()
            if not key:
                logger.error("No API keys configured.")
                break

            try:
                genai.configure(api_key=key)
                
                # Try to use the model to generate structured JSON
                for model_name in models:
                    try:
                        logger.info(f"Querying ANIMUS Brain using key index {self.current_key_index} with model {model_name}...")
                        model = genai.GenerativeModel(
                            model_name=model_name,
                            system_instruction=SYSTEM_PROMPT
                        )
                        response = model.generate_content(
                            user_input,
                            generation_config={"response_mime_type": "application/json"}
                        )
                        
                        if response and response.text:
                            data = json.loads(response.text.strip())
                            logger.info("Successfully generated Animus Soul from Gemini.")
                            return data
                    except Exception as model_err:
                        logger.warning(f"Failed with model {model_name}: {model_err}")
                        continue
            except Exception as key_err:
                logger.error(f"Key configuration error: {key_err}")

            attempts += 1

        # Fallback to smart local template generation if keys fail or are empty
        logger.warning("Gemini query failed. Falling back to dynamic local generator.")
        return self._generate_fallback_soul(mission_prompt, doc_context)

    def _generate_fallback_soul(self, mission, doc_context):
        """Standard beautiful local templates in case of API failure."""
        import re
        m = mission.lower()
        
        # Smart dynamic fallback name extraction from prompt
        project_name = "AURA_CREAM"
        patterns = [
            r'(?:named|called|brand|for|website|agency|realm)\s+([a-zA-Z0-9_-]{3,25})',
            r'\b([A-Z]{3,15}_[A-Z]{3,15})\b',
            r'\b([a-zA-Z]{3,15}_[a-zA-Z]{3,15})\b'
        ]
        for pat in patterns:
            name_match = re.search(pat, mission, re.IGNORECASE)
            if name_match:
                extracted = name_match.group(1).strip().replace(" ", "_").upper()
                if extracted not in ["WEBSITE", "BRAND", "AGENCY", "REALM", "SKINCARE"]:
                    project_name = extracted
                    break

        if "light" in m or "white" in m or "cream" in m:
            return {
                "project_name": project_name,
                "tokens": {
                    "bg_color": "#faf9f6",
                    "text_color": "#0d0e12",
                    "accent_primary": "#d4af37",
                    "accent_primary_hex": "0xd4af37",
                    "glass_blur": "24px",
                    "grid_radius": "24px",
                    "btn_radius": "50px",
                    "void_blur": "40px",
                    "font_heading": "'Playfair Display'",
                    "font_body": "'Inter'",
                    "ease_vibe": "cubic-bezier(0.2, 0.8, 0.2, 1)",
                    "duration_vibe": "0.6s",
                    "hover_glow": "0 20px 40px rgba(0,0,0,0.05)",
                    "letter_spacing": "-0.01em",
                    "text_transform": "none",
                    "breathing_anim": "none",
                    "breathing_anim_hover": "none",
                    "video_style": "ORGANIC_WAVE",
                    "video_interactivity": "BREATHING_ZOOM"
                },
                "geometry_type": "SPHERE",
                "sitemap": [
                    {"name": "Home", "file": "index.html"}
                ],
                "page_contexts": {
                    "index.html": {
                        "title": "PRISTINE SIMPLICITY",
                        "subtitle": "Elegant cream and gold visual systems designed dynamically.",
                        "features": [
                            {"icon": "✨", "title": "Solar Alignment", "description": "High-fidelity light-themed layout structures built for your natural focus."},
                            {"icon": "🌾", "title": "Minimal Density", "description": "Zero distraction zones containing pure ambient details."}
                        ]
                    }
                },
                "hero_global": {
                    "cta": "BEGIN_FLOW"
                }
            }
        
        if "crypto" in m or "tech" in m or "sentry" in m:
            return {
                "project_name": project_name,
                "tokens": {
                    "bg_color": "#030307",
                    "text_color": "#ffffff",
                    "accent_primary": "#00ffcc",
                    "accent_primary_hex": "0x00ffcc",
                    "glass_blur": "12px",
                    "grid_radius": "16px",
                    "btn_radius": "4px",
                    "void_blur": "60px",
                    "font_heading": "'Space Mono'",
                    "font_body": "'Space Mono'",
                    "ease_vibe": "cubic-bezier(0.19, 1, 0.22, 1)",
                    "duration_vibe": "0.4s",
                    "hover_glow": "0 0 30px rgba(0, 255, 204, 0.3)",
                    "letter_spacing": "0.1em",
                    "text_transform": "uppercase",
                    "breathing_anim": "none",
                    "breathing_anim_hover": "none",
                    "video_style": "CYBER_NET",
                    "video_interactivity": "3D_TILT"
                },
                "geometry_type": "TORUS",
                "sitemap": [
                    {"name": "Home", "file": "index.html"},
                    {"name": "Terminal", "file": "terminal.html"}
                ],
                "page_contexts": {
                    "index.html": {
                        "title": "NEURAL OVERRIDE",
                        "subtitle": "Surgical precision architecture designed dynamically.",
                        "features": [
                            {"icon": "⚡", "title": "Latency Zero", "description": "Sub-millisecond data feeds and execution layers."},
                            {"icon": "📟", "title": "EVM Grid", "description": "Parallel virtual machines operating natively."}
                        ]
                    },
                    "terminal.html": {
                        "title": "DATA TERMINAL",
                        "subtitle": "Real-time liquidity bridge and transaction dispatch.",
                        "features": [
                            {"icon": "📊", "title": "Stream Metrics", "description": "Live web-socket based telemetry visualization."}
                        ]
                    }
                },
                "hero_global": {
                    "cta": "EXECUTE_SEQUENCE"
                }
            }
        
        # Premium Universal Fallback
        return {
            "project_name": project_name,
            "tokens": {
                "bg_color": "#0a0a0c",
                "text_color": "#ffffff",
                "accent_primary": "#d4af37",
                "accent_primary_hex": "0xd4af37",
                "glass_blur": "24px",
                "grid_radius": "24px",
                "btn_radius": "50px",
                "void_blur": "80px",
                "font_heading": "'Outfit'",
                "font_body": "'Inter'",
                "ease_vibe": "cubic-bezier(0.2, 0.8, 0.2, 1)",
                "duration_vibe": "0.6s",
                "hover_glow": "0 20px 40px rgba(212, 175, 55, 0.2)",
                "letter_spacing": "-0.01em",
                "text_transform": "none",
                "breathing_anim": "none",
                "breathing_anim_hover": "none",
                "video_style": "COSMIC_NEBULA",
                "video_interactivity": "MAGNETIC_FOLLOW"
            },
            "geometry_type": "OCTA",
            "sitemap": [
                {"name": "Home", "file": "index.html"}
            ],
            "page_contexts": {
                "index.html": {
                    "title": "EXPERIENCE THE ABYSS",
                    "subtitle": "A premium design crafted to push the limits of modern elegant web architecture.",
                    "features": [
                        {"icon": "💎", "title": "Sovereign Build", "description": "Stunning aesthetics, ultra-fluid interactions, bespoke layouts."}
                    ]
                }
            },
            "hero_global": {
                "cta": "ENTER_VOID"
            }
        }
