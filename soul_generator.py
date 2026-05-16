import json

class AnimusSoul:
    """
    The 'Soul' of the Animus Engine. 
    Now equipped with the 'Neural Sitemap' engine.
    """
    def __init__(self, mission_prompt):
        self.mission = mission_prompt
        self.soul_data = self._ignite_consciousness()

    def _ignite_consciousness(self):
        # 1. Calculate Atmospheric DNA
        tokens = self._calculate_atmospheric_dna()
        
        # 2. Map the Neural Sitemap
        sitemap = self._generate_sitemap()
        
        # 3. Generate Core Identity
        m = self.mission.lower()
        if any(x in m for x in ["crypto", "tech", "neural", "precision", "surgical"]):
            identity = {
                "project_name": "NEURAL_CORE",
                "hero": { "title": "NEURAL OVERRIDE", "subtitle": "Precision intelligence for the sovereign architect.", "cta": "IGNITE BRIDGE" },
                "features": [
                    {"icon": "⚡", "title": "Neural Latency", "description": "0.01ms execution via localized mesh nodes."},
                    {"icon": "🛡️", "title": "Black Box", "description": "Surgical encryption protocols that self-destruct on breach."},
                    {"icon": "📈", "title": "Hyper Alpha", "description": "Predictive models tuned to the heartbeat of the chain."}
                ]
            }
        elif any(x in m for x in ["nature", "soft", "organic", "wellness"]):
            identity = {
                "project_name": "AETHER_FLOW",
                "hero": { "title": "AETHER FLOW", "subtitle": "Breathe into the digital sanctuary of the future.", "cta": "BEGIN ASCENSION" },
                "features": [
                    {"icon": "🌿", "title": "Organic Growth", "description": "Systems that evolve like a living forest."},
                    {"icon": "🌊", "title": "Fluid State", "description": "Transitions as smooth as water on stone."},
                    {"icon": "✨", "title": "Pure Essence", "description": "Zero noise, 100% intentionality in every pixel."}
                ]
            }
        else:
            identity = {
                "project_name": "ANIMUS_GEN",
                "hero": { "title": "BEYOND CODE", "subtitle": "Engineering digital luxury that transcends the ordinary.", "cta": "START BUILDING" },
                "features": [
                    {"icon": "🎨", "title": "Visual Soul", "description": "High-fidelity aesthetics that redefine digital luxury."},
                    {"icon": "⚙️", "title": "Self-Healing", "description": "Systems that evolve with your user base."},
                    {"icon": "🌐", "title": "Infinite Scale", "description": "Infrastructure designed for global expansion."}
                ]
            }
            
        identity["tokens"] = tokens
        identity["sitemap"] = sitemap
        return identity

    def _generate_sitemap(self):
        """
        The 'Neural Sitemap' Engine.
        Decides which pages a project needs based on the mission.
        """
        m = self.mission.lower()
        sitemap = [
            {"name": "Home", "file": "index.html"},
        ]
        
        if any(x in m for x in ["crypto", "tech"]):
            sitemap += [
                {"name": "Terminal", "file": "terminal.html"},
                {"name": "Security", "file": "security.html"},
                {"name": "Connect", "file": "connect.html"}
            ]
        elif any(x in m for x in ["nature", "wellness", "organic"]):
            sitemap += [
                {"name": "Sanctuary", "file": "sanctuary.html"},
                {"name": "Essence", "file": "essence.html"},
                {"name": "Rituals", "file": "rituals.html"}
            ]
        else:
            sitemap += [
                {"name": "Work", "file": "work.html"},
                {"name": "About", "file": "about.html"},
                {"name": "Contact", "file": "contact.html"}
            ]
            
        return sitemap

    def _calculate_atmospheric_dna(self):
        m = self.mission.lower()
        
        # Default: Modern Luxury
        dna = {
            "bg_color": "#050505", "text_color": "#ffffff", "accent_primary": "#00d4ff",
            "glass_blur": "25px", "grid_radius": "32px", "btn_radius": "50px", "void_blur": "40px",
            "font_heading": "'Outfit'", "font_body": "'Inter'",
            "ease_vibe": "cubic-bezier(0.2, 0.8, 0.2, 1)", "duration_vibe": "0.6s",
            "hover_glow": "0 20px 40px rgba(0,0,0,0.4)", "letter_spacing": "-0.02em", "text_transform": "none",
            "breathing_anim": "none", "breathing_anim_hover": "none"
        }
        
        # TECH / SURGICAL / NEURAL
        if any(x in m for x in ["crypto", "tech", "precision", "surgical", "neural"]):
            dna.update({
                "bg_color": "#000000", "accent_primary": "#00ffcc", "glass_blur": "5px",
                "grid_radius": "0px", "btn_radius": "2px", "void_blur": "0px",
                "font_heading": "'Space Mono'", "font_body": "'Space Mono'",
                "ease_vibe": "cubic-bezier(0.19, 1, 0.22, 1)", "duration_vibe": "0.3s",
                "hover_glow": "0 0 30px rgba(0, 255, 204, 0.3)", "letter_spacing": "0.1em", "text_transform": "uppercase"
            })

        # NATURE / ORGANIC / WELLNESS
        elif any(x in m for x in ["nature", "organic", "wellness", "soft"]):
            dna.update({
                "bg_color": "#0a0c0a", "accent_primary": "#a8e6cf", "glass_blur": "60px",
                "grid_radius": "80px", "btn_radius": "100px", "void_blur": "150px",
                "font_heading": "'Playfair Display'", "font_body": "'Inter'",
                "ease_vibe": "cubic-bezier(0.4, 0, 0.2, 1)", "duration_vibe": "1.5s",
                "hover_glow": "0 40px 80px rgba(0,0,0,0.2)", "letter_spacing": "-0.05em", "text_transform": "none",
                "breathing_anim": "aether-breath", "breathing_anim_hover": "aether-breath-deep"
            })
            
        return dna

    def get_soul(self):
        return self.soul_data
