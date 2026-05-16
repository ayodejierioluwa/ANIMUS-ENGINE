import json

class AnimusSoul:
    """
    The 'Soul' of the Animus Engine. 
    Now equipped with 'Deep Page Intelligence' and 'Active Nav Logic'.
    """
    def __init__(self, mission_prompt):
        self.mission = mission_prompt
        self.soul_data = self._ignite_consciousness()

    def _ignite_consciousness(self):
        tokens = self._calculate_atmospheric_dna()
        sitemap = self._generate_sitemap()
        
        m = self.mission.lower()
        project_name = "NEURAL_CORE" if any(x in m for x in ["crypto", "tech"]) else "AETHER_FLOW" if any(x in m for x in ["nature", "wellness"]) else "ANIMUS_GEN"
        
        # Generate Unique Context for every page in the sitemap
        page_contexts = {}
        for page in sitemap:
            page_contexts[page["file"]] = self._generate_page_content(page["name"], m)

        return {
            "project_name": project_name,
            "tokens": tokens,
            "sitemap": sitemap,
            "page_contexts": page_contexts,
            "hero_global": { "cta": "START_ACTION" if "tech" in m else "EXPLORE" }
        }

    def _generate_page_content(self, page_name, mission):
        """
        Deep Intelligence: Generates unique copy/features for specific page roles.
        """
        # --- TECH / SURGICAL ---
        if any(x in mission for x in ["crypto", "tech", "surgical"]):
            if page_name == "Home":
                return {
                    "title": "NEURAL OVERRIDE", "subtitle": "Surgical precision for the sovereign architect.",
                    "features": [
                        {"icon": "⚡", "title": "Neural Latency", "description": "0.01ms execution via localized mesh nodes."},
                        {"icon": "📈", "title": "Hyper Alpha", "description": "Predictive models tuned to the heartbeat of the chain."}
                    ]
                }
            if page_name == "Terminal":
                return {
                    "title": "DATA TERMINAL", "subtitle": "Real-time bridge to the liquidity layers.",
                    "features": [
                        {"icon": "📟", "title": "Stream Logic", "description": "Raw data feeds with zero-buffer processing."},
                        {"icon": "🔗", "title": "Multi-Chain Sync", "description": "Simultaneous execution across 12+ EVM layers."}
                    ]
                }
            if page_name == "Security":
                return {
                    "title": "BLACK BOX", "subtitle": "Hardened encryption for high-stakes operations.",
                    "features": [
                        {"icon": "🛡️", "title": "Surgical Shield", "description": "Self-destructing keys on any unauthorized probe."},
                        {"icon": "🔐", "title": "Cold State", "description": "Air-gapped transaction signing for max security."}
                    ]
                }
        
        # --- NATURE / WELLNESS ---
        elif any(x in mission for x in ["nature", "wellness", "organic"]):
            if page_name == "Home":
                return {
                    "title": "AETHER FLOW", "subtitle": "Breathe into the digital sanctuary of the future.",
                    "features": [
                        {"icon": "🌿", "title": "Organic Growth", "description": "Systems that evolve like a living forest."},
                        {"icon": "✨", "title": "Pure Essence", "description": "Zero noise, 100% intentionality."}
                    ]
                }
            if page_name == "Sanctuary":
                return {
                    "title": "THE SANCTUARY", "subtitle": "A silent space for deep digital meditation.",
                    "features": [
                        {"icon": "🕯️", "title": "Calm State", "description": "Muted visual frequencies to reduce sensory load."},
                        {"icon": "🌬️", "title": "Air Logic", "description": "Space and breath integrated into the layout."}
                    ]
                }

        # --- DEFAULT / LUXURY ---
        return {
            "title": f"{page_name.upper()}", "subtitle": f"Experience the {page_name} layer of the Animus.",
            "features": [
                {"icon": "💎", "title": "Premium Logic", "description": "Excellence in every interaction."},
                {"icon": "🚀", "title": "Future Ready", "description": "Scaling beyond the current limits of code."}
            ]
        }

    def _generate_sitemap(self):
        m = self.mission.lower()
        if any(x in m for x in ["crypto", "tech"]):
            return [{"name": "Home", "file": "index.html"}, {"name": "Terminal", "file": "terminal.html"}, {"name": "Security", "file": "security.html"}]
        if any(x in m for x in ["nature", "wellness"]):
            return [{"name": "Home", "file": "index.html"}, {"name": "Sanctuary", "file": "sanctuary.html"}]
        return [{"name": "Home", "file": "index.html"}, {"name": "Work", "file": "work.html"}]

    def _calculate_atmospheric_dna(self):
        m = self.mission.lower()
        dna = {
            "bg_color": "#050505", "text_color": "#ffffff", "accent_primary": "#00d4ff",
            "glass_blur": "25px", "grid_radius": "32px", "btn_radius": "50px", "void_blur": "40px",
            "font_heading": "'Outfit'", "font_body": "'Inter'",
            "ease_vibe": "cubic-bezier(0.2, 0.8, 0.2, 1)", "duration_vibe": "0.6s",
            "hover_glow": "0 20px 40px rgba(0,0,0,0.4)", "letter_spacing": "-0.02em", "text_transform": "none",
            "breathing_anim": "none", "breathing_anim_hover": "none"
        }
        if any(x in m for x in ["crypto", "tech"]):
            dna.update({
                "bg_color": "#000000", "accent_primary": "#00ffcc", "glass_blur": "5px", "grid_radius": "0px", "btn_radius": "2px", "void_blur": "0px",
                "font_heading": "'Space Mono'", "font_body": "'Space Mono'", "ease_vibe": "cubic-bezier(0.19, 1, 0.22, 1)", "duration_vibe": "0.3s",
                "hover_glow": "0 0 30px rgba(0, 255, 204, 0.3)", "letter_spacing": "0.1em", "text_transform": "uppercase"
            })
        elif any(x in m for x in ["nature", "wellness"]):
            dna.update({
                "bg_color": "#0a0c0a", "accent_primary": "#a8e6cf", "glass_blur": "60px", "grid_radius": "80px", "btn_radius": "100px", "void_blur": "150px",
                "font_heading": "'Playfair Display'", "font_body": "'Inter'", "ease_vibe": "cubic-bezier(0.4, 0, 0.2, 1)", "duration_vibe": "1.5s",
                "hover_glow": "0 40px 80px rgba(0,0,0,0.2)", "letter_spacing": "-0.05em", "text_transform": "none",
                "breathing_anim": "aether-breath", "breathing_anim_hover": "aether-breath-deep"
            })
        return dna

    def get_soul(self):
        return self.soul_data
