from animus_engine import AnimusEngine

def run_test(prompt_id, data):
    output_dir = f"tests/test_{prompt_id}"
    engine = AnimusEngine(output_dir=output_dir)
    print(f"--- Running Test: {prompt_id} ---")
    print(engine.generate_site(data))
    print(f"View at: {output_dir}/index.html\n")

# Prompt 1: Futuristic Crypto Exchange
run_test("crypto", {
    "project_name": "NEON_DEX",
    "hero_title": "THE FUTURE OF LIQUIDITY",
    "hero_subtitle": "Hyper-fast, decentralized, and entirely interactive trading experience.",
    "use_3d": True,
    "features": [
        {"title": "Zero Latency", "content": "Trade at the speed of light with our optimized engine."},
        {"title": "Multi-Chain", "content": "Connect to any chain seamlessly with a single click."}
    ]
})

# Prompt 2: Minimalist Architecture Portfolio
run_test("architecture", {
    "project_name": "STRUCT_STUDIO",
    "hero_title": "SILENCE IN STRUCTURE",
    "hero_subtitle": "Designing the spaces that define tomorrow's skyline.",
    "use_3d": True,
    "features": [
        {"title": "Organic Flow", "content": "Buildings that breathe and evolve with their environment."},
        {"title": "Sustainable Future", "content": "Zero-emission materials for a greener world."}
    ]
})

# Prompt 3: Cyberpunk Fashion Brand
run_test("fashion", {
    "project_name": "VOID_WEAR",
    "hero_title": "STYLE FROM THE ABYSS",
    "hero_subtitle": "Wearable tech that pushes the boundaries of human expression.",
    "use_3d": True,
    "features": [
        {"title": "Neural Link", "content": "Sync your style with your subconscious mind."},
        {"title": "AR Overlay", "content": "Real-time aesthetic shifts powered by augmented reality."}
    ]
})
