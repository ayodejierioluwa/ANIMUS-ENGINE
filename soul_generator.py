import json

class AnimusSoul:
    """
    The 'Soul' of the Animus Engine. 
    It takes a core mission and generates the brand voice, copy, and structural data.
    Now equipped with the 'Vibe Shift' engine to calculate design tokens.
    """
    def __init__(self, mission_prompt):
        self.mission = mission_prompt
        self.soul_data = self._ignite_consciousness()

    def _ignite_consciousness(self):
        # 1. Calculate Design Tokens (Vibe Shift Engine)
        tokens = self._calculate_vibe_tokens()
        
        # 2. Generate Content
        if "crypto" in self.mission.lower() or "wealth" in self.mission.lower():
            return {
                "hero": {
                    "title": "NEURAL WEALTH",
                    "subtitle": "Decentralized intelligence for the next generation of sovereign capital.",
                    "cta": "ENTER THE VOID"
                },
                "features": [
                    {"icon": "⚡", "title": "Zero Latency", "description": "Execute trades at the speed of thought with our neural bridge."},
                    {"icon": "🛡️", "title": "Quantum Shield", "description": "Security that transcends standard encryption protocols."},
                    {"icon": "📈", "title": "Predictive Alpha", "description": "Deep learning models that spot trends before the market moves."}
                ],
                "tokens": tokens
            }
        
        return {
            "hero": {
                "title": "BEYOND CODE",
                "subtitle": "Engineering digital experiences that transcend the ordinary.",
                "cta": "START BUILDING"
            },
            "features": [
                {"icon": "🎨", "title": "Visual Excellence", "description": "High-fidelity aesthetics that redefine digital luxury."},
                {"icon": "⚙️", "title": "Autonomous Logic", "description": "Self-healing systems that evolve with your user base."},
                {"icon": "🌐", "title": "Global Scale", "description": "Infrastructure designed for infinite expansion."}
            ],
            "tokens": tokens
        }

    def _calculate_vibe_tokens(self):
        """
        The 'Vibe Shift' Engine.
        Calculates CSS tokens based on the emotional intensity of the mission.
        """
        m = self.mission.lower()
        
        # Defaults (Luxury / Modern)
        tokens = {
            "glass_blur": "20px",
            "grid_radius": "32px",
            "btn_radius": "50px",
            "void_blur": "40px"
        }
        
        # Aggressive / Tech / Surgical Vibe
        if any(x in m for x in ["crypto", "tech", "surgical", "neural", "precision"]):
            tokens["glass_blur"] = "10px"
            tokens["grid_radius"] = "8px"
            tokens["btn_radius"] = "4px"
            tokens["void_blur"] = "10px"
            
        # Nature / Soft / Organic Vibe
        elif any(x in m for x in ["nature", "soft", "organic", "wellness"]):
            tokens["glass_blur"] = "40px"
            tokens["grid_radius"] = "60px"
            tokens["btn_radius"] = "80px"
            tokens["void_blur"] = "100px"
            
        return tokens

    def get_soul(self):
        return self.soul_data
