import os
import json
import logging
from animus_brain import AnimusBrain

logger = logging.getLogger(__name__)

class AnimusSoul:
    """
    The 'Soul' of the Animus Engine.
    Powered by the new ANIMUS Brain running on CORTEX intelligence with cognitive critique capabilities.
    """
    def __init__(self, mission_prompt, critique=None):
        self.mission = mission_prompt
        self.critique = critique
        self.brain = AnimusBrain()
        self.soul_data = self._ignite_consciousness()

    def _ignite_consciousness(self):
        logger.info(f"Igniting consciousness for mission: {self.mission[:100]}...")
        if self.critique:
            logger.info(f"Applying self-correction critique feedback: {self.critique[:150]}")
        
        # We query the AnimusBrain to generate a bespoke web design configuration
        brain_data = self.brain.generate_soul_data(self.mission, critique=self.critique)
        
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
            "breathing_anim_hover": "none"
        }
        for k, v in required_tokens.items():
            if k not in tokens:
                tokens[k] = v

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
