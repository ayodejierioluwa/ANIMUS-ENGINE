# AETHER_ANIMUS Component Library

NAV_BAR_TEMPLATE = """
<nav style="position: fixed; top: 2rem; left: 50%; transform: translateX(-50%); width: auto; min-width: 400px; z-index: 10000; background: var(--glass-bg); border: 1px solid var(--glass-border); backdrop-filter: blur(var(--glass-blur)); border-radius: 100px; padding: 0.75rem 2rem; display: flex; align-items: center; justify-content: space-between; gap: 3rem; transition: all 0.5s var(--ease-vibe);">
    <div class="logo" style="font-family: var(--font-heading); font-weight: 700; letter-spacing: 0.1em; font-size: 0.9rem; color: var(--accent-primary);">[[project_name]]</div>
    <div class="nav-links" style="display: flex; gap: 2rem; align-items: center;">
        [[nav_links]]
    </div>
    <div class="nav-cta">
        <a href="#" style="background: white; color: black; padding: 0.5rem 1.5rem; border-radius: 50px; text-decoration: none; font-size: 0.8rem; font-weight: 700; letter-spacing: 0.05em; transition: transform 0.3s var(--ease-vibe); display: inline-block;">[[cta_text]]</a>
    </div>
</nav>
<style>
    .nav-cta a:hover { transform: scale(1.05); box-shadow: 0 10px 20px rgba(0,0,0,0.3); }
</style>
"""

NAV_LINK_TEMPLATE = """
<a href="[[link]]" class="nav-item [[active_class]]" style="text-decoration: none; color: white; font-size: 0.8rem; font-weight: 400; letter-spacing: 0.05em; transition: all 0.3s var(--ease-vibe); font-family: var(--font-body); position: relative; padding: 0.5rem 0;">
    [[name]]
    <div class="active-indicator" style="position: absolute; bottom: 0; left: 0; width: 100%; height: 2px; background: white; transition: transform 0.3s var(--ease-vibe); border-radius: 2px; transform: scaleX(0); transform-origin: left;"></div>
</a>
<style>
    .nav-item { opacity: 0.5; }
    .nav-item:hover { opacity: 1; }
    .nav-item.active { opacity: 1; font-weight: 700; }
    .nav-item.active .active-indicator { transform: scaleX(1) !important; }
</style>
"""

HERO_TEMPLATE = """
<section class="hero" id="hero">
    <div class="mesh-gradient"></div>
    <div class="hero-content">
        <h1 class="reveal">{title}</h1>
        <p class="reveal">{subtitle}</p>
        <div class="reveal">
            <a href="{cta_link}" class="btn-primary">{cta_text}</a>
        </div>
    </div>
</section>
"""

IMAGE_HERO_TEMPLATE = """
<section class="hero [[layout_class]]" id="hero" style="background: url('[[image_url]]') center/cover no-repeat !important; min-height: 100vh; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(0,0,0,0.8), var(--bg-color));"></div>
    <div id="void-canvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0.2; mix-blend-mode: screen;"></div>
    <div class="hero-content" style="position: relative; z-index: 10; text-align: center;">
        <h1 class="reveal" style="font-size: clamp(3rem, 10vw, 6rem); letter-spacing: -0.04em; line-height: 0.95; font-weight: 700;">[[title]]</h1>
        <p class="reveal" style="font-size: 1.25rem; opacity: 0.6; margin-top: 2rem; max-width: 650px; margin-left: auto; margin-right: auto; line-height: 1.6; font-weight: 300;">[[subtitle]]</p>
        <div class="reveal" style="margin-top: 4rem;">
            <a href="[[cta_link]]" class="btn-primary" style="padding: 1.25rem 3.5rem; font-size: 1rem; border-radius: var(--btn-radius); background: white; color: black; text-decoration: none; font-weight: 700; letter-spacing: 0.1em; transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); box-shadow: 0 20px 40px rgba(0,0,0,0.4);">[[cta_text]]</a>
        </div>
    </div>
</section>
"""

VIDEO_HERO_TEMPLATE = """
<section class="hero [[layout_class]]" id="hero" style="background: var(--bg-color) !important; min-height: 100vh; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
    <div id="void-canvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0.3; filter: blur(var(--void-blur));"></div>
    <div class="hero-content" style="position: relative; z-index: 10; text-align: center;">
        <h1 class="reveal" style="font-size: clamp(3rem, 10vw, 6rem); letter-spacing: -0.04em; line-height: 0.95; font-weight: 700;">[[title]]</h1>
        <p class="reveal" style="font-size: 1.25rem; opacity: 0.6; margin-top: 2rem; max-width: 650px; margin-left: auto; margin-right: auto; line-height: 1.6; font-weight: 300;">[[subtitle]]</p>
        <div class="reveal" style="margin-top: 4rem;">
            <a href="[[cta_link]]" class="btn-primary" style="padding: 1.25rem 3.5rem; font-size: 1rem; border-radius: var(--btn-radius); background: white; color: black; text-decoration: none; font-weight: 700; letter-spacing: 0.1em; transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); box-shadow: 0 20px 40px rgba(0,0,0,0.4);">[[cta_text]]</a>
        </div>
    </div>
</section>
"""

FEATURE_GRID_TEMPLATE = """
<section class="features" style="padding: 12rem 2rem; background: var(--bg-color); position: relative;">
    <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 100%; height: 1px; background: linear-gradient(90deg, transparent, var(--glass-border), transparent);"></div>
    <div class="container" style="max-width: 1300px; margin: 0 auto;">
        <div class="grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 3rem;">
            [[features]]
        </div>
    </div>
</section>
"""

FEATURE_ITEM_TEMPLATE = """
<div class="feature-item" style="background: var(--glass-bg); border: 1px solid var(--glass-border); padding: 4rem; border-radius: var(--grid-radius); backdrop-filter: blur(var(--glass-blur)); transition: all 0.5s cubic-bezier(0.2, 0.8, 0.2, 1); position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, transparent 100%); pointer-events: none;"></div>
    <div class="icon" style="font-size: 2.5rem; margin-bottom: 2rem; filter: drop-shadow(0 0 15px var(--accent-primary));">[[icon]]</div>
    <h3 style="font-size: 1.75rem; margin-bottom: 1.5rem; color: white; font-weight: 600; letter-spacing: -0.02em;">[[title]]</h3>
    <p style="opacity: 0.5; line-height: 1.8; font-size: 1.05rem; font-weight: 300;">[[description]]</p>
</div>
<style>
    .feature-item:hover {
        transform: translateY(-15px) scale(1.02);
        border-color: var(--accent-primary);
        background: rgba(255,255,255,0.06);
        box-shadow: 0 30px 60px rgba(0,0,0,0.5);
    }
    .btn-primary:hover {
        transform: scale(1.05);
        box-shadow: 0 0 30px var(--accent-primary);
    }
</style>
"""

SHADER_HERO_TEMPLATE = """
<div id="shader-background-container" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -100; pointer-events: none;"></div>
<section class="hero [[layout_class]]" id="hero" style="background: transparent !important;">
    <div class="noise-overlay"></div>
    <div class="hero-content">
        <h1 class="reveal">[[title]]</h1>
        <p class="reveal">[[subtitle]]</p>
        <div class="reveal">
            <a href="[[cta_link]]" class="btn-primary">[[cta_text]]</a>
        </div>
    </div>
</section>
<button onclick="diagnoseVisuals()" style="position: fixed; bottom: 1rem; right: 1rem; z-index: 10002; background: rgba(255,255,255,0.1); color: white; border: 1px solid white; padding: 0.5rem; border-radius: 5px; cursor: pointer;">Diagnostic</button>
"""

SCROLL_SECTION_TEMPLATE = """
<div class="noise-overlay"></div>
<section class="grid">
    {cards}
</section>
"""

CARD_TEMPLATE = """
<div class="card glass reveal">
    <h3>{title}</h3>
    <p>{content}</p>
</div>
"""

THREE_JS_HERO_TEMPLATE = """
<section class="hero [[layout_class]]" id="hero">
    <div id="three-canvas-container"></div>
    <div class="hero-content">
        <h1 class="reveal">[[title]]</h1>
        <p class="reveal">[[subtitle]]</p>
        <div class="reveal">
            <a href="[[cta_link]]" class="btn-primary">[[cta_text]]</a>
        </div>
    </div>
</section>
"""

SPLIT_HERO_TEMPLATE = """
<section class="hero split-layout" id="hero">
    <div class="hero-left">
        <h1 class="reveal">[[title]]</h1>
        <p class="reveal">[[subtitle]]</p>
        <div class="reveal">
            <a href="[[cta_link]]" class="btn-primary">[[cta_text]]</a>
        </div>
    </div>
    <div class="hero-right">
        <div id="three-canvas-container"></div>
    </div>
</section>
"""

SENTRY_REPORT_TEMPLATE = """
<div id="sentry-report" style="position: fixed; bottom: 2rem; left: 2rem; z-index: 10005; background: rgba(0,255,204,0.1); border: 1px solid rgba(0,255,204,0.3); padding: 1rem 1.5rem; border-radius: 12px; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 1rem; cursor: pointer; transition: all 0.3s var(--ease-vibe);">
    <div style="width: 8px; height: 8px; background: #00ffcc; border-radius: 50%; box-shadow: 0 0 10px #00ffcc;"></div>
    <div style="font-family: 'Space Mono', monospace; font-size: 0.7rem; color: #00ffcc; letter-spacing: 0.1em;">SENTRY_AUDIT: [[sentry_status]]</div>
</div>
"""

FOOTER_TEMPLATE = """
<footer style="padding: 4rem 2rem; text-align: center; color: rgba(255,255,255,0.4); border-top: 1px solid var(--glass-border);">
    <p>&copy; 2026 AETHER_ANIMUS | Built for {project_name}</p>
</footer>
"""

GSAP_SCRIPT = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/0.160.0/three.min.js"></script>

<script>
    gsap.registerPlugin(ScrollTrigger);

    // Three.js Scene Setup
    const container = document.getElementById('three-canvas-container');
    if (container) {
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        renderer.setSize(container.clientWidth, container.clientHeight);
        container.appendChild(renderer.domElement);

        // Dynamic Geometry Selection (WOW Factor)
        const geometries = {
            "SPHERE": new THREE.IcosahedronGeometry(2, 1),
            "TORUS": new THREE.TorusKnotGeometry(1.5, 0.4, 100, 16),
            "PLANE": new THREE.PlaneGeometry(5, 5, 32, 32),
            "OCTA": new THREE.OctahedronGeometry(2, 0),
            "RING": new THREE.TorusGeometry(2, 0.5, 16, 100)
        };
        const geoType = "[[geometry_type]]";
        const geometry = geometries[geoType] || geometries["SPHERE"];
        
        const material = new THREE.MeshPhongMaterial({
            color: "[[accent_primary_hex]]",
            wireframe: true,
            transparent: true,
            opacity: 0.9,
            emissive: "[[accent_primary_hex]]",
            emissiveIntensity: 0.6
        });
        const sphere = new THREE.Mesh(geometry, material);
        scene.add(sphere);

        const light = new THREE.PointLight(0xffffff, 4, 100);
        light.position.set(10, 10, 10);
        scene.add(light);
        scene.add(new THREE.AmbientLight(0xffffff, 1.2));

        camera.position.z = 5;

        function animate() {
            requestAnimationFrame(animate);
            sphere.rotation.x += 0.005;
            sphere.rotation.y += 0.005;
            renderer.render(scene, camera);
        }
        animate();

        // Mouse Interactivity for Three.js
        window.addEventListener('mousemove', (e) => {
            const x = (e.clientX / window.innerWidth - 0.5) * 2;
            const y = (e.clientY / window.innerHeight - 0.5) * 2;
            gsap.to(sphere.rotation, { y: x, x: -y, duration: 2 });
        });

        // Scroll Parallax for Three.js
        gsap.to(sphere.position, {
            scrollTrigger: {
                trigger: "body",
                start: "top top",
                end: "bottom bottom",
                scrub: 1
            },
            z: -5,
            y: 2
        });
    }

    // Minimal aesthetic movement for the 'Void' background
    const voidCont = document.getElementById('void-canvas');
    if (voidCont) {
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        voidCont.appendChild(canvas);
        function resize() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resize);
        resize();
        function animate() {
            ctx.clearRect(0,0,canvas.width, canvas.height);
            ctx.fillStyle = 'rgba(255,255,255,0.05)';
            for(let i=0; i<40; i++) {
                ctx.beginPath();
                ctx.arc(Math.sin(Date.now()*0.0002 + i)*canvas.width, Math.cos(Date.now()*0.0001 + i)*canvas.height, 1, 0, Math.PI*2);
                ctx.fill();
            }
            requestAnimationFrame(animate);
        }
        animate();
    }

    // Liquid Fire Shader (DEPRECATED - MOVED TO GENERIC SHADER)

    // AETHER_IGNIS_ULTIMA (The Mesmerising Realistic Fix)
    const realisticFire = document.getElementById('realistic-fire-container');
    if (realisticFire) {
        const rf_scene = new THREE.Scene();
        const rf_camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
        const rf_renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        rf_renderer.setPixelRatio(window.devicePixelRatio);
        rf_renderer.setSize(window.innerWidth, window.innerHeight);
        realisticFire.appendChild(rf_renderer.domElement);

        const rf_material = new THREE.ShaderMaterial({
            uniforms: { 
                time: { value: 1.0 }, 
                resolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) },
                mouse: { value: new THREE.Vector2(0.5, 0.5) }
            },
            vertexShader: `void main() { gl_Position = vec4(position, 1.0); }`,
            fragmentShader: `
                uniform float time;
                uniform vec2 resolution;
                uniform vec2 mouse;
                
                vec3 firePalette(float t) {
                    vec3 a = vec3(0.5, 0.5, 0.5);
                    vec3 b = vec3(0.5, 0.5, 0.5);
                    vec3 c = vec3(1.0, 1.0, 1.0);
                    vec3 d = vec3(0.00, 0.10, 0.20);
                    return a + b * cos(6.28318 * (c * t + d));
                }

                float hash(vec2 p) { return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453); }
                float noise(vec2 p) {
                    vec2 i = floor(p); vec2 f = fract(p);
                    vec2 u = f*f*(3.0-2.0*f);
                    return mix(mix(hash(i + vec2(0.,0.)), hash(i + vec2(1.,0.)), u.x),
                               mix(hash(i + vec2(0.,1.)), hash(i + vec2(1.,1.)), u.x), u.y);
                }

                void main() {
                    vec2 uv = gl_FragCoord.xy / resolution.xy;
                    vec2 q = uv;
                    q.y -= time * 0.6; // Faster, more energetic
                    
                    float T3 = 1.6 * noise(q * 3.0);
                    float T2 = 1.2 * noise(q * 6.0 + T3);
                    float T1 = 0.8 * noise(q * 12.0 + T2);
                    float f = T1 + T2 + T3;
                    
                    f *= (1.0 - uv.y) * 3.0; // Sharper taper
                    f = clamp(f, 0.0, 1.0);
                    
                    // RAZOR SHARP STEPS (No more blur)
                    vec3 fireColor = mix(vec3(0.0), vec3(1.0, 0.2, 0.0), smoothstep(0.2, 0.25, f));
                    fireColor = mix(fireColor, vec3(1.0, 0.6, 0.0), smoothstep(0.4, 0.45, f));
                    fireColor = mix(fireColor, vec3(1.0, 1.0, 0.5), smoothstep(0.7, 0.72, f));
                    
                    // High Contrast Bloom
                    fireColor *= 1.5;
                    
                    // Mouse Distortion (Crystal Clear)
                    float dist = distance(uv, mouse);
                    if (dist < 0.2) {
                        fireColor *= 1.2;
                    }
                    
                    gl_FragColor = vec4(fireColor, 1.0);
                }
            `
        });
        rf_scene.add(new THREE.Mesh(new THREE.PlaneGeometry(2, 2), rf_material));
        
        window.addEventListener('mousemove', (e) => {
            rf_material.uniforms.mouse.value.x = e.clientX / window.innerWidth;
            rf_material.uniforms.mouse.value.y = 1.0 - (e.clientY / window.innerHeight);
        });

        function rf_animate(t) {
            requestAnimationFrame(rf_animate);
            rf_material.uniforms.time.value = t * 0.001;
            rf_renderer.render(rf_scene, rf_camera);
        }
        rf_animate(0);
        window.addEventListener('resize', () => {
            rf_renderer.setSize(window.innerWidth, window.innerHeight);
            rf_material.uniforms.resolution.value.set(window.innerWidth, window.innerHeight);
        });
    }

    // Indestructible Visual Fix Diagnostic
    function diagnoseVisuals() {
        const grid = document.querySelector('.features');
        if (grid) {
            alert(`Animus Diagnostic:\\n- Grid Active: ${grid.offsetWidth}x${grid.offsetHeight}\\n- Soul Identity: Active`);
        }
    }

    // Magnetic Cursor Logic (WOW Factor)
    const cursor = document.createElement('div');
    cursor.className = 'custom-cursor';
    document.body.appendChild(cursor);

    window.addEventListener('mousemove', (e) => {
        gsap.to(cursor, {
            x: e.clientX,
            y: e.clientY,
            duration: 0.6,
            ease: "power2.out"
        });
    });

    document.querySelectorAll('.btn-primary, .card').forEach(el => {
        el.addEventListener('mouseenter', () => gsap.to(cursor, { scale: 3, backgroundColor: "var(--accent-primary)", opacity: 0.3 }));
        el.addEventListener('mouseleave', () => gsap.to(cursor, { scale: 1, backgroundColor: "transparent", opacity: 1 }));
    });

    function diagnoseVisuals() {
        const video = document.getElementById('bg-video');
        const shader = document.getElementById('shader-background-container');
        const realistic = document.getElementById('realistic-fire-container');
        if (realistic) {
            alert(`Sentry Diagnostic:\\n- Realistic Shader Active: ${realistic.offsetWidth}x${realistic.offsetHeight}\\n- Z-Index: ${realistic.style.zIndex}`);
        } else if (shader) {
            alert(`Sentry Diagnostic:\\n- Abstract Shader Active: ${shader.offsetWidth}x${shader.offsetHeight}\\n- Z-Index: ${shader.style.zIndex}`);
        } else {
            alert("Sentry Diagnostic: NO BACKGROUND ELEMENT FOUND.");
        }
    }
</script>
"""

BASE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[[title]]</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Outfit:wght@200;400;700&family=Space+Mono&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: [[bg_color]];
            --text-color: [[text_color]];
            --accent-primary: [[accent_primary]];
            --glass-bg: rgba(255, 255, 255, 0.03);
            --glass-border: rgba(255, 255, 255, 0.1);
            
            /* Vibe Shift Tokens */
            --glass-blur: [[glass_blur]];
            --grid-radius: [[grid_radius]];
            --btn-radius: [[btn_radius]];
            --void-blur: [[void_blur]];
            
            /* Atmospheric DNA */
            --font-heading: [[font_heading]];
            --font-body: [[font_body]];
            --ease-vibe: [[ease_vibe]];
            --duration-vibe: [[duration_vibe]];
            --hover-glow: [[hover_glow]];
            --breathing-anim: [[breathing_anim]];
            --breathing-anim-hover: [[breathing_anim_hover]];
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            background-color: var(--bg-color); 
            color: var(--text-color); 
            font-family: var(--font-body), sans-serif;
            overflow-x: hidden;
            transition: background 1s ease;
        }
        h1, h2, h3 { 
            font-family: var(--font-heading), sans-serif; 
            letter-spacing: [[letter_spacing]];
            text-transform: [[text_transform]];
        }
        .site-wrapper { position: relative; z-index: 10; }
        
        .feature-item {
            transition: all var(--duration-vibe) var(--ease-vibe) !important;
            animation: var(--breathing-anim) 8s ease-in-out infinite;
        }
        .feature-item:hover {
            box-shadow: var(--hover-glow) !important;
            animation: var(--breathing-anim-hover) 4s ease-in-out infinite;
        }
        .btn-primary {
            transition: all 0.3s var(--ease-vibe) !important;
        }

        /* Tactical Layer: Surgical SVG Grain */
        .film-grain {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 99999;
            opacity: 0.25;
            filter: url(#grainy);
        }
        .ambient-vignette {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 99998;
            background: radial-gradient(circle, transparent 20%, rgba(0,0,0,0.6) 100%);
        }
        .ambient-vignette {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 99998;
            background: radial-gradient(circle, transparent 20%, rgba(0,0,0,0.4) 100%);
        }
        @keyframes grain {
            0%, 100% { transform: translate(0, 0); }
            10% { transform: translate(-5%, -10%); }
            20% { transform: translate(-15%, 5%); }
            30% { transform: translate(7%, -25%); }
            40% { transform: translate(-5%, 25%); }
            50% { transform: translate(-15%, 10%); }
            60% { transform: translate(15%, 0%); }
            70% { transform: translate(0%, 15%); }
            80% { transform: translate(3%, 35%); }
            90% { transform: translate(-10%, 10%); }
        }

        @keyframes aether-breath {
            0%, 100% { transform: translateY(0) scale(1); }
            50% { transform: translateY(-10px) scale(1.01); }
        }
        @keyframes aether-breath-deep {
            0%, 100% { transform: translateY(-15px) scale(1.02); }
            50% { transform: translateY(-25px) scale(1.03); }
        }
    </style>
</head>
<body>
    <svg style="display: none;">
        <filter id="grainy">
            <feTurbulence type="fractalNoise" baseFrequency="0.6" numOctaves="3" stitchTiles="stitch" />
            <feColorMatrix type="saturate" values="0" />
        </filter>
    </svg>
    <div class="film-grain"></div>
    <div class="ambient-vignette"></div>
    <div class="custom-cursor"></div>
    <div class="site-wrapper">
        [[body]]
    </div>
    """ + GSAP_SCRIPT + """
</body>
</html>
"""
