from flask import Flask, render_template, request, jsonify, send_from_directory
from animus_engine import AnimusEngine
import os
import werkzeug

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

engine = AnimusEngine(output_dir="static/projects")

# AETHER_COMMAND v3.0 // OBSIDIAN & GOLD (TRANSFUSED)
DASHBOARD_HTML = """
<!DOCTYPE html>
<html class="dark" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;500;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1" rel="stylesheet"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <script id="tailwind-config">
          tailwind.config = {
            darkMode: "class",
            theme: {
              extend: {
                "colors": {
                        "surface": "#131314",
                        "primary": "#f2ca50",
                        "on-primary": "#3c2f00",
                        "on-surface": "#e5e2e3",
                        "surface-container-low": "#1c1b1c",
                        "on-surface-variant": "#d0c5af"
                },
                "fontFamily": {
                        "headline-md": ["EB Garamond"],
                        "body-md": ["Inter", "sans-serif"],
                        "code-ui": ["JetBrains Mono"]
                }
              },
            },
          }
    </script>
    <style>
        body { background-color: #0A0A0B; background-image: url(https://lh3.googleusercontent.com/aida-public/AB6AXuDlxuSL-GneSMLZFBbbaRzw0f8JwHqAk1Ah_QA1sC0Ooz7pGWfEunLBz-2Regm0kqRhpn-iNOspDi_VyG2i_KoQKpbmTr1neHIEGL8rtoEDQQ4Kh2IaZ9eUUQJiC9dWqRpA6n0hU8DTJ__pKvRbqjFYp0VVZ-vbB3qgJwq69n2jiMrSIyGTt5L836iPMymlD961GsPBrAY0rLv1Bf06eC_KkxT1eMw6by5pdVQAkpjaLUmpeNp4hWhB41ac9Y1Dj4VW-fssscJGvPg); background-repeat: repeat; }
        .obsidian-panel { background: rgba(18, 18, 20, 0.8); border: 1px solid rgba(255, 255, 255, 0.08); backdrop-filter: blur(12px); }
        .gold-rim { box-shadow: 0 0 2px 0 rgba(212, 175, 55, 0.3), 0 0 20px 0 rgba(212, 175, 55, 0.05); }
        .gold-rim-hover:hover { box-shadow: 0 0 5px 1px rgba(212, 175, 55, 0.4), 0 0 30px 2px rgba(212, 175, 55, 0.1); border-color: rgba(212, 175, 55, 0.3); }
        @keyframes pulse-rotate { 0% { transform: scale(1) rotate(0deg); opacity: 0.9; } 50% { transform: scale(1.05) rotate(180deg); opacity: 1; } 100% { transform: scale(1) rotate(360deg); opacity: 0.9; } }
        .animate-aether-core { animation: pulse-rotate 20s linear infinite; }
        .glass-header { backdrop-filter: blur(20px); background: rgba(18, 18, 20, 0.7); }
        .film-grain { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 9999; opacity: 0.1; background: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); mix-blend-mode: overlay; }
        .custom-cursor { position: fixed; width: 20px; height: 20px; border: 1px solid #f2ca50; border-radius: 50%; pointer-events: none; z-index: 99999; transform: translate(-50%, -50%); transition: transform 0.1s; }
        textarea:focus, input:focus { outline: none; border-color: #f2ca50 !important; }
    </style>
</head>
<body class="min-h-screen flex flex-col font-body-md text-on-surface overflow-hidden">
    <div class="film-grain"></div>
    <div class="custom-cursor" id="cursor"></div>

    <header class="fixed top-0 left-0 w-full z-50 glass-header border-b border-white/5 shadow-xl">
        <div class="flex justify-between items-center px-10 py-4 w-full max-w-[1440px] mx-auto">
            <div class="flex items-center gap-6">
                <span class="font-headline-md text-2xl font-bold tracking-tighter text-primary uppercase">Aether Command</span>
                <nav class="hidden md:flex items-center gap-6 ml-8">
                    <a class="text-[11px] uppercase tracking-widest text-primary border-b-2 border-primary pb-1 font-bold" href="#">Engine</a>
                    <a class="text-[11px] uppercase tracking-widest text-on-surface-variant hover:text-on-surface transition-colors" href="#">Blueprint</a>
                    <a class="text-[11px] uppercase tracking-widest text-on-surface-variant hover:text-on-surface transition-colors" href="#">Deploy</a>
                    <a class="text-[11px] uppercase tracking-widest text-on-surface-variant hover:text-on-surface transition-colors" href="#">Vault</a>
                </nav>
            </div>
            <div class="flex items-center gap-4">
                <button onclick="ignite()" class="bg-primary text-on-primary font-code-ui text-[13px] px-6 py-2 rounded-sm font-bold active:scale-95 transition-all gold-rim hover:shadow-primary/20">EXECUTE MISSION</button>
            </div>
        </div>
    </header>

    <main class="flex-grow pt-32 pb-16 px-10 max-w-[1440px] mx-auto w-full grid grid-cols-12 gap-8 items-center">
        <!-- Left: Inputs -->
        <div class="col-span-12 lg:col-span-5 space-y-8">
            <div class="obsidian-panel p-8 rounded-xl gold-rim-hover transition-all">
                <span class="text-[10px] uppercase tracking-[0.2em] text-primary/60 mb-4 block">Neural Mission Objective</span>
                <input type="text" id="mission" placeholder="DESCRIBE YOUR DIGITAL REALM..." class="w-full bg-white/5 border border-white/10 rounded-lg p-4 text-sm font-code-ui text-white">
            </div>

            <div class="grid grid-cols-2 gap-4">
                <div class="obsidian-panel p-6 rounded-xl gold-rim-hover transition-all">
                    <span class="text-[10px] uppercase tracking-[0.2em] text-primary/60 mb-4 block">Source Document</span>
                    <label for="file-upload" class="cursor-pointer flex flex-col items-center gap-2 text-on-surface-variant hover:text-primary transition-all">
                        <i class="fa-solid fa-paperclip text-2xl" id="file-icon"></i>
                        <span class="text-[10px]" id="file-name">ATTACH SOURCE</span>
                    </label>
                    <input type="file" id="file-upload" class="hidden" onchange="updateFileStatus()">
                </div>
                <div class="obsidian-panel p-6 rounded-xl gold-rim-hover transition-all">
                    <span class="text-[10px] uppercase tracking-[0.2em] text-primary/60 mb-4 block">HTML Injection</span>
                    <textarea id="html-injection" placeholder="PASTE RAW CODE..." class="w-full h-24 bg-white/5 border border-white/10 rounded-lg p-3 text-[12px] font-code-ui text-white resize-none"></textarea>
                </div>
            </div>

            <div id="results" class="hidden obsidian-panel p-6 rounded-xl border-primary/20 bg-primary/5">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-code-ui tracking-widest text-primary animate-pulse">MISSION_SUCCESS:</span>
                    <a id="view-link" href="#" target="_blank" class="text-xs font-bold underline decoration-primary underline-offset-4">LAUNCH_DEPLOYMENT</a>
                </div>
            </div>
            
            <div id="status" class="text-[10px] font-code-ui uppercase tracking-[0.3em] opacity-30">Status: Terminal Idle</div>
        </div>

        <!-- Center: Aether Core -->
        <div class="col-span-12 lg:col-span-7 flex flex-col items-center justify-center relative">
            <div class="absolute w-[600px] h-[600px] bg-primary/5 rounded-full blur-[120px] pointer-events-none"></div>
            <div class="animate-aether-core w-[450px] h-[450px] relative z-10">
                <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuDlxuSL-GneSMLZFBbbaRzw0f8JwHqAk1Ah_QA1sC0Ooz7pGWfEunLBz-2Regm0kqRhpn-iNOspDi_VyG2i_KoQKpbmTr1neHIEGL8rtoEDQQ4Kh2IaZ9eUUQJiC9dWqRpA6n0hU8DTJ__pKvRbqjFYp0VVZ-vbB3qgJwq69n2jiMrSIyGTt5L836iPMymlD961GsPBrAY0rLv1Bf06eC_KkxT1eMw6by5pdVQAkpjaLUmpeNp4hWhB41ac9Y1Dj4VW-fssscJGvPg" class="w-full h-full object-contain filter drop-shadow-[0_0_30px_rgba(212,175,55,0.3)]">
            </div>
            
            <!-- Sovereign Seal -->
            <div class="signature absolute bottom-0 right-0 w-48 opacity-60 hover:opacity-100 transition-opacity cursor-pointer">
                <canvas id="sig-canvas" style="width: 100%; height: auto;"></canvas>
            </div>
        </div>
    </main>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script>
        // Magnetic Cursor
        const cursor = document.getElementById('cursor');
        window.addEventListener('mousemove', (e) => {
            gsap.to(cursor, { x: e.clientX, y: e.clientY, duration: 0.6, ease: "power2.out" });
        });

        // Neural Ink Extraction logic
        function extractSignature() {
            const img = new Image();
            img.src = '/static/signature.jpg';
            img.onload = () => {
                const canvas = document.getElementById('sig-canvas');
                const ctx = canvas.getContext('2d');
                canvas.width = img.width;
                canvas.height = img.height;
                ctx.drawImage(img, 0, 0);
                const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
                const data = imageData.data;
                for (let i = 0; i < data.length; i += 4) {
                    if ((data[i] + data[i+1] + data[i+2]) / 3 < 160) {
                        data[i] = 242; data[i+1] = 202; data[i+2] = 80; data[i+3] = 255; // Re-color to Aether Gold
                    } else { data[i+3] = 0; }
                }
                ctx.putImageData(imageData, 0, 0);
            };
        }
        extractSignature();

        function updateFileStatus() {
            const file = document.getElementById('file-upload').files[0];
            if (file) {
                document.getElementById('file-name').innerText = file.name;
                document.getElementById('file-icon').className = "fa-solid fa-check text-primary";
            }
        }

        async function ignite() {
            const mission = document.getElementById('mission').value;
            const html = document.getElementById('html-injection').value;
            const fileInput = document.getElementById('file-upload');
            const status = document.getElementById('status');
            const results = document.getElementById('results');
            const viewLink = document.getElementById('view-link');
            
            status.innerText = "INITIALIZING_SYNTHESIS_ENGINE...";
            gsap.to('.animate-aether-core', { scale: 1.2, duration: 0.5, repeat: -1, yoyo: true });
            
            const formData = new FormData();
            formData.append('mission', mission);
            formData.append('html', html);
            if (fileInput.files[0]) formData.append('file', fileInput.files[0]);

            try {
                const response = await fetch('/generate', { method: 'POST', body: formData });
                const data = await response.json();
                status.innerText = "SYNTHESIS_COMPLETE // PROJECT_AUDITED";
                results.classList.remove('hidden');
                viewLink.href = data.url;
                gsap.to('.animate-aether-core', { scale: 1, duration: 1 });
            } catch (err) {
                status.innerText = "SYSTEM_ERROR // CORE_OVERHEAT";
            }
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
        try:
            with open(filepath, 'r', errors='ignore') as f:
                extracted_text = f.read()
        except:
            extracted_text = "File uploaded: " + filename

    total_mission = f"{mission}. Document Context: {extracted_text}. HTML Reference: {html_injection}"
    engine.generate_project(total_mission[:500])
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
