# AETHER_ANIMUS Component Library

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

VIDEO_HERO_TEMPLATE = """
<video autoplay muted loop playsinline id="bg-video" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; object-fit: cover; z-index: 1; pointer-events: none; background: black;">
    <source src="[[video_url]]" type="video/mp4">
</video>
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const v = document.getElementById('bg-video');
        if (v) v.play().catch(e => console.log("Autoplay blocked, waiting for interaction."));
    });
</script>
<section class="hero [[layout_class]]" id="hero" style="background: transparent !important;">
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

    // Liquid Fire Shader (The "WOWER" Guarantee)
    const shaderContainer = document.getElementById('shader-background-container');
    if (shaderContainer) {
        const s_scene = new THREE.Scene();
        const s_camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
        const s_renderer = new THREE.WebGLRenderer({ antialias: true });
        s_renderer.setSize(window.innerWidth, window.innerHeight);
        shaderContainer.appendChild(s_renderer.domElement);

        const s_material = new THREE.ShaderMaterial({
            uniforms: { time: { value: 1.0 }, resolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) } },
            vertexShader: `void main() { gl_Position = vec4(position, 1.0); }`,
            fragmentShader: `
                uniform float time;
                uniform vec2 resolution;
                float hash(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453123); }
                float noise(vec2 p) {
                    vec2 i = floor(p); vec2 f = fract(p);
                    vec2 u = f*f*(3.0-2.0*f);
                    return mix(mix(hash(i + vec2(0.0,0.0)), hash(i + vec2(1.0,0.0)), u.x),
                               mix(hash(i + vec2(0.0,1.0)), hash(i + vec2(1.0,1.0)), u.x), u.y);
                }
                void main() {
                    vec2 uv = gl_FragCoord.xy / resolution.xy;
                    float n = noise(uv * 4.0 + time * 0.5);
                    vec3 fire = mix(vec3(0.8, 0.1, 0.0), vec3(1.0, 0.6, 0.1), n);
                    gl_FragColor = vec4(fire * (1.0 - uv.y) * 1.5, 1.0);
                }
            `
        });
        const s_mesh = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), s_material);
        s_scene.add(s_mesh);

        function s_animate(t) {
            requestAnimationFrame(s_animate);
            s_material.uniforms.time.value = t * 0.001;
            s_renderer.render(s_scene, s_camera);
        }
        s_animate(0);
        
        window.addEventListener('resize', () => {
            s_renderer.setSize(window.innerWidth, window.innerHeight);
            s_material.uniforms.resolution.value.set(window.innerWidth, window.innerHeight);
        });
    }

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

    // Initial Reveal Animations
    gsap.to(".reveal", {
        opacity: 1,
        y: 0,
        duration: 1.5,
        stagger: 0.15,
        ease: "expo.out",
        delay: 0.2
    });

    // Stunning Card Entrances
    gsap.utils.toArray(".card").forEach((card, i) => {
        gsap.from(card, {
            scrollTrigger: {
                trigger: card,
                start: "top 95%",
                toggleActions: "play none none none"
            },
            opacity: 0,
            scale: 0.8,
            rotationY: 15,
            duration: 1.2,
            delay: i * 0.1,
            ease: "back.out(1.7)"
        });
    });

    // Robust Scroll Reveal (Final Fix for disappearing bug)
    gsap.utils.toArray(".reveal, section, .card").forEach(el => {
        gsap.set(el, { opacity: 0, y: 30 }); // Ensure initial state
        ScrollTrigger.create({
            trigger: el,
            start: "top 95%",
            onEnter: () => gsap.to(el, { opacity: 1, y: 0, duration: 1.2, ease: "power4.out" })
        });
    });

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
