from animus_engine import AnimusEngine

def run_multi_page_test():
    output_dir = "tests/test_nature_tech"
    engine = AnimusEngine(output_dir=output_dir)
    
    data = {
        "project_name": "GEO_SYNC",
        "pages": [
            {
                "name": "index",
                "content": {
                    "theme": "DARK_NEON",
                    "use_video": True,
                    "hero_title": "NATURE SYNCED",
                    "hero_subtitle": "Reconnecting humanity with the biosphere through autonomous technology.",
                    "video_url": "https://assets.mixkit.co/videos/preview/mixkit-stars-in-the-night-sky-flowing-slowly-3665-large.mp4",
                    "features": [
                        {"title": "Organic Intelligence", "content": "AI trained on biological ecosystems."},
                        {"title": "Global Mesh", "content": "Real-time planetary monitoring."}
                    ]
                }
            },
            {
                "name": "about",
                "content": {
                    "theme": "MINIMAL_LIGHT",
                    "layout": "SPLIT",
                    "geometry": "PLANE",
                    "hero_title": "OUR ROOTS",
                    "hero_subtitle": "Founded in the heart of the Amazon, built for the global stage.",
                    "features": [
                        {"title": "Transparency", "content": "Open-source conservation data."},
                        {"title": "Impact", "content": "100% of proceeds go to reforestation."}
                    ]
                }
            },
            {
                "name": "contact",
                "content": {
                    "theme": "LUXURY_GOLD",
                    "use_3d": True,
                    "geometry": "TORUS",
                    "hero_title": "JOIN THE SYNC",
                    "hero_subtitle": "Reach out to start your journey into the new ecological frontier.",
                    "features": [
                        {"title": "Discord", "content": "Join our 24/7 community hub."},
                        {"title": "Headquarters", "content": "Visit us in Oslo, Norway."}
                    ]
                }
            }
        ]
    }
    
    print("--- Running Multi-Page Test: Nature Tech ---")
    print(engine.generate_site(data))
    print(f"View at: {output_dir}/index.html\n")

if __name__ == "__main__":
    run_multi_page_test()
