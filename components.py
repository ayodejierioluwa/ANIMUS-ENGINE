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
<section class="hero" id="hero">
    <div id="three-canvas-container"></div>
    <div class="hero-content">
        <h1 class="reveal">{title}</h1>
        <p class="reveal">{subtitle}</p>
        <div class="reveal">
            <a href="{cta_link}" class="btn-primary">{cta_text}</a>
        </div>
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
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        container.appendChild(renderer.domElement);

        const geometry = new THREE.IcosahedronGeometry(2, 1);
        const material = new THREE.MeshPhongMaterial({
            color: 0x00ffcc,
            wireframe: true,
            transparent: true,
            opacity: 0.5
        });
        const sphere = new THREE.Mesh(geometry, material);
        scene.add(sphere);

        const light = new THREE.PointLight(0xffffff, 1, 100);
        light.position.set(10, 10, 10);
        scene.add(light);
        scene.add(new THREE.AmbientLight(0x404040));

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

    // Content Safe Reveal (Fixes disappearing bug)
    gsap.utils.toArray("section").forEach(section => {
        gsap.from(section, {
            scrollTrigger: {
                trigger: section,
                start: "top 90%",
                toggleActions: "play none none none"
            },
            opacity: 0,
            y: 30,
            duration: 1
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
</script>
"""
