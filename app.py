from flask import Flask, render_template, request, jsonify, send_from_directory
from animus_engine import AnimusEngine
import os
import werkzeug

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

engine = AnimusEngine(output_dir="static/projects")

# AETHER_COMMAND Dashboard v2.0 (Multimodal)
DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AETHER_COMMAND | Nerve Center</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root { --accent: #00ffcc; --bg: #050505; }
        body { background: var(--bg); color: white; font-family: 'Space Mono', monospace; margin: 0; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }
        #void-canvas { position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0.3; pointer-events: none; }
        .dashboard { width: 900px; padding: 4rem; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); backdrop-filter: blur(40px); border-radius: 24px; text-align: center; position: relative; z-index: 10; }
        h1 { font-size: 0.8rem; letter-spacing: 0.5em; opacity: 0.5; margin-bottom: 3rem; color: var(--accent); }
        .grid-inputs { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 2rem; }
        .input-group { text-align: left; }
        .label { font-size: 0.6rem; opacity: 0.4; margin-bottom: 0.5rem; display: block; }
        input, textarea { width: 100%; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); color: white; font-family: inherit; padding: 1rem; border-radius: 12px; outline: none; transition: border 0.4s; }
        input:focus, textarea:focus { border: 1px solid var(--accent); }
        textarea { height: 100px; resize: none; }
        .btn-ignite { margin-top: 3rem; background: white; color: black; border: none; padding: 1.25rem 4rem; border-radius: 50px; font-weight: 700; cursor: pointer; transition: all 0.3s; font-size: 0.9rem; letter-spacing: 0.1em; }
        .btn-ignite:hover { transform: scale(1.05); box-shadow: 0 0 40px var(--accent); }
        .status { margin-top: 2rem; font-size: 0.7rem; opacity: 0.4; font-family: 'Space Mono'; }
        #results { margin-top: 2rem; display: none; padding: 1.5rem; background: rgba(0,255,204,0.05); border: 1px solid rgba(0,255,204,0.2); border-radius: 12px; }
        a { color: var(--accent); text-decoration: none; font-weight: 700; }
        .file-input { display: none; }
        .file-label { cursor: pointer; border: 1px dashed rgba(255,255,255,0.2); padding: 1rem; border-radius: 12px; display: flex; align-items: center; justify-content: center; gap: 1rem; opacity: 0.6; transition: all 0.3s; height: 100px; }
        .file-label:hover { border-color: var(--accent); opacity: 1; }
        .custom-cursor { position: fixed; width: 20px; height: 20px; border: 1px solid var(--accent); border-radius: 50%; pointer-events: none; z-index: 99999; transform: translate(-50%, -50%); transition: transform 0.1s; }
        
        /* Tactical Layer: High-Contrast Photon Grain */
        .film-grain {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 99999;
            opacity: 0.15;
            background: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
            mix-blend-mode: soft-light;
            animation: grain-shift 0.2s steps(2) infinite;
        }
        @keyframes grain-shift {
            0% { transform: translate(0,0); }
            100% { transform: translate(-5%, -5%); }
        }
    </style>
</head>
<body>
    <div class="film-grain"></div>
    <div id="void-canvas"></div>
    <div class="custom-cursor" id="cursor"></div>

    <div class="dashboard">
        <h1>AETHER_COMMAND v2.1 // TACTILE_DNA</h1>
        
        <div class="input-group">
            <span class="label">NEURAL_MISSION_PROMPT</span>
            <input type="text" id="mission" placeholder="ENTER CORE MISSION OBJECTIVE...">
        </div>

        <div class="grid-inputs">
            <div class="input-group">
                <span class="label">SOURCE_DOCUMENT_UPLOAD</span>
                <label class="file-label" for="file-upload" id="file-status">
                    <i class="fa-solid fa-paperclip"></i>
                    <span>CLICK TO ATTACH DOCS</span>
                </label>
                <input type="file" id="file-upload" class="file-input" onchange="updateFileStatus()">
            </div>
            <div class="input-group">
                <span class="label">HTML_TRANSFUSION_PORTAL</span>
                <textarea id="html-injection" placeholder="PASTE LEGACY HTML CODE HERE..."></textarea>
            </div>
        </div>

        <button class="btn-ignite" onclick="ignite()">EXECUTE_TRANSFUSION</button>
        
        <div class="status" id="status">STATUS: SYSTEM_READY_FOR_INPUT</div>
        
        <div id="results">
            <p>PROJECT_SYNTHESIZED: <a id="view-link" href="#" target="_blank">OPEN_LIVE_DEPLOYMENT</a></p>
        </div>

        <div class="signature" style="position: absolute; bottom: 2rem; right: 2rem; width: 150px; opacity: 0.6; filter: invert(1) hue-rotate(120deg) brightness(2) contrast(1.2); mix-blend-mode: screen; transition: opacity 0.5s var(--ease-vibe); cursor: pointer;" onmouseover="this.style.opacity=1" onmouseout="this.style.opacity=0.6">
            <img src="/static/signature.jpg" style="width: 100%; height: auto;">
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script>
        // Void Background Physics
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        document.getElementById('void-canvas').appendChild(canvas);
        function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
        window.addEventListener('resize', resize); resize();
        function animate() {
            ctx.clearRect(0,0,canvas.width, canvas.height);
            ctx.fillStyle = 'rgba(0, 255, 204, 0.1)';
            for(let i=0; i<40; i++) {
                ctx.beginPath();
                ctx.arc(Math.sin(Date.now()*0.0002 + i)*canvas.width, Math.cos(Date.now()*0.0001 + i)*canvas.height, 1, 0, Math.PI*2);
                ctx.fill();
            }
            requestAnimationFrame(animate);
        }
        animate();

        // Magnetic Cursor
        const cursor = document.getElementById('cursor');
        window.addEventListener('mousemove', (e) => {
            gsap.to(cursor, { x: e.clientX, y: e.clientY, duration: 0.6, ease: "power2.out" });
        });

        function updateFileStatus() {
            const file = document.getElementById('file-upload').files[0];
            if (file) document.getElementById('file-status').innerHTML = '<i class="fa-solid fa-check" style="color: var(--accent)"></i> <span>' + file.name + '</span>';
        }

        async function ignite() {
            const mission = document.getElementById('mission').value;
            const html = document.getElementById('html-injection').value;
            const fileInput = document.getElementById('file-upload');
            const status = document.getElementById('status');
            const results = document.getElementById('results');
            
            status.innerText = "INITIALIZING_SYNTHESIS_ENGINE...";
            
            const formData = new FormData();
            formData.append('mission', mission);
            formData.append('html', html);
            if (fileInput.files[0]) formData.append('file', fileInput.files[0]);

            const response = await fetch('/generate', { method: 'POST', body: formData });
            const data = await response.json();
            status.innerText = "SYNTHESIS_COMPLETE // PROJECT_AUDITED";
            results.style.display = "block";
            document.getElementById('view-link').href = data.url;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return DASHBOARD_HTML

@app.route('/generate', methods=['POST'])
def generate():
    mission = request.form.get('mission', 'Autonomous Project')
    html_injection = request.form.get('html', '')
    file = request.files.get('file')
    
    extracted_text = ""
    if file:
        filename = werkzeug.utils.secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Simple extraction for now (we'll expand to PDF parsing)
        try:
            with open(filepath, 'r', errors='ignore') as f:
                extracted_text = f.read()
        except:
            extracted_text = "File uploaded: " + filename

    # Combine all context for the Soul
    total_mission = f"{mission}. Document Context: {extracted_text}. HTML Reference: {html_injection}"
    
    engine.generate_project(total_mission[:500]) # Cap mission length for stability
    return jsonify({"status": "success", "url": "/static/projects/index.html"})

@app.route('/static/projects/<path:path>')
def serve_project(path):
    return send_from_directory('static/projects', path)

@app.route('/api/bridge', methods=['POST'])
def bridge():
    data = request.json
    mission = data.get('mission')
    engine.generate_project(mission)
    return jsonify({"status": "success", "url": "/static/projects/index.html"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
