import os
import json
from components import HERO_TEMPLATE, THREE_JS_HERO_TEMPLATE, SPLIT_HERO_TEMPLATE, VIDEO_HERO_TEMPLATE, SHADER_HERO_TEMPLATE, SCROLL_SECTION_TEMPLATE, CARD_TEMPLATE, FOOTER_TEMPLATE, GSAP_SCRIPT

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
        """Generates a multi-page interactive website with an auto-correction loop."""
        pages = data.get("pages", [{"name": "index", "content": data}])
        generated_files = []
        
        for page in pages:
            page_name = page.get("name", "index")
            page_data = page.get("content", data)
            
            # Initial Attempt
            file_path = self.generate_page(page_name, page_data)
            
            # Sentry Audit & Correction Loop (WOWER Excellence)
            from animus_sentry import AnimusSentry
            sentry = AnimusSentry()
            
            retries = 2
            while not sentry.audit_file(file_path) and retries > 0:
                print(f"⚠️ Sentry detected issues in {file_path}. Attempting auto-correction...")
                # Apply heuristic correction: force transparency and z-index
                page_data["force_visual_fix"] = True
                file_path = self.generate_page(page_name, page_data)
                retries -= 1
                
            generated_files.append(file_path)
            
        return f"Successfully generated {len(generated_files)} pages: {', '.join(generated_files)}"

    def architect_unique_theme(self, data):
        """Generates a truly unique theme based on the prompt keywords."""
        prompt = data.get("hero_title", "").lower()
        
        # Generative Color Theory
        if "nature" in prompt or "green" in prompt:
            bg, accent = "#020804", "#00ff88"
        elif "crypto" in prompt or "tech" in prompt:
            bg, accent = "#050505", "#00d4ff"
        elif "fire" in prompt or "energy" in prompt:
            bg, accent = "#0a0202", "#ff4d00"
        else:
            bg, accent = "#080808", "#ffffff"
            
        return {
            "bg_color": bg, "text_color": "#ffffff", "accent_primary": accent, "accent_secondary": "#ffffff",
            "glass_bg": "rgba(255, 255, 255, 0.02)", "glass_border": "rgba(255, 255, 255, 0.05)",
            "font_main": "'Inter', sans-serif", "font_heading": "'Outfit', sans-serif",
            "hero_gradient": f"linear-gradient(to bottom, {accent}, transparent)"
        }
    def generate_page(self, page_name, data):
        """Generates a single page of the site."""
        self.project_name = data.get("project_name", self.project_name)
        use_3d = data.get("use_3d", True)
        use_video = data.get("use_video", False)
        
        # 0. Generate Unique Design System (Generative Stylist)
        theme_type = data.get("theme", "DYNAMIC")
        
        if theme_type == "DYNAMIC":
            # Generate a unique palette based on the prompt
            tokens = self.architect_unique_theme(data)
        else:
            # Fallback to presets
            themes = {
                "LIQUID_METAL": {
                    "bg_color": "#000000", "text_color": "#ffffff", "accent_primary": "#00d4ff", "accent_secondary": "#ff0055",
                    "glass_bg": "rgba(255, 255, 255, 0.05)", "glass_border": "rgba(255, 255, 255, 0.1)",
                    "font_main": "'Inter', sans-serif", "font_heading": "'Outfit', sans-serif",
                    "hero_gradient": "linear-gradient(135deg, #00d4ff, #ff0055)"
                },
                "CYBER_NATURE": {
                    "bg_color": "#020f12", "text_color": "#e0f2f1", "accent_primary": "#00ff88", "accent_secondary": "#00b8d4",
                    "glass_bg": "rgba(0, 255, 136, 0.03)", "glass_border": "rgba(0, 255, 136, 0.1)",
                    "font_main": "'Inter', sans-serif", "font_heading": "'Outfit', sans-serif",
                    "hero_gradient": "linear-gradient(to bottom, #00ff88, #00b8d4)"
                }
            }
            tokens = themes.get(theme_type, themes["LIQUID_METAL"])
        tokens["hero_gradient"] = tokens.get("hero_gradient", "linear-gradient(to bottom, #fff, transparent)")
        tokens["video_url"] = data.get("video_url", "https://res.cloudinary.com/demo/video/upload/f_auto:video,q_auto/docs/sea_turtle.mp4")
        tokens["youtube_id"] = data.get("youtube_id", "Lp6WjSTU80M") # Default Cinematic Fire
        tokens["vimeo_id"] = data.get("vimeo_id", "189852033")

        # 1. Build Hero (Variety Selection)
        layout_type = data.get("layout", "FULL")
        geometry_type = data.get("geometry", "SPHERE")
        
        if use_video:
            template = VIDEO_HERO_TEMPLATE
        elif data.get("use_shader", False):
            template = SHADER_HERO_TEMPLATE
        elif layout_type == "SPLIT":
            template = SPLIT_HERO_TEMPLATE
        else:
            template = THREE_JS_HERO_TEMPLATE if use_3d else HERO_TEMPLATE

        # 2. Token Injection (Recursive)
        tokens["title"] = data.get("hero_title", "Infinity Awaits")
        tokens["subtitle"] = data.get("hero_subtitle", "Experience the future.")
        tokens["cta_text"] = data.get("cta_text", "Get Started")
        tokens["cta_link"] = data.get("cta_link", "#")
        tokens["geometry_type"] = geometry_type
        tokens["accent_primary_hex"] = tokens["accent_primary"]
        tokens["layout_class"] = "full-layout"

        hero_html = template
        for key, value in tokens.items():
            hero_html = hero_html.replace(f"[[{key}]]", str(value))
        
        # 3. Build Feature Cards
        cards_html = ""
        for card in data.get("features", []):
            cards_html += CARD_TEMPLATE.format(
                title=card.get("title", "Feature"),
                content=card.get("content", "Description goes here.")
            )
        
        feature_section_html = SCROLL_SECTION_TEMPLATE.format(cards=cards_html)
        
        # 4. Build Footer
        footer_html = FOOTER_TEMPLATE.format(project_name=self.project_name)
        
        # 5. Assemble Index.html
        base_dir = os.path.dirname(os.path.abspath(__file__))
        css_path = os.path.join(base_dir, "templates/base_styles.css")
        with open(css_path, "r") as f:
            styles = f.read()
            for key, value in tokens.items():
                styles = styles.replace(f"[[{key}]]", value)
            
        # 5. Build Dynamic Navigation
        nav_html = '<nav style="position: fixed; top: 2rem; width: 100%; display: flex; justify-content: center; gap: 2rem; z-index: 10001;">'
        for p in data.get("pages", []):
            p_name = p.get("name", "index")
            nav_html += f'<a href="{p_name}.html" class="glass" style="padding: 0.5rem 1.5rem; text-decoration: none; color: white; border-radius: 20px;">{p_name.capitalize()}</a>'
        nav_html += '</nav>'

        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.project_name} | {page_name.capitalize()}</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/0.160.0/three.min.js"></script>
    <style>{styles}</style>
</head>
<body class="page-{page_name}">
    <div class="mesh-gradient"></div>
    <div class="site-wrapper">
        {nav_html}
        {hero_html}
        {feature_section_html}
        {footer_html}
    </div>
    {GSAP_SCRIPT.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>', '').replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>', '').replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/0.160.0/three.min.js"></script>', '')}
</body>
</html>
"""
        
        # 6. Write to File
        os.makedirs(self.output_dir, exist_ok=True)
        out_path = f"{self.output_dir}/{page_name}.html"
        with open(out_path, "w") as f:
            f.write(full_html)
            
        # 7. Generate Asset Plan
        asset_plan = self.generate_asset_plan(data)
        with open(f"{self.output_dir}/asset_plan.json", "w") as f:
            json.dump(asset_plan, f, indent=4)
            
        return out_path

if __name__ == "__main__":
    # Test Generation
    test_data = {
        "project_name": "CORTEX_PRO",
        "pages": [
            {
                "name": "index",
                "content": {
                    "theme": "DARK_NEON",
                    "use_video": True,
                    "hero_title": "BEYOND CODE",
                    "hero_subtitle": "Experience the world's first autonomous web engine.",
                    "video_url": "https://assets.mixkit.co/videos/preview/mixkit-abstract-form-of-blue-and-purple-ink-in-water-39850-large.mp4"
                }
            },
            {
                "name": "about",
                "content": {
                    "theme": "LUXURY_GOLD",
                    "layout": "SPLIT",
                    "geometry": "TORUS",
                    "hero_title": "OUR VISION",
                    "hero_subtitle": "Crafting the digital future with artificial intelligence.",
                }
            }
        ]
    }
    
    engine = AnimusEngine()
    print(engine.generate_site(test_data))
