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
<input type="checkbox" id="ignite-engine" style="display: none;">
<div id="video-background-container" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; pointer-events: none; overflow: hidden; background: black; opacity: 0; transition: opacity 2s ease;">
    <iframe id="bg-video-iframe" 
        src="https://www.youtube.com/embed/9f7_5iS7nS8?enablejsapi=1&autoplay=0&loop=1&controls=0&showinfo=0&rel=0&mute=1&playlist=9f7_5iS7nS8" 
        frameborder="0" 
        style="position: absolute; top: 50%; left: 50%; width: 100vw; height: 56.25vw; min-height: 100vh; min-width: 177.77vh; transform: translate(-50%, -50%);"
        allow="autoplay; fullscreen">
    </iframe>
</div>

<div id="css-sparks" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 10006; pointer-events: none; opacity: 0;">
    <div class="spark" style="left: 50%; top: 50%; width: 10px; height: 10px; background: orange; border-radius: 50%; position: absolute; filter: blur(2px);"></div>
</div>

<label for="ignite-engine" id="ignition-overlay" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 20000; background: black; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: opacity 1.5s ease-out, visibility 1.5s;">
    <div style="text-align: center;">
        <h2 style="color: white; font-size: 1.2rem; letter-spacing: 0.8rem; margin-bottom: 1rem; font-weight: 200;">STRIKE TO IGNITE</h2>
        <div style="width: 40px; height: 1px; background: white; margin: 0 auto; opacity: 0.3;"></div>
    </div>
</label>

<style>
    #ignite-engine:checked ~ #video-background-container { opacity: 1 !important; }
    #ignite-engine:checked ~ #ignition-overlay { opacity: 0 !important; visibility: hidden; }
    #ignite-engine:checked ~ .site-wrapper .hero-content { opacity: 1 !important; transform: translateY(0) !important; }
    #ignite-engine:checked ~ #css-sparks { animation: sparkBurst 1s ease-out forwards; }
    
    @keyframes sparkBurst {
        0% { opacity: 1; transform: scale(0); }
        100% { opacity: 0; transform: scale(5); }
    }
    
    .hero-content { 
        transition: opacity 2s ease 0.8s, transform 2s ease 0.8s !important; 
        transform: translateY(20px);
        opacity: 0;
    }
</style>

<section class="hero [[layout_class]]" id="hero" style="background: transparent !important;">
    <div class="hero-content" style="position: relative; z-index: 10000;">
        <h1 class="reveal">[[title]]</h1>
        <p class="reveal">[[subtitle]]</p>
        <div class="reveal">
            <a href="[[cta_link]]" class="btn-primary">[[cta_text]]</a>
        </div>
    </div>
</section>
<button onclick="diagnoseVisuals()" style="position: fixed; bottom: 1rem; right: 1rem; z-index: 10002; background: rgba(255,255,255,0.1); color: white; border: 1px solid white; padding: 0.5rem; border-radius: 5px; cursor: pointer;">Diagnostic</button>
<script>
    document.getElementById('ignite-engine').addEventListener('change', (e) => {
        if (e.target.checked) {
            const iframe = document.getElementById('bg-video-iframe');
            iframe.contentWindow.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
        }
    });
</script>
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

    // AETHER_IGNIS_ULTRA_IGNITION (The "Match-Strike" Experience)
    const fireContainer = document.getElementById('kinetic-fire-container');
    const overlay = document.getElementById('ignition-overlay');
    
    if (fireContainer && overlay && window.FIRE_BG) {
        const scene = new THREE.Scene();
        const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        fireContainer.appendChild(renderer.domElement);

        const loader = new THREE.TextureLoader();
        loader.load(window.FIRE_BG, (texture) => {
            const material = new THREE.ShaderMaterial({
                uniforms: { 
                    time: { value: 0.0 }, 
                    opacity: { value: 0.0 },
                    uTexture: { value: texture },
                    resolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) }
                },
                vertexShader: `void main() { gl_Position = vec4(position, 1.0); }`,
                fragmentShader: `
                    uniform float time;
                    uniform float opacity;
                    uniform sampler2D uTexture;
                    uniform vec2 resolution;
                    float hash(vec2 p) { return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453); }
                    float noise(vec2 p) {
                        vec2 i = floor(p); vec2 f = fract(p);
                        vec2 u = f*f*(3.0-2.0*f);
                        return mix(mix(hash(i + vec2(0.,0.)), hash(i + vec2(1.,0.)), u.x),
                                   mix(hash(i + vec2(0.,1.)), hash(i + vec2(1.,1.)), u.x), u.y);
                    }
                    void main() {
                        vec2 uv = gl_FragCoord.xy / resolution.xy;
                        vec4 base = texture2D(uTexture, uv);
                        float isFire = smoothstep(0.3, 0.8, length(base.rgb));
                        float distortion = noise(uv * 12.0 + time * 1.2) * 0.015 * isFire;
                        vec4 final = texture2D(uTexture, uv + vec2(distortion, distortion - time * 0.02 * isFire));
                        final.rgb *= 0.95 + 0.1 * noise(vec2(time * 3.0));
                        gl_FragColor = vec4(final.rgb, opacity);
                    }
                `,
                transparent: true
            });
            scene.add(new THREE.Mesh(new THREE.PlaneGeometry(2, 2), material));

            // Match-Strike Spark System
            const sparkCount = 150;
            const sGeometry = new THREE.BufferGeometry();
            const sPos = new Float32Array(sparkCount * 3);
            const sVel = new Float32Array(sparkCount * 3);
            for(let i=0; i<sparkCount*3; i++) { sPos[i] = 0; sVel[i] = 0; }
            sGeometry.setAttribute('position', new THREE.BufferAttribute(sPos, 3));
            const sMaterial = new THREE.PointsMaterial({ color: 0xffaa00, size: 0.02, transparent: true, opacity: 0, blending: THREE.AdditiveBlending });
            const sparks = new THREE.Points(sGeometry, sMaterial);
            scene.add(sparks);

            let ignited = false;
            overlay.addEventListener('click', () => {
                if (ignited) return;
                ignited = true;
                
                overlay.style.opacity = '0';
                setTimeout(() => overlay.style.display = 'none', 1500);

                gsap.to(material.uniforms.opacity, { value: 1, duration: 2.5, ease: "power2.inOut" });
                gsap.to(".hero-content", { opacity: 1, duration: 2, delay: 0.8 });
                
                // Spark Explosion
                sMaterial.opacity = 1;
                const vel = sGeometry.attributes.position.array;
                for(let i=0; i<sparkCount; i++) {
                    const angle = Math.random() * Math.PI * 2;
                    const speed = Math.random() * 0.08 + 0.02;
                    sVel[i*3] = Math.cos(angle) * speed;
                    sVel[i*3+1] = Math.sin(angle) * speed;
                }
                gsap.to(sMaterial, { opacity: 0, duration: 2, delay: 0.5 });
                
                // Reveal other elements
                gsap.to(".reveal, section, .card", { opacity: 1, y: 0, duration: 1.5, stagger: 0.1, ease: "power4.out", delay: 1 });
            });

            function animate(t) {
                requestAnimationFrame(animate);
                const time = t * 0.001;
                material.uniforms.time.value = time;
                
                if (ignited) {
                    const pos = sGeometry.attributes.position.array;
                    for(let i=0; i<sparkCount; i++) {
                        pos[i*3] += sVel[i*3];
                        pos[i*3+1] += sVel[i*3+1];
                        sVel[i*3+1] -= 0.002; // Gravity
                    }
                    sGeometry.attributes.position.needsUpdate = true;
                }
                renderer.render(scene, camera);
            }
            animate(0);
        });
        window.addEventListener('resize', () => renderer.setSize(window.innerWidth, window.innerHeight));
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
