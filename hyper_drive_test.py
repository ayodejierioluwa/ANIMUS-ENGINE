from animus_engine import AnimusEngine
from animus_sentry import AnimusSentry
import os

def test_minds_eye_project():
    print("--- Running Animus Mind's Eye Test ---")
    engine = AnimusEngine(output_dir="tests/test_hyper_drive")
    sentry = AnimusSentry()
    
    # The Mind's Eye Visual (Generated in previous step)
    hero_img = "/Users/macbook/.gemini/antigravity/brain/010e3ac2-392d-469e-af4e-19c079b21dff/neural_core_hero_vison_1778955942947.png"
    
    # 1. Generate full 'Surgical Tech' Project with the Mind's Eye
    generated_files = engine.generate_project(
        "A surgical neural-bridge for high-frequency crypto trading",
        hero_image=hero_img
    )
    
    # 2. Sentry Audit
    print("🕵️ Sentry performing deep project audit...")
    if not sentry.audit_project(generated_files):
        sentry.report_issues()
        print("❌ Project Audit FAILED.")
    else:
        print("✅ Project Audit PASSED: All pages are unique, visual, and tactile.")

    print(f"Project can be viewed in tests/test_hyper_drive/")

if __name__ == "__main__":
    test_minds_eye_project()
