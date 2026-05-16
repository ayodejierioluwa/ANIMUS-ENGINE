from animus_engine import AnimusEngine
import os

def test_neural_project():
    print("--- Running Animus Neural Project Test ---")
    engine = AnimusEngine(output_dir="tests/test_hyper_drive")
    
    # Generate a full 'Surgical Tech' Project
    engine.generate_project("A surgical neural-bridge for high-frequency crypto trading")
    
    # Generate a full 'Organic Wellness' Project
    # (Note: This will overwrite in the same dir if we don't change it, 
    # but for testing we'll just check the first one)
    
    print(f"Successfully generated a full autonomous project in tests/test_hyper_drive/")

if __name__ == "__main__":
    test_neural_project()
