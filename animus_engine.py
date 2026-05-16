import os
import json
from components import HERO_TEMPLATE, THREE_JS_HERO_TEMPLATE, SCROLL_SECTION_TEMPLATE, CARD_TEMPLATE, FOOTER_TEMPLATE, GSAP_SCRIPT

class AnimusEngine:
    def __init__(self, output_dir="generated_site"):
        self.output_dir = output_dir
        self.project_name = "Aether Project"
        
    def generate_site(self, data):
        """Generates a full interactive website from input data."""
        self.project_name = data.get("project_name", self.project_name)
        use_3d = data.get("use_3d", True)
        
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
        with open("aether_core/site_builder/templates/base_styles.css", "r") as f:
            styles = f.read()
            
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
            
        return f"Successfully generated site in {self.output_dir}/index.html"

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
