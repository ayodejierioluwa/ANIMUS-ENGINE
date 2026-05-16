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
                    "layout": "FULL",
                    "geometry": "OCTA",
                    "hero_title": "FUEL YOUR FIRE",
                    "hero_subtitle": "The world's first bio-kinetic energy drink powered by AI-optimized nutrients.",
                    "use_3d": True,
                    "features": [
                        {"title": "Zero Crash", "content": "Steady energy for 12 hours straight."},
                        {"title": "Neural Focus", "content": "Boost your cognitive performance by 40%."}
                    ]
                }
            },
            {
                "name": "flavors",
                "content": {
                    "theme": "DYNAMIC",
                    "use_video": True,
                    "hero_title": "EXPLOSIVE TASTE",
                    "hero_subtitle": "From Electric Mango to Midnight Berries. Find your flow.",
                    "youtube_id": "Lp6WjSTU80M",
                    "features": [
                        {"title": "Electric Mango", "content": "A surge of tropical intensity."},
                        {"title": "Midnight Berry", "content": "Smooth, dark, and powerful."}
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
