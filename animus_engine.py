import os
import json
from components import (
    HERO_TEMPLATE, THREE_JS_HERO_TEMPLATE, SPLIT_HERO_TEMPLATE, 
    VIDEO_HERO_TEMPLATE, SHADER_HERO_TEMPLATE, SCROLL_SECTION_TEMPLATE, 
    CARD_TEMPLATE, FOOTER_TEMPLATE, GSAP_SCRIPT, BASE_HTML, 
    FEATURE_GRID_TEMPLATE, FEATURE_ITEM_TEMPLATE
)
from soul_generator import AnimusSoul

class AnimusEngine:
    def __init__(self, output_dir="generated_site"):
        self.output_dir = output_dir
        self.project_name = "Aether Project"
        
    def architect_unique_theme(self, data):
        prompt = data.get("mission", "").lower()
        if "crypto" in prompt or "wealth" in prompt:
            bg, accent = "#050505", "#00d4ff"
        elif "nature" in prompt:
            bg, accent = "#020804", "#00ff88"
        else:
            bg, accent = "#080808", "#ffffff"
            
        return {
            "bg_color": bg, "text_color": "#ffffff", "accent_primary": accent, "accent_secondary": "#ffffff",
            "glass_bg": "rgba(255, 255, 255, 0.02)", "glass_border": "rgba(255, 255, 255, 0.05)",
            "font_main": "'Inter', sans-serif", "font_heading": "'Outfit', sans-serif"
        }

    def generate_page(self, page_name, data):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
        # 1. Ignite the Soul
        soul = AnimusSoul(data.get("mission", "Digital Innovation"))
        soul_data = soul.get_soul()
        
        # 2. Design System
        tokens = self.architect_unique_theme(data)
        
        # 3. Build Hero
        use_shader = data.get("use_shader", False)
        use_3d = data.get("use_3d", False)
        
        if use_shader:
            template = SHADER_HERO_TEMPLATE
        elif use_3d:
            template = THREE_JS_HERO_TEMPLATE
        else:
            template = VIDEO_HERO_TEMPLATE # Now static in our latest components.py

        hero_html = template
        # Inject Soul Data into Hero
        hero_html = hero_html.replace("[[title]]", soul_data["hero"]["title"])
        hero_html = hero_html.replace("[[subtitle]]", soul_data["hero"]["subtitle"])
        hero_html = hero_html.replace("[[cta_text]]", soul_data["hero"]["cta"])
        hero_html = hero_html.replace("[[cta_link]]", "#")
        hero_html = hero_html.replace("[[layout_class]]", "full-layout")
        hero_html = hero_html.replace("[[accent_primary_hex]]", tokens["accent_primary"])
        hero_html = hero_html.replace("[[geometry_type]]", "SPHERE")

        # 4. Build Feature Grid (The Interaction)
        feature_items_html = ""
        for feat in soul_data["features"]:
            item = FEATURE_ITEM_TEMPLATE.replace("[[icon]]", feat["icon"])
            item = item.replace("[[title]]", feat["title"])
            item = item.replace("[[description]]", feat["description"])
            feature_items_html += item
        
        grid_html = FEATURE_GRID_TEMPLATE.replace("[[features]]", feature_items_html)
        
        # 5. Build Footer
        footer_html = FOOTER_TEMPLATE.replace("{project_name}", self.project_name)
        
        # 6. Final Assembly (With Vibe Shift Integration)
        body_content = hero_html + grid_html + footer_html
        
        full_page = BASE_HTML.replace("[[title]]", f"{soul_data['hero']['title']} | Animus Engine")
        full_page = full_page.replace("[[body]]", body_content)
        
        # Vibe Shift Injection: Mapping Soul Tokens to CSS Variables
        for key, value in soul_data["tokens"].items():
            full_page = full_page.replace(f"[[{key}]]", value)
            
        # Theme Injection (Legacy & Color)
        for key, value in tokens.items():
            full_page = full_page.replace(f"[[{key}]]", value)

        file_path = f"{self.output_dir}/{page_name}.html"
        with open(file_path, "w") as f:
            f.write(full_page)
            
        return file_path
