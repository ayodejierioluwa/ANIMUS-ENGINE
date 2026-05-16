from animus_engine import AnimusEngine

def run_hyper_drive_test():
    output_dir = "tests/test_hyper_drive"
    engine = AnimusEngine(output_dir=output_dir)
    
    data = {
        "project_name": "HYPER_DRIVE",
        "pages": [
            {
                "name": "index",
                "content": {
                    "theme": "DYNAMIC",
                    "use_video": True,
                    "video_url": "https://archive.org/download/Fireplace_201602/Fireplace.mp4",
                    "hero_title": "WOOD BURNING",
                    "hero_subtitle": "Testing the realistic fire textures for production.",
                    "features": [
                        {"title": "Realism", "content": "Sharp wood burning textures."},
                        {"title": "Direct Stream", "content": "Zero YouTube UI artifacts."}
                    ]
                }
            },
            {
                "name": "flavors",
                "content": {
                    "theme": "DYNAMIC",
                    "use_shader": True,
                    "hero_title": "ABSTRACT LIQUID",
                    "hero_subtitle": "Testing the code-based generative fire shader.",
                    "features": [
                        {"title": "Indestructible", "content": "100% reliable GPU simulation."},
                        {"title": "Interactive", "content": "Flows with your motion."}
                    ]
                }
            },
            {
                "name": "metrics",
                "content": {
                    "theme": "DYNAMIC",
                    "layout": "SPLIT",
                    "geometry": "RING",
                    "hero_title": "BIO-METRIC SYNC",
                    "hero_subtitle": "Track your performance in real-time with the Hyper-Drive app.",
                    "features": [
                        {"title": "Heart Rate", "content": "Optimized cardiovascular monitoring."},
                        {"title": "ATP Tracking", "content": "Measure your cellular energy levels."}
                    ]
                }
            }
        ]
    }
    
    print("--- Running Generic Test: Hyper Drive ---")
    print(engine.generate_site(data))
    print(f"View at: {output_dir}/index.html\n")

if __name__ == "__main__":
    run_hyper_drive_test()
