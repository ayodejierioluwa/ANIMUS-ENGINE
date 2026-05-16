import os
import json
from components import HERO_TEMPLATE, THREE_JS_HERO_TEMPLATE, SCROLL_SECTION_TEMPLATE, CARD_TEMPLATE, FOOTER_TEMPLATE, GSAP_SCRIPT

class AnimusEngine:
    def __init__(self, output_dir="generated_site"):
        self.output_dir = output_dir
        self.project_name = "Aether Project"
        
    def generate_asset_plan(self, data):
        """Generates prompts for external AI sites (Midjourney, Luma, etc.) to match Viktor's workflow."""
        theme = data.get("hero_title", "Futuristic")
        plan = {
            "Midjourney_Hero_Image": f"/imagine prompt: A high-fidelity, premium {theme} website background, cinematic lighting, 8k, glassmorphism elements --ar 16:9",
            "Luma_AI_Video_Background": f"A cinematic, slow-motion sweeping shot of a {theme} digital landscape with glowing cyan particles and liquid metal textures.",
            "Spline_3D_Prompt": f"A high-detail, interactive 3D {theme} abstract geometry with soft shadows and metallic finish."
        }
        return plan

    def generate_site(self, data):
        """Generates a full interactive website from input data."""
        self.project_name = data.get("project_name", self.project_name)
        use_3d = data.get("use_3d", True)
        
        # 0. Generate Theme Tokens (The "WOW" Factor)
        theme_type = data.get("theme", "DARK_NEON")
        themes = {
            "DARK_NEON": {
                "bg_color": "#050505", "text_color": "#ffffff", "accent_primary": "#00ffcc", "accent_secondary": "#ff00ff",
                "glass_bg": "rgba(255, 255, 255, 0.03)", "glass_border": "rgba(255, 255, 255, 0.08)",
                "font_main": "'Inter', sans-serif", "font_heading": "'Outfit', sans-serif",
                "hero_gradient": "linear-gradient(to bottom, #fff 40%, rgba(255,255,255,0.4))"
            },
            "MINIMAL_LIGHT": {
                "bg_color": "#f8f9fa", "text_color": "#1a1a1a", "accent_primary": "#000000", "accent_secondary": "#6c757d",
                "glass_bg": "rgba(0, 0, 0, 0.02)", "glass_border": "rgba(0, 0, 0, 0.05)",
                "font_main": "'Inter', sans-serif", "font_heading": "'Inter', sans-serif",
                "hero_gradient": "linear-gradient(to bottom, #1a1a1a 40%, rgba(26,26,26,0.5))"
            },
            "LUXURY_GOLD": {
                "bg_color": "#0a0908", "text_color": "#eae0d5", "accent_primary": "#c6ac8f", "accent_secondary": "#5e503f",
                "glass_bg": "rgba(198, 172, 143, 0.05)", "glass_border": "rgba(198, 172, 143, 0.1)",
                "font_main": "'Inter', sans-serif", "font_heading": "'Outfit', sans-serif",
                "hero_gradient": "linear-gradient(to bottom, #c6ac8f 40%, #5e503f)"
            }
        }
        tokens = themes.get(theme_type, themes["DARK_NEON"])
        tokens["hero_gradient"] = tokens.get("hero_gradient", "linear-gradient(to bottom, #fff, transparent)")

        # 1. Build Hero (3D or Standard)
        template = THREE_JS_HERO_TEMPLATE if use_3d else HERO_TEMPLATE
        hero_html = template.format(
            title=data.get("hero_title", "Infinity Awaits"),
            subtitle=data.get("hero_subtitle", "Experience the future of interactive web design."),
            cta_text=data.get("cta_text", "Get Started"),
            cta_link=data.get("cta_link", "#")
        )
        
        # 2. Build Feature Cards
        cards_html = ""
        for card in data.get("features", []):
            cards_html += CARD_TEMPLATE.format(
                title=card.get("title", "Feature"),
                content=card.get("content", "Description goes here.")
            )
        
        feature_section_html = SCROLL_SECTION_TEMPLATE.format(cards=cards_html)
        
        # 3. Build Footer
        footer_html = FOOTER_TEMPLATE.format(project_name=self.project_name)
        
        # 4. Assemble Index.html
        base_dir = os.path.dirname(os.path.abspath(__file__))
        css_path = os.path.join(base_dir, "templates/base_styles.css")
        with open(css_path, "r") as f:
            styles = f.read()
            for key, value in tokens.items():
                styles = styles.replace(f"[[{key}]]", value)
            
        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.project_name} | AETHER_ANIMUS</title>
    <style>
        {styles}
    </style>
</head>
<body>
    {hero_html}
    {feature_section_html}
    {footer_html}
    {GSAP_SCRIPT}
</body>
</html>
"""
        
        # 5. Write to File
        os.makedirs(self.output_dir, exist_ok=True)
        with open(f"{self.output_dir}/index.html", "w") as f:
            f.write(full_html)
            
        # 6. Generate Asset Plan (The Viktor Guide Workflow)
        asset_plan = self.generate_asset_plan(data)
        with open(f"{self.output_dir}/asset_plan.json", "w") as f:
            json.dump(asset_plan, f, indent=4)
            
        return f"Successfully generated site in {self.output_dir}/index.html and asset_plan.json"

if __name__ == "__main__":
    # Test Generation
    test_data = {
        "project_name": "CORTEX_PRO",
        "hero_title": "THE ANIMUS SYSTEM",
        "hero_subtitle": "Autonomous Interactive Web Experiences. Built in seconds, not hours.",
        "features": [
            {"title": "GSAP Powered", "content": "Smooth, scroll-triggered animations that bring your content to life."},
            {"title": "Vibe Coding", "content": "Design through natural language. No manual CSS needed."},
            {"title": "Cloud Ready", "content": "One-click deployment to Netlify and Vercel."}
        ]
    }
    
    engine = AnimusEngine()
    print(engine.generate_site(test_data))
