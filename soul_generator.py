import os
import json
import logging
from animus_brain import AnimusBrain

logger = logging.getLogger(__name__)

class AnimusSoul:
    """
    The 'Soul' of the Animus Engine.
    Powered by the new ANIMUS Brain running on CORTEX intelligence with cognitive critique capabilities and multi-user tracking.
    """
    def __init__(self, mission_prompt, critique=None, user_id=None):
        self.mission = mission_prompt
        self.critique = critique
        self.user_id = user_id
        self.brain = AnimusBrain()
        self.soul_data = self._ignite_consciousness()

    def _ignite_consciousness(self):
        logger.info(f"Igniting consciousness for mission: {self.mission[:100]}...")
        if self.critique:
            logger.info(f"Applying self-correction critique feedback: {self.critique[:150]}")
        if self.user_id:
            logger.info(f"Loading isolated styling memories for user: {self.user_id}")
        
        # We query the AnimusBrain to generate a bespoke web design configuration
        brain_data = self.brain.generate_soul_data(self.mission, critique=self.critique, user_id=self.user_id)
        
        # Extract details with resilient defaults matching the old keys
        project_name = brain_data.get("project_name", "AETHER_PROJ")
        tokens = brain_data.get("tokens", {})
        sitemap = brain_data.get("sitemap", [{"name": "Home", "file": "index.html"}])
        page_contexts = brain_data.get("page_contexts", {})
        hero_global = brain_data.get("hero_global", {"cta": "EXPLORE"})
        geometry_type = brain_data.get("geometry_type", "SPHERE")

        # Atmospheric DNA overrides to guarantee stunning visual consistency if any key is missing
        required_tokens = {
            "bg_color": "#0a0a0c",
            "text_color": "#ffffff",
            "accent_primary": "#00ffcc",
            "accent_primary_hex": "0x00ffcc",
            "glass_blur": "15px",
            "grid_radius": "24px",
            "btn_radius": "50px",
            "void_blur": "80px",
            "font_heading": "'Outfit'",
            "font_body": "'Inter'",
            "ease_vibe": "cubic-bezier(0.2, 0.8, 0.2, 1)",
            "duration_vibe": "0.6s",
            "hover_glow": "0 20px 40px rgba(0, 255, 204, 0.2)",
            "letter_spacing": "-0.01em",
            "text_transform": "none",
            "breathing_anim": "none",
            "breathing_anim_hover": "none",
            "video_style": "COSMIC_NEBULA",
            "video_interactivity": "3D_TILT"
        }
        for k, v in required_tokens.items():
            if k not in tokens:
                tokens[k] = v

        # Dynamic high-fidelity video loop streams matching the AI-prompted video_style archetype
        video_libraries = {
            "CYBER_NET": "https://player.vimeo.com/external/371433846.sd.mp4?s=236da2f3c022718b5deab7da7c9ec437c3558197&profile_id=139&oauth2_token_id=57447761",
            "ORGANIC_WAVE": "https://player.vimeo.com/external/434045526.sd.mp4?s=c27d2ad6cfed9d511cc0a8a6cb9373ed7d73010b&profile_id=165&oauth2_token_id=57447761",
            "GOLD_DUST": "https://player.vimeo.com/external/459389137.sd.mp4?s=87ae39bbdc97034bf08044709d2112444f6f8f74&profile_id=165&oauth2_token_id=57447761",
            "FIRE_EMBER": "https://player.vimeo.com/external/517602120.sd.mp4?s=d760db56610b64d1f2e4685ff86eb8c74378f4b0&profile_id=165&oauth2_token_id=57447761",
            "DARK_ENERGY": "https://player.vimeo.com/external/540058564.sd.mp4?s=f52bc194689626e25287f3ee1ca360f06a1bd226&profile_id=165&oauth2_token_id=57447761",
            "COSMIC_NEBULA": "https://player.vimeo.com/external/538571861.sd.mp4?s=404229eb4945417066922ff11bfcfc92f59f6356&profile_id=165&oauth2_token_id=57447761"
        }
        
        style_key = tokens.get("video_style", "COSMIC_NEBULA").upper()
        tokens["video_url"] = video_libraries.get(style_key, video_libraries["COSMIC_NEBULA"])

        # Determine relative luminance of the chosen background to establish high-contrast glass panels
        bg_hex = tokens.get("bg_color", "#0a0a0c").lower().strip("#")
        try:
            if len(bg_hex) == 3:
                bg_hex = "".join([c*2 for c in bg_hex])
            r, g, b = int(bg_hex[0:2], 16), int(bg_hex[2:4], 16), int(bg_hex[4:6], 16)
            luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
        except Exception:
            luminance = 0.0 # Default dark

        if luminance > 0.6:
            # Bright/Light Theme: Apply dark text, dark glass outlines, and thin dynamic vignette
            logger.info("AETHER_LUMINANCE: Light theme detected. Adjusting glass overlay contrast limits.")
            tokens["glass_bg_token"] = "rgba(0, 0, 0, 0.03)"
            tokens["glass_border_token"] = "rgba(0, 0, 0, 0.07)"
            tokens["vignette_token"] = "radial-gradient(circle, transparent 40%, rgba(0,0,0,0.03) 100%)"
            # Auto-align contrasting text color if the brain didn't generate one
            if tokens.get("text_color") == "#ffffff":
                tokens["text_color"] = "#0d0e12"
        else:
            # Classic Dark Theme: Apply light frosted glass overlays and thick dark vignette
            tokens["glass_bg_token"] = "rgba(255, 255, 255, 0.03)"
            tokens["glass_border_token"] = "rgba(255, 255, 255, 0.1)"
            tokens["vignette_token"] = "radial-gradient(circle, transparent 20%, rgba(0,0,0,0.6) 100%)"
            # Auto-align contrasting text color if the brain didn't generate one
            if tokens.get("text_color") == "#0d0e12":
                tokens["text_color"] = "#ffffff"

        # Dynamic visual prompt generation for DALL-E / Midjourney mockup displays
        visual_prompt = f"Breathtaking premium website dashboard mockups for {project_name}, high-fidelity, styling tokens: bg {tokens['bg_color']}, accent {tokens['accent_primary']}, typography {tokens['font_heading']}, architecture aesthetic, 3D geometry {geometry_type}"

        # Inject Three.js geometry token into dynamic tokens
        tokens["geometry_type"] = geometry_type

        return {
            "project_name": project_name,
            "tokens": tokens,
            "sitemap": sitemap,
            "page_contexts": page_contexts,
            "visual_prompt": visual_prompt,
            "hero_global": hero_global
        }

    def get_soul(self):
        return self.soul_data
