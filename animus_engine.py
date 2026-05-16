import os
import json
from components import (
    HERO_TEMPLATE, THREE_JS_HERO_TEMPLATE, SPLIT_HERO_TEMPLATE, 
    VIDEO_HERO_TEMPLATE, SHADER_HERO_TEMPLATE, SCROLL_SECTION_TEMPLATE, 
    CARD_TEMPLATE, FOOTER_TEMPLATE, GSAP_SCRIPT, BASE_HTML, 
    FEATURE_GRID_TEMPLATE, FEATURE_ITEM_TEMPLATE, NAV_BAR_TEMPLATE, NAV_LINK_TEMPLATE
)
from soul_generator import AnimusSoul

class AnimusEngine:
    def __init__(self, output_dir="generated_site"):
        self.output_dir = output_dir
        self.project_name = "Aether Project"
        
    def architect_unique_theme(self, soul_data):
        return soul_data["tokens"]

    def generate_project(self, mission):
        """
        The 'Master Build' Command.
        Takes a mission and builds the entire autonomous project.
        """
        print(f"🚀 IGNITING PROJECT: {mission}")
        soul = AnimusSoul(mission)
        soul_data = soul.get_soul()
        self.project_name = soul_data["project_name"]
        
        generated_files = []
        for page in soul_data["sitemap"]:
            file_name = page["file"].replace(".html", "")
            file_path = self.generate_page(file_name, {"mission": mission}, soul_data=soul_data)
            generated_files.append(file_path)
            
        print(f"✅ PROJECT COMPLETE: {len(generated_files)} pages generated.")
        return generated_files

    def generate_page(self, page_name, data, soul_data=None):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
        # 1. Soul Retrieval
        if soul_data is None:
            soul = AnimusSoul(data.get("mission", "Digital Innovation"))
            soul_data = soul.get_soul()
        
        self.project_name = soul_data["project_name"]
        
        # 2. Design System
        tokens = soul_data["tokens"]
        
        # 3. Build Navigation (Interactive Sitemap)
        nav_links_html = ""
        for page in soul_data["sitemap"]:
            link = NAV_LINK_TEMPLATE.replace("[[link]]", page["file"])
            link = link.replace("[[name]]", page["name"])
            nav_links_html += link
            
        nav_html = NAV_BAR_TEMPLATE.replace("[[project_name]]", self.project_name)
        nav_html = nav_html.replace("[[nav_links]]", nav_links_html)
        nav_html = nav_html.replace("[[cta_text]]", soul_data["hero"]["cta"])

        # 4. Build Hero
        use_shader = data.get("use_shader", False)
        use_3d = data.get("use_3d", False)
        
        template = VIDEO_HERO_TEMPLATE # Standardized hero
        if use_shader: template = SHADER_HERO_TEMPLATE
        elif use_3d: template = THREE_JS_HERO_TEMPLATE

        hero_html = template
        hero_html = hero_html.replace("[[title]]", soul_data["hero"]["title"] if page_name == "index" else page_name.upper())
        hero_html = hero_html.replace("[[subtitle]]", soul_data["hero"]["subtitle"])
        hero_html = hero_html.replace("[[cta_text]]", soul_data["hero"]["cta"])
        hero_html = hero_html.replace("[[cta_link]]", "#")
        hero_html = hero_html.replace("[[accent_primary_hex]]", tokens["accent_primary"])
        hero_html = hero_html.replace("[[geometry_type]]", "SPHERE")
        hero_html = hero_html.replace("[[layout_class]]", "full-layout")

        # 5. Build Feature Grid
        feature_items_html = ""
        for feat in soul_data["features"]:
            item = FEATURE_ITEM_TEMPLATE.replace("[[icon]]", feat["icon"])
            item = item.replace("[[title]]", feat["title"])
            item = item.replace("[[description]]", feat["description"])
            feature_items_html += item
        
        grid_html = FEATURE_GRID_TEMPLATE.replace("[[features]]", feature_items_html)
        
        # 6. Build Footer
        footer_html = FOOTER_TEMPLATE.replace("{project_name}", self.project_name)
        
        # 7. Final Assembly
        body_content = nav_html + hero_html + grid_html + footer_html
        
        full_page = BASE_HTML.replace("[[title]]", f"{self.project_name} | {page_name.capitalize()}")
        full_page = full_page.replace("[[body]]", body_content)
        
        # Vibe Shift Injection
        for key, value in tokens.items():
            full_page = full_page.replace(f"[[{key}]]", str(value))

        file_path = f"{self.output_dir}/{page_name}.html"
        with open(file_path, "w") as f:
            f.write(full_page)
            
        return file_path
