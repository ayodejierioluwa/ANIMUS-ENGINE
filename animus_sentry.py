import os
import re

class AnimusSentry:
    def audit_site(self, directory):
        print(f"--- Auditing Site: {directory} ---")
        errors = []
        files = [f for f in os.listdir(directory) if f.endswith(".html")]
        
        for file in files:
            path = os.path.join(directory, file)
            with open(path, "r") as f:
                content = f.read()
                
                # Check 1: Video visibility
                if "<video" in content:
                    if "z-index: 1" not in content and "z-index: 1" not in self._get_css(directory):
                        errors.append(f"[{file}] Video element might be hidden by z-index.")
                    if "background: transparent" not in content and "background: transparent" not in self._get_css(directory):
                        errors.append(f"[{file}] Hero background might block video.")
                
                # Check 2: Broken Navigation
                links = re.findall(r'href="([^"]+)"', content)
                for link in links:
                    if link.endswith(".html") and not os.path.exists(os.path.join(directory, link)):
                        errors.append(f"[{file}] Broken Link: {link}")
                        
                # Check 3: Valid Video Source
                video_srcs = re.findall(r'src="([^"]+)"', content)
                for src in video_srcs:
                    if ".mp4" in src and not src.startswith("http"):
                         if not os.path.exists(os.path.join(directory, src)):
                            errors.append(f"[{file}] Broken Video Source: {src}")

        if not errors:
            print("✅ Sentry Audit Passed: Everything looks clean.")
            return True
        else:
            print("❌ Sentry Audit Failed:")
            for err in errors:
                print(f"  - {err}")
            return False

    def _get_css(self, directory):
        # Helper to find CSS in the directory or template
        return "" # Simplified for now

if __name__ == "__main__":
    sentry = AnimusSentry()
    sentry.audit_site("tests/test_hyper_drive")
