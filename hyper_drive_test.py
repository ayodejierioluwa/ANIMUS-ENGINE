from animus_engine import AnimusEngine
from animus_sentry import AnimusSentry
import os

def test_neural_project():
    print("--- Running Animus Deep Intelligence Test ---")
    engine = AnimusEngine(output_dir="tests/test_hyper_drive")
    sentry = AnimusSentry()
    
    # 1. Generate full 'Surgical Tech' Project
    generated_files = engine.generate_project("A surgical neural-bridge for high-frequency crypto trading")
    
    # 2. Sentry Audit
    print("🕵️ Sentry performing deep project audit...")
    if not sentry.audit_project(generated_files):
        sentry.report_issues()
        print("❌ Project Audit FAILED.")
    else:
        print("✅ Project Audit PASSED: All pages are unique and UX-compliant.")

    print(f"Project can be viewed in tests/test_hyper_drive/")

if __name__ == "__main__":
    test_neural_project()
