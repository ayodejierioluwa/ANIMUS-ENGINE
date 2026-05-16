import json

class AnimusSoul:
    """
    The 'Soul' of the Animus Engine. 
    Now equipped with the 'Elite Atmospheric DNA' engine.
    """
    def __init__(self, mission_prompt):
        self.mission = mission_prompt
        self.soul_data = self._ignite_consciousness()

    def _ignite_consciousness(self):
        # 1. Calculate Atmospheric DNA
        tokens = self._calculate_atmospheric_dna()
        
        # 2. Generate Content
        m = self.mission.lower()
        if any(x in m for x in ["crypto", "tech", "neural", "precision", "surgical"]):
            content = {
                "hero": {
                    "title": "NEURAL OVERRIDE",
                    "subtitle": "Precision intelligence for the sovereign architect.",
                    "cta": "IGNITE BRIDGE"
                },
                "features": [
                    {"icon": "⚡", "title": "Neural Latency", "description": "0.01ms execution via localized mesh nodes."},
                    {"icon": "🛡️", "title": "Black Box", "description": "Surgical encryption protocols that self-destruct on breach."},
                    {"icon": "📈", "title": "Hyper Alpha", "description": "Predictive models tuned to the heartbeat of the chain."}
                ]
            }
        elif any(x in m for x in ["nature", "soft", "organic", "wellness"]):
            content = {
                "hero": {
                    "title": "AETHER FLOW",
                    "subtitle": "Breathe into the digital sanctuary of the future.",
                    "cta": "BEGIN ASCENSION"
                },
                "features": [
                    {"icon": "🌿", "title": "Organic Growth", "description": "Systems that evolve like a living forest."},
                    {"icon": "🌊", "title": "Fluid State", "description": "Transitions as smooth as water on stone."},
                    {"icon": "✨", "title": "Pure Essence", "description": "Zero noise, 100% intentionality in every pixel."}
                ]
            }
        else:
            content = {
                "hero": {
                    "title": "BEYOND CODE",
                    "subtitle": "Engineering digital luxury that transcends the ordinary.",
                    "cta": "START BUILDING"
                },
                "features": [
                    {"icon": "🎨", "title": "Visual Soul", "description": "High-fidelity aesthetics that redefine digital luxury."},
                    {"icon": "⚙️", "title": "Self-Healing", "description": "Systems that evolve with your user base."},
                    {"icon": "🌐", "title": "Infinite Scale", "description": "Infrastructure designed for global expansion."}
                ]
            }
            
        content["tokens"] = tokens
        return content

    def _calculate_atmospheric_dna(self):
        """
        The 'Elite Vibe Shift' Engine.
        Re-engineers typography, physics, and interactive behaviors.
        """
        m = self.mission.lower()
        
        # Default: Modern Luxury
        dna = {
            "bg_color": "#050505",
            "text_color": "#ffffff",
            "accent_primary": "#00d4ff",
            "glass_blur": "25px",
            "grid_radius": "32px",
            "btn_radius": "50px",
            "void_blur": "40px",
            "font_heading": "'Outfit'",
            "font_body": "'Inter'",
            "ease_vibe": "cubic-bezier(0.2, 0.8, 0.2, 1)",
            "duration_vibe": "0.6s",
            "hover_glow": "0 20px 40px rgba(0,0,0,0.4)",
            "letter_spacing": "-0.02em",
            "text_transform": "none"
        }
        
        # TECH / SURGICAL / NEURAL
        if any(x in m for x in ["crypto", "tech", "precision", "surgical", "neural"]):
            dna["bg_color"] = "#000000"
            dna["accent_primary"] = "#00ffcc"
            dna["glass_blur"] = "5px"
            dna["grid_radius"] = "0px"
            dna["btn_radius"] = "2px"
            dna["void_blur"] = "0px"
            dna["font_heading"] = "'Space Mono'"
            dna["font_body"] = "'Space Mono'"
            dna["ease_vibe"] = "cubic-bezier(0.19, 1, 0.22, 1)" # Snappy
            dna["duration_vibe"] = "0.3s"
            dna["hover_glow"] = "0 0 30px rgba(0, 255, 204, 0.3)"
            dna["letter_spacing"] = "0.1em"
            dna["text_transform"] = "uppercase"

        # NATURE / ORGANIC / WELLNESS
        elif any(x in m for x in ["nature", "organic", "wellness", "soft"]):
            dna["bg_color"] = "#0a0c0a"
            dna["accent_primary"] = "#a8e6cf"
            dna["glass_blur"] = "60px"
            dna["grid_radius"] = "80px"
            dna["btn_radius"] = "100px"
            dna["void_blur"] = "150px"
            dna["font_heading"] = "'Playfair Display'"
            dna["font_body"] = "'Inter'"
            dna["ease_vibe"] = "cubic-bezier(0.4, 0, 0.2, 1)" # Fluid
            dna["duration_vibe"] = "1.5s"
            dna["hover_glow"] = "0 40px 80px rgba(0,0,0,0.2)"
            dna["letter_spacing"] = "-0.05em"
            dna["text_transform"] = "none"
            
        return dna

    def get_soul(self):
        return self.soul_data
