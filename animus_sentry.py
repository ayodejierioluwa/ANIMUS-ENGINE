import os
import re

class AnimusSentry:
    """
    The 'Quality Sentinel' of the Animus Engine.
    Audits generated files for visual overlaps, content redundancy, and UX failures.
    """
    def __init__(self):
        self.issues = []

    def audit_project(self, generated_files):
        """
        Audits an entire project for cross-page consistency and content unique-ness.
        """
        self.issues = []
        contents = {}
        
        for file_path in generated_files:
            with open(file_path, "r") as f:
                html = f.read()
                # Extract the main content features to check for clones
                features = re.findall(r'<h3.*?>(.*?)</h3>', html)
                contents[file_path] = features
                
                # Audit individual file
                self.audit_file(file_path, html)

        # Content Redundancy Audit
        file_paths = list(contents.keys())
        for i in range(len(file_paths)):
            for j in range(i + 1, len(file_paths)):
                if contents[file_paths[i]] == contents[file_paths[j]] and len(contents[file_paths[i]]) > 0:
                    self.issues.append(f"CRITICAL: Content Redundancy detected between {file_paths[i]} and {file_paths[j]}. Pages are clones.")

        return len(self.issues) == 0

    def audit_file(self, file_path, html=None):
        if html is None:
            with open(file_path, "r") as f:
                html = f.read()

        # Visual Overlap Audit
        if 'z-index: -100' in html and 'background: transparent' not in html:
            self.issues.append(f"Visual Error in {file_path}: Background is opaque, hiding the shader layer.")

        # Nav Active State Audit
        if 'class="nav-item active"' not in html:
            self.issues.append(f"UX Error in {file_path}: No active navigation state detected.")

        return len(self.issues) == 0

    def report_issues(self):
        for issue in self.issues:
            print(f"🚨 SENTRY ALERT: {issue}")
