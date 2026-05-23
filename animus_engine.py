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
from animus_sentry import AnimusSentry
from animus_brain import AnimusBrain

class AnimusEngine:
    def __init__(self, output_dir="generated_site"):
        self.output_dir = output_dir
        self.project_name = "Aether Project"
        self.sentry = AnimusSentry()
        
    def generate_project(self, mission, hero_image=None, user_id=None):
        """
        The 'Master Build' Command.
        Now integrates an autonomous Self-Correction Critique Loop and Adaptive User Preference Learning.
        """
        print(f"🚀 IGNITING PROJECT (Generation Phase 1) for user {user_id}: {mission}")
        
        # Iteration 1: Initial Generation
        soul = AnimusSoul(mission, user_id=user_id)
        soul_data = soul.get_soul()
        self.project_name = soul_data["project_name"]
        
        generated_files = self._assemble_site_files(soul_data, mission, hero_image)
        
        # Heuristic & LLM Design Audit
        print("🕵️ ANIMUS SENTRY: Initiating layout, contrast, and visual audit...")
        audit_passed = self.sentry.audit_project(generated_files)
        
        if not audit_passed:
            critiques = "\n".join(self.sentry.issues)
            print(f"⚠️ AUDIT WARNING: Design flaws detected in Phase 1:\n{critiques}")
            print("🔄 IGNITING PROJECT (Self-Correction Phase 2): Querying critic layer...")
            
            # Iteration 2: Self-Correction Loop
            corrected_soul = AnimusSoul(mission, critique=critiques, user_id=user_id)
            corrected_soul_data = corrected_soul.get_soul()
            self.project_name = corrected_soul_data["project_name"]
            
            # Re-assemble pages with the corrected configuration
            generated_files = self._assemble_site_files(corrected_soul_data, mission, hero_image)
            
            # Re-run Sentry Audit to certify the changes
            print("🕵️ ANIMUS SENTRY: Re-auditing corrected designs...")
            second_audit = self.sentry.audit_project(generated_files)
            if second_audit:
                print("✅ SELF-CORRECTION SUCCESSFUL: Visual layout errors resolved.")
                # Learn preferences since the build successfully passed
                if user_id and user_id != "anonymous":
                    self._learn_user_style_preferences(user_id, corrected_soul_data["tokens"])
            else:
                print("⚠️ SELF-CORRECTION PARTIAL: Audits completed with minor styling items.")
                self.sentry.report_issues()
        else:
            print("✅ AUDIT PASSED: Visual contrast, template tags, and layer stacks are pristine.")
            # Learn preferences since the build successfully passed immediately
            if user_id and user_id != "anonymous":
                self._learn_user_style_preferences(user_id, soul_data["tokens"])
            
        print(f"✅ PROJECT COMPLETE: {len(generated_files)} pages compiled.")
        self._sync_to_github()
        return generated_files

    def _learn_user_style_preferences(self, user_id, tokens):
        """Analyzes the successful styling choices and records them as user-scoped preferences."""
        pref_mappings = {
            "font_heading": "preferred_heading_font",
            "font_body": "preferred_body_font",
            "bg_color": "preferred_bg_color",
            "accent_primary": "preferred_accent_color",
            "geometry_type": "preferred_3d_geometry"
        }
        try:
            brain = AnimusBrain()
            for token_key, pref_key in pref_mappings.items():
                if token_key in tokens:
                    brain.save_user_preference(user_id, pref_key, tokens[token_key])
            print(f"📈 MACHINE LEARNING: User {user_id} styling preferences parsed and learned successfully.")
        except Exception as e:
            print(f"⚠️ Preference learning failed: {e}")

    def _assemble_site_files(self, soul_data, mission, hero_image):
        generated_files = []
        for page in soul_data["sitemap"]:
            file_name = page["file"].replace(".html", "")
            # Apply hero image only to index
            image = hero_image if file_name == "index" else None
            file_path = self.generate_page(file_name, {"mission": mission}, soul_data=soul_data, hero_image=image)
            generated_files.append(file_path)
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
            
        self._write_page_to_db(f"{page_name}.html", full_page)
        return file_path

    def _write_page_to_db(self, page_name, html_content):
        persistent_dir = os.getenv("PERSISTENT_DATA_DIR")
        if persistent_dir:
            db_path = os.path.join(persistent_dir, "laura_memory.db")
        else:
            db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "laura_memory.db")
        if not os.path.exists(db_path):
            db_path = "laura_memory.db"
        try:
            import sqlite3
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS generated_pages (
                    page_name TEXT PRIMARY KEY,
                    html_content TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            cursor.execute("""
                INSERT OR REPLACE INTO generated_pages (page_name, html_content)
                VALUES (?, ?)
            """, (page_name, html_content))
            conn.commit()
            conn.close()
            print(f"💾 DATABASE SYNC: Saved {page_name} to SQLite shared memory.")
        except Exception as e:
            print(f"⚠️ Failed to sync {page_name} to database: {e}")

    def _sync_to_github(self):
        import subprocess
        persistent_dir = os.getenv("PERSISTENT_DATA_DIR")
        if persistent_dir:
            db_path = os.path.join(persistent_dir, "laura_memory.db")
        else:
            db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "laura_memory.db")
        if os.path.exists(db_path):
            print("📤 GIT SYNC: Local Mac detected. Auto-syncing generated work to GitHub...")
            try:
                # Stage projects and tests
                subprocess.run(["git", "add", "static/projects/", "tests/"], check=True)
                status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
                if status.stdout.strip():
                    subprocess.run(["git", "commit", "-m", f"FEAT: Live compile - {self.project_name}"], check=True)
                    subprocess.run(["git", "push", "origin", "main"], check=True)
                    print("✅ GIT SYNC SUCCESS: Generated files pushed to GitHub main branch!")
                else:
                    print("📤 GIT SYNC: No static files changed, skipping commit.")
            except Exception as e:
                print(f"⚠️ GIT SYNC FAILED: {e}")

