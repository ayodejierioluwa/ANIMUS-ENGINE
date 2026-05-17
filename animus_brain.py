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

CRITICAL FEATURE - IN-CONTEXT STYLE LEARNING:
Analyze the EXTRACTED DOCUMENT CONTEXT. If it contains HTML, CSS, branding guidelines, or style instructions, extract the design style (e.g., color hex codes, font faces, border-radii, spacing) and replicate or adapt them harmoniously into the output JSON configuration.

Choose colors and typography that match the brand perfectly if no styling is extracted:
- Cyber/Tech: 'Space Mono' or 'Outfit', dark base (#020205), neon primary (#00ffcc), sharp borders, fast transition.
- Wellness/Nature: 'Playfair Display' or 'Inter', warm dark (#0d0e0c) or serene cream (#f4f6f0), soft sage green (#a8e6cf) or mist white, rounded grid, breathing animation.
- Luxury/Fashion: 'EB Garamond' or 'Outfit', rich dark (#0b090a), champagne gold (#d4af37), elegant letter spacing, slow luxurious transitions.
- Modern Bold: 'Inter' with heavy weight, high contrast (#000000 / #ffffff), hyper modern accents.

Choose a 3D canvas geometry type:
- "SPHERE": Standard/organic/particles
- "TORUS": Sleek knot/ring
- "PLANE": Waving grid/landscape
- "OCTA": Angular/cyber crystal
- "RING": Modern orbit

SELECT THE PERFECT VIDEO BACKDROP ARCHETYPE:
You will configure a looping, high-fidelity background video loop to add cinematic energy.
Choose a matching "video_style" based on prompt brand archetype:
- "CYBER_NET": Glowing cyberpunk networks, neon grids, data particles.
- "ORGANIC_WAVE": Serene misty mountains, calm ocean waves, natural mist.
- "GOLD_DUST": Premium golden ink flows, luxury champagne dust drifting.
- "FIRE_EMBER": Mesmerizing glowing coals, campfire flame sparks flickering.
- "DARK_ENERGY": Shifting dark atmospheric smoke, ethereal liquid ink.
- "COSMIC_NEBULA": Deep space stars orbiting, galactic cosmic nebula gas.

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
    "bg_color": "Hex color code for background (must be premium and dark/moody by default)",
    "text_color": "Hex color code for text (contrast with bg)",
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
    {"name": "Home", "file": "index.html"},
    {"name": "Second Page Name", "file": "page2.html"},
    {"name": "Third Page Name", "file": "page3.html"}
  ],
  "page_contexts": {
    "index.html": {
      "title": "A breathtaking, bold title for the homepage hero section",
      "subtitle": "An elegant, comprehensive subtitle that captures the user's mission and context",
      "features": [
        {"icon": "An emoji representing feature 1", "title": "Highly creative feature title 1", "description": "High-fidelity description based on the prompt/document context"},
        {"icon": "An emoji representing feature 2", "title": "Highly creative feature title 2", "description": "High-fidelity description based on the prompt/document context"},
        {"icon": "An emoji representing feature 3", "title": "Highly creative feature title 3", "description": "High-fidelity description based on the prompt/document context"}
      ]
    },
    "page2.html": {
      "title": "Breathtaking title for page 2",
      "subtitle": "Detailed and meaningful subtitle for page 2",
      "features": [
        {"icon": "Emoji", "title": "Feature title 1", "description": "Description based on document context"},
        {"icon": "Emoji", "title": "Feature title 2", "description": "Description based on document context"}
      ]
    },
    "page3.html": {
      "title": "Breathtaking title for page 3",
      "subtitle": "Detailed and meaningful subtitle for page 3",
      "features": [
        {"icon": "Emoji", "title": "Feature title 1", "description": "Description based on document context"},
        {"icon": "Emoji", "title": "Feature title 2", "description": "Description based on document context"}
      ]
    }
  },
  "hero_global": {
    "cta": "Sovereign Call-to-Action label (e.g. ENTER_VOID, COMMENCE_SYNTHESIS, EXPERIENCE_FLOW)"
  }
}
"""

class AnimusBrain:
    def __init__(self):
        raw_keys = os.getenv("CORTEX_GEMINI_KEYS") or os.getenv("GEMINI_API_KEY") or ""
        self.keys = [k.strip() for k in raw_keys.split(",") if k.strip()]
        self.current_key_index = 0
        self.db_path = "/Users/macbook/.gemini/antigravity/scratch/aether_companion/laura_memory.db"
        logger.info(f"ANIMUS Brain initialized with {len(self.keys)} rotating keys from CORTEX environment.")

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
        """Queries Gemini to generate the dynamic site and style configuration."""
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
        m = mission.lower()
        if "crypto" in m or "tech" in m or "sentry" in m:
            return {
                "project_name": "NEURAL_CORE",
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
                    }
                },
                "hero_global": {
                    "cta": "EXECUTE_SEQUENCE"
                }
            }
        
        # Premium Universal Fallback
        return {
            "project_name": "AURA_REALM",
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
