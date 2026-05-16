from animus_engine import AnimusEngine
import os

def test_hyper_drive():
    print("--- Running Animus Vibe Shift Engine Test ---")
    engine = AnimusEngine(output_dir="tests/test_hyper_drive")
    
    # Page 1: Surgical Crypto (Neural/Tech Vibe)
    # Expected: Sharp corners, low blur, high precision.
    engine.generate_page("index", {
        "mission": "A surgical neural-bridge for high-frequency crypto trading",
        "theme": "DYNAMIC"
    })
    
    # Page 2: Organic Wellness (Soft Vibe)
    # Expected: Ultra-round corners, deep blur, organic fades.
    engine.generate_page("wellness", {
        "mission": "An organic wellness sanctuary for holistic nature meditation",
        "theme": "DYNAMIC"
    })
    
    # Page 3: Standard Modern (The Baseline)
    engine.generate_page("flavors", {
        "mission": "A high-end digital design studio",
        "theme": "DYNAMIC"
    })
    
    print(f"Successfully generated Vibe Shifted pages in tests/test_hyper_drive/")

if __name__ == "__main__":
    test_hyper_drive()
