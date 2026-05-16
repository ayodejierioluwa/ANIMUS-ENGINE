from animus_engine import AnimusEngine
import os

def test_hyper_drive():
    print("--- Running Animus Soul + Grid Interaction Test ---")
    engine = AnimusEngine(output_dir="tests/test_hyper_drive")
    
    # Page 1: Crypto Project (The 'Soul' should generate Neural Wealth)
    engine.generate_page("index", {
        "mission": "A high-fidelity cryptocurrency trading platform with neural intelligence",
        "theme": "DYNAMIC",
        "hero_title": "Crypto Future",
        "use_3d": True
    })
    
    # Page 2: Design Studio (The 'Soul' should generate Beyond Code)
    engine.generate_page("flavors", {
        "mission": "A luxury design studio for high-end digital experiences",
        "theme": "DYNAMIC",
        "use_shader": True
    })
    
    print(f"Successfully generated interactive pages in tests/test_hyper_drive/")

if __name__ == "__main__":
    test_hyper_drive()
