import os
import json
from components import (
    HERO_TEMPLATE, THREE_JS_HERO_TEMPLATE, SPLIT_HERO_TEMPLATE, 
    VIDEO_HERO_TEMPLATE, SHADER_HERO_TEMPLATE, IMAGE_HERO_TEMPLATE, SCROLL_SECTION_TEMPLATE, 
    CARD_TEMPLATE, FOOTER_TEMPLATE, GSAP_SCRIPT, BASE_HTML, 
    FEATURE_GRID_TEMPLATE, FEATURE_ITEM_TEMPLATE, NAV_BAR_TEMPLATE, NAV_LINK_TEMPLATE,
    SENTRY_REPORT_TEMPLATE, SOVEREIGN_SEAL_TEMPLATE
)
from soul_generator import AnimusSoul

class AnimusEngine:
    def __init__(self, output_dir="generated_site"):
        self.output_dir = output_dir
        self.project_name = "Aether Project"
        
    def generate_project(self, mission, hero_image=None):
        """
        The 'Master Build' Command.
        Now integrates the 'Mind's Eye' visual.
        """
        print(f"🚀 IGNITING PROJECT: {mission}")
        soul = AnimusSoul(mission)
        soul_data = soul.get_soul()
        self.project_name = soul_data["project_name"]
        
        generated_files = []
        for page in soul_data["sitemap"]:
            file_name = page["file"].replace(".html", "")
            # Apply hero image only to index
            image = hero_image if file_name == "index" else None
            file_path = self.generate_page(file_name, {"mission": mission}, soul_data=soul_data, hero_image=image)
            generated_files.append(file_path)
            
        print(f"✅ PROJECT COMPLETE: {len(generated_files)} pages generated.")
        return generated_files

    def generate_page(self, page_name, data, soul_data=None, hero_image=None):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
        if soul_data is None:
            soul = AnimusSoul(data.get("mission", "Digital Innovation"))
            soul_data = soul.get_soul()
        
        self.project_name = soul_data["project_name"]
        tokens = soul_data["tokens"]
        page_file = f"{page_name}.html"
        context = soul_data["page_contexts"].get(page_file, soul_data["page_contexts"].get("index.html"))
        
        # 3. Build Navigation (Interactive Sitemap + Active State)
        nav_links_html = ""
        for page in soul_data["sitemap"]:
            link_html = NAV_LINK_TEMPLATE.replace("[[link]]", page["file"])
            link_html = link_html.replace("[[name]]", page["name"])
            is_active = (page["file"] == page_file)
            link_html = link_html.replace("[[active_class]]", "active" if is_active else "")
            nav_links_html += link_html
            
        nav_html = NAV_BAR_TEMPLATE.replace("[[project_name]]", self.project_name)
        nav_html = nav_html.replace("[[nav_links]]", nav_links_html)
        nav_html = nav_html.replace("[[cta_text]]", soul_data["hero_global"]["cta"])

        # 4. Build Hero (Dynamic Type: Image vs Video/Void)
        template = IMAGE_HERO_TEMPLATE if hero_image else VIDEO_HERO_TEMPLATE
        
        hero_html = template
        hero_html = hero_html.replace("[[title]]", context["title"])
        hero_html = hero_html.replace("[[subtitle]]", context["subtitle"])
        hero_html = hero_html.replace("[[cta_text]]", soul_data["hero_global"]["cta"])
        hero_html = hero_html.replace("[[cta_link]]", "#")
        hero_html = hero_html.replace("[[image_url]]", hero_image if hero_image else "")
        hero_html = hero_html.replace("[[layout_class]]", "full-layout")

        # 5. Build Feature Grid
        feature_items_html = ""
        for feat in context["features"]:
            item = FEATURE_ITEM_TEMPLATE.replace("[[icon]]", feat["icon"])
            item = item.replace("[[title]]", feat["title"])
            item = item.replace("[[description]]", feat["description"])
            feature_items_html += item
        
        grid_html = FEATURE_GRID_TEMPLATE.replace("[[features]]", feature_items_html)
        
        # 6. Build Footer
        footer_html = FOOTER_TEMPLATE.replace("{project_name}", self.project_name)
        
        # 7. Final Assembly
        body_content = nav_html + hero_html + grid_html + footer_html + \
                       SENTRY_REPORT_TEMPLATE.replace("[[sentry_status]]", "PASSED_SURGICAL_AUDIT") + \
                       SOVEREIGN_SEAL_TEMPLATE
        
        full_page = BASE_HTML.replace("[[title]]", f"{self.project_name} | {page_name.capitalize()}")
        full_page = full_page.replace("[[body]]", body_content)
        
        # Vibe Shift Injection
        for key, value in tokens.items():
            full_page = full_page.replace(f"[[{key}]]", str(value))

        file_path = f"{self.output_dir}/{page_name}.html"
        with open(file_path, "w") as f:
            f.write(full_page)
            
        return file_path
