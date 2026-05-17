from flask import Flask, render_template, request, jsonify, send_from_directory
from animus_engine import AnimusEngine
import os
import werkzeug

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

engine = AnimusEngine(output_dir="static/projects")

# AETHER_COMMAND v3.1 // FULL ARCHITECT OS
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
        .tab-content { display: none; }
        .tab-content.active { display: block; }
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-thumb { background: #f2ca50; border-radius: 10px; }
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
                    <button onclick="showTab('engine')" class="tab-btn text-[11px] uppercase tracking-widest text-primary border-b-2 border-primary pb-1 font-bold">Engine</button>
                    <button onclick="showTab('blueprint')" class="tab-btn text-[11px] uppercase tracking-widest text-on-surface-variant hover:text-on-surface transition-colors">Blueprint</button>
                    <button onclick="showTab('deploy')" class="tab-btn text-[11px] uppercase tracking-widest text-on-surface-variant hover:text-on-surface transition-colors">Deploy</button>
                    <button onclick="showTab('vault')" class="tab-btn text-[11px] uppercase tracking-widest text-on-surface-variant hover:text-on-surface transition-colors">Vault</button>
                </nav>
            </div>
            <div class="flex items-center gap-4">
                <button onclick="ignite()" class="bg-primary text-on-primary font-code-ui text-[13px] px-6 py-2 rounded-sm font-bold active:scale-95 transition-all gold-rim">EXECUTE MISSION</button>
            </div>
        </div>
    </header>

    <main class="flex-grow pt-32 pb-16 px-10 max-w-[1440px] mx-auto w-full relative">
        
        <!-- TAB: ENGINE (Main) -->
        <div id="tab-engine" class="tab-content active grid grid-cols-12 gap-8 items-center h-full">
            <div class="col-span-5 space-y-8">
                <div class="obsidian-panel p-8 rounded-xl gold-rim-hover transition-all">
                    <span class="text-[10px] uppercase tracking-[0.2em] text-primary/60 mb-4 block">Neural Mission Objective</span>
                    <input type="text" id="mission" placeholder="DESCRIBE YOUR DIGITAL REALM..." class="w-full bg-white/5 border border-white/10 rounded-lg p-4 text-sm font-code-ui text-white">
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div class="obsidian-panel p-6 rounded-xl gold-rim-hover transition-all">
                        <span class="text-[10px] uppercase tracking-[0.2em] text-primary/60 mb-4 block">Source Document</span>
                        <label for="file-upload" class="cursor-pointer flex flex-col items-center gap-2 text-on-surface-variant hover:text-primary">
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
                    <span class="text-xs font-code-ui tracking-widest text-primary animate-pulse">MISSION_SUCCESS:</span>
                    <a id="view-link" href="#" target="_blank" class="ml-4 text-xs font-bold underline">LAUNCH_DEPLOYMENT</a>
                </div>
                <div id="status" class="text-[10px] font-code-ui uppercase tracking-[0.3em] opacity-30">Status: Terminal Idle</div>
            </div>
            <div class="col-span-7 flex flex-col items-center justify-center relative">
                <div class="absolute w-[600px] h-[600px] bg-primary/5 rounded-full blur-[120px] pointer-events-none"></div>
                <!-- TRUE AETHER COMPASS ROSE (SVG) -->
                <div id="compass-wrap" style="width:420px;height:420px;position:relative;z-index:10;animation:compass-spin 25s linear infinite;filter:drop-shadow(0 0 40px rgba(212,175,55,0.4));">
                <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" width="420" height="420">
                  <defs>
                    <radialGradient id="cg" cx="50%" cy="50%" r="50%">
                      <stop offset="0%" stop-color="#f2ca50" stop-opacity="0.15"/>
                      <stop offset="100%" stop-color="#f2ca50" stop-opacity="0"/>
                    </radialGradient>
                    <filter id="glow"><feGaussianBlur stdDeviation="3" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
                  </defs>
                  <!-- Outer rings -->
                  <circle cx="200" cy="200" r="195" fill="none" stroke="#f2ca50" stroke-width="0.5" opacity="0.3"/>
                  <circle cx="200" cy="200" r="185" fill="none" stroke="#f2ca50" stroke-width="1" opacity="0.2"/>
                  <circle cx="200" cy="200" r="170" fill="url(#cg)" stroke="#f2ca50" stroke-width="1.5" opacity="0.6"/>
                  <circle cx="200" cy="200" r="140" fill="none" stroke="#f2ca50" stroke-width="0.5" opacity="0.3"/>
                  <circle cx="200" cy="200" r="100" fill="none" stroke="#f2ca50" stroke-width="0.5" opacity="0.2"/>
                  <circle cx="200" cy="200" r="60" fill="none" stroke="#f2ca50" stroke-width="1" opacity="0.4"/>
                  <!-- 32-point tick marks -->
                  <g stroke="#f2ca50" filter="url(#glow)">
                    <line x1="200" y1="5" x2="200" y2="30" stroke-width="2" opacity="0.9"/>
                    <line x1="200" y1="370" x2="200" y2="395" stroke-width="2" opacity="0.9"/>
                    <line x1="5" y1="200" x2="30" y2="200" stroke-width="2" opacity="0.9"/>
                    <line x1="370" y1="200" x2="395" y2="200" stroke-width="2" opacity="0.9"/>
                    <!-- 45deg ticks -->
                    <line x1="338" y1="62" x2="320" y2="80" stroke-width="1.5" opacity="0.7"/>
                    <line x1="62" y1="62" x2="80" y2="80" stroke-width="1.5" opacity="0.7"/>
                    <line x1="338" y1="338" x2="320" y2="320" stroke-width="1.5" opacity="0.7"/>
                    <line x1="62" y1="338" x2="80" y2="320" stroke-width="1.5" opacity="0.7"/>
                    <!-- 22.5deg small ticks -->
                    <line x1="280" y1="16" x2="274" y2="29" stroke-width="1" opacity="0.4"/>
                    <line x1="120" y1="16" x2="126" y2="29" stroke-width="1" opacity="0.4"/>
                    <line x1="384" y1="120" x2="371" y2="126" stroke-width="1" opacity="0.4"/>
                    <line x1="384" y1="280" x2="371" y2="274" stroke-width="1" opacity="0.4"/>
                    <line x1="16" y1="120" x2="29" y2="126" stroke-width="1" opacity="0.4"/>
                    <line x1="16" y1="280" x2="29" y2="274" stroke-width="1" opacity="0.4"/>
                    <line x1="280" y1="384" x2="274" y2="371" stroke-width="1" opacity="0.4"/>
                    <line x1="120" y1="384" x2="126" y2="371" stroke-width="1" opacity="0.4"/>
                  </g>
                  <!-- Cardinal labels -->
                  <g font-family="EB Garamond,serif" font-size="22" fill="#f2ca50" text-anchor="middle" filter="url(#glow)" opacity="0.95">
                    <text x="200" y="45" font-weight="700">N</text>
                    <text x="200" y="372">S</text>
                    <text x="360" y="206">E</text>
                    <text x="40" y="206">W</text>
                  </g>
                  <!-- Ordinal labels -->
                  <g font-family="EB Garamond,serif" font-size="13" fill="#f2ca50" text-anchor="middle" opacity="0.6">
                    <text x="337" y="72">NE</text>
                    <text x="63" y="72">NW</text>
                    <text x="337" y="340">SE</text>
                    <text x="63" y="340">SW</text>
                  </g>
                  <!-- Main compass star — North (gold) -->
                  <polygon points="200,30 210,185 200,200 190,185" fill="#f2ca50" filter="url(#glow)" opacity="0.95"/>
                  <!-- South (dark) -->
                  <polygon points="200,370 210,215 200,200 190,215" fill="#8b6914" opacity="0.9"/>
                  <!-- East (gold) -->
                  <polygon points="370,200 215,190 200,200 215,210" fill="#f2ca50" filter="url(#glow)" opacity="0.8"/>
                  <!-- West (dark) -->
                  <polygon points="30,200 185,190 200,200 185,210" fill="#8b6914" opacity="0.7"/>
                  <!-- Ordinal arrow points -->
                  <polygon points="200,75 207,140 200,150 193,140" fill="#f2ca50" opacity="0.4" transform="rotate(45,200,200)"/>
                  <polygon points="200,75 207,140 200,150 193,140" fill="#f2ca50" opacity="0.4" transform="rotate(135,200,200)"/>
                  <polygon points="200,75 207,140 200,150 193,140" fill="#f2ca50" opacity="0.4" transform="rotate(225,200,200)"/>
                  <polygon points="200,75 207,140 200,150 193,140" fill="#f2ca50" opacity="0.4" transform="rotate(315,200,200)"/>
                  <!-- Inner rings -->
                  <circle cx="200" cy="200" r="28" fill="#0a0a0b" stroke="#f2ca50" stroke-width="1.5" opacity="0.9"/>
                  <circle cx="200" cy="200" r="18" fill="#f2ca50" opacity="0.15"/>
                  <circle cx="200" cy="200" r="8" fill="#f2ca50" filter="url(#glow)" opacity="0.9"/>
                </svg>
                </div>
                <style>@keyframes compass-spin{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}</style>
                </div>
                <!-- Sovereign Seal -->
                <div class="signature absolute bottom-0 right-0 w-48 opacity-60 hover:opacity-100 transition-opacity cursor-pointer">
                    <canvas id="sig-canvas" style="width: 100%; height: auto;"></canvas>
                </div>
            </div>
        </div>

        <!-- TAB: BLUEPRINT -->
        <div id="tab-blueprint" class="tab-content h-full">
            <div class="grid grid-cols-12 gap-8 h-[600px]">
                <div class="col-span-4 obsidian-panel p-6 rounded-xl overflow-y-auto">
                    <span class="text-[10px] uppercase tracking-widest text-primary mb-4 block">Project_File_System</span>
                    <ul id="file-list" class="space-y-2 text-sm font-code-ui text-on-surface-variant">
                        <!-- Populated by JS -->
                    </ul>
                </div>
                <div class="col-span-8 obsidian-panel p-8 rounded-xl relative">
                    <span class="text-[10px] uppercase tracking-widest text-primary mb-4 block">Source_Code_Terminal</span>
                    <div id="code-viewer" class="h-full overflow-y-auto text-[12px] font-code-ui text-white/80 whitespace-pre bg-black/20 p-4 rounded-lg border border-white/5">
                        // Select a file to view its neural architecture...
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB: DEPLOY -->
        <div id="tab-deploy" class="tab-content">
            <div class="max-w-2xl mx-auto obsidian-panel p-12 rounded-xl text-center space-y-8">
                <i class="fa-solid fa-cloud-arrow-up text-6xl text-primary opacity-20"></i>
                <h2 class="font-headline-md text-3xl">Ready for Redeployment?</h2>
                <p class="text-on-surface-variant text-sm">You can refine your mission or source documents in the Engine tab and execute a full re-architecture here.</p>
                <button onclick="showTab('engine')" class="bg-primary text-on-primary font-code-ui text-sm px-8 py-3 rounded-sm font-bold active:scale-95 transition-all">REFINE MISSION</button>
            </div>
        </div>

        <!-- TAB: VAULT -->
        <div id="tab-vault" class="tab-content">
            <div class="grid grid-cols-3 gap-8" id="vault-list">
                <!-- Archived projects will appear here -->
                <div class="obsidian-panel p-8 rounded-xl text-center space-y-4 gold-rim-hover cursor-pointer opacity-40">
                    <i class="fa-solid fa-box-archive text-3xl text-primary"></i>
                    <h3 class="text-sm uppercase tracking-widest">Legacy_Archive</h3>
                </div>
            </div>
        </div>

    </main>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script>
        // Tab Navigation Logic
        function showTab(tabName) {
            document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
            document.getElementById('tab-' + tabName).classList.add('active');
            
            document.querySelectorAll('.tab-btn').forEach(b => {
                b.classList.remove('text-primary', 'border-primary', 'border-b-2', 'font-bold');
                b.classList.add('text-on-surface-variant');
            });
            event.currentTarget.classList.add('text-primary', 'border-primary', 'border-b-2', 'font-bold');
            
            if(tabName === 'blueprint') loadFiles();
        }

        // Blueprint Logic
        async function loadFiles() {
            const response = await fetch('/api/list_files');
            const files = await response.json();
            const list = document.getElementById('file-list');
            list.innerHTML = '';
            files.forEach(f => {
                const li = document.createElement('li');
                li.className = "hover:text-primary cursor-pointer p-2 rounded transition-all";
                li.innerText = f;
                li.onclick = () => viewCode(f);
                list.appendChild(li);
            });
        }

        async function viewCode(filename) {
            const response = await fetch('/api/get_file?name=' + filename);
            const code = await response.text();
            document.getElementById('code-viewer').innerText = code;
        }

        // Magnetic Cursor
        const cursor = document.getElementById('cursor');
        window.addEventListener('mousemove', (e) => {
            gsap.to(cursor, { x: e.clientX, y: e.clientY, duration: 0.6, ease: "power2.out" });
        });

        // Neural Ink Extraction
        function extractSignature() {
            const img = new Image();
            img.src = '/static/signature.jpg';
            img.onload = () => {
                const canvas = document.getElementById('sig-canvas');
                const ctx = canvas.getContext('2d');
                canvas.width = img.width; canvas.height = img.height;
                ctx.drawImage(img, 0, 0);
                const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
                const data = imageData.data;
                for (let i = 0; i < data.length; i += 4) {
                    if ((data[i] + data[i+1] + data[i+2]) / 3 < 160) {
                        data[i] = 242; data[i+1] = 202; data[i+2] = 80; data[i+3] = 255;
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

        // Retrieve or generate unique persistent client identifier
        let animusUserId = localStorage.getItem('animus_user_id');
        if (!animusUserId) {
            animusUserId = 'user_' + Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
            localStorage.setItem('animus_user_id', animusUserId);
        }

        async function ignite() {
            const status = document.getElementById('status');
            const results = document.getElementById('results');
            status.innerText = "INITIALIZING_SYNTHESIS_ENGINE...";
            gsap.to('.animate-aether-core', { scale: 1.1, duration: 0.3, repeat: -1, yoyo: true });
            
            const formData = new FormData();
            formData.append('mission', document.getElementById('mission').value);
            formData.append('html', document.getElementById('html-injection').value);
            formData.append('user_id', animusUserId);
            if (document.getElementById('file-upload').files[0]) formData.append('file', document.getElementById('file-upload').files[0]);

            const response = await fetch('/generate', { method: 'POST', body: formData });
            const data = await response.json();
            status.innerText = "SYNTHESIS_COMPLETE // PROJECT_AUDITED";
            results.classList.remove('hidden');
            document.getElementById('view-link').href = data.url;
            gsap.to('.animate-aether-core', { scale: 1, duration: 1 });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return DASHBOARD_HTML

def extract_file_content(filepath):
    import os
    ext = os.path.splitext(filepath)[1].lower()
    text = ""
    if ext == '.pdf':
        try:
            import pypdf
            reader = pypdf.PdfReader(filepath)
            for page in reader.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
        except Exception as e:
            text = f"[PDF Parse Error: {e}]"
    elif ext in ['.docx', '.doc']:
        try:
            import docx
            doc = docx.Document(filepath)
            text = "\n".join([p.text for p in doc.paragraphs])
        except Exception as e:
            text = f"[DOCX Parse Error: {e}]"
    else:
        try:
            with open(filepath, 'r', errors='ignore', encoding='utf-8') as f:
                text = f.read()
        except Exception as e:
            text = f"[Text File Parse Error: {e}]"
    return text

@app.route('/generate', methods=['POST'])
def generate():
    mission = request.form.get('mission', 'Autonomous Project')
    html_injection = request.form.get('html', '')
    user_id = request.form.get('user_id', 'anonymous')
    file = request.files.get('file')
    extracted_text = ""
    if file:
        filename = werkzeug.utils.secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        extracted_text = extract_file_content(filepath)

    total_mission = f"{mission}. Context: {extracted_text}. HTML: {html_injection}"
    engine.generate_project(total_mission, user_id=user_id)
    import time
    return jsonify({"status": "success", "url": f"/static/projects/index.html?t={int(time.time())}"})

@app.route('/api/list_files')
def list_files():
    project_dir = 'static/projects'
    files = [f for f in os.listdir(project_dir) if f.endswith(('.html', '.css', '.js'))]
    return jsonify(files)

@app.route('/api/get_file')
def get_file():
    name = request.args.get('name')
    return send_from_directory('static/projects', name)

@app.route('/static/projects/<path:path>')
def serve_project(path):
    # Verify if it's an HTML page first
    if path.endswith('.html') or '.' not in path:
        page_name = path if path.endswith('.html') else f"{path}.html"
        db_path = "/Users/macbook/.gemini/antigravity/scratch/aether_companion/laura_memory.db"
        if not os.path.exists(db_path):
            db_path = "laura_memory.db"
            
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT html_content FROM generated_pages WHERE page_name = ?", (page_name,))
            row = cursor.fetchone()
            conn.close()
            if row:
                from flask import Response
                return Response(row[0], mimetype='text/html')
        except Exception as e:
            app.logger.error(f"Error serving {page_name} from database: {e}")

    return send_from_directory('static/projects', path)

@app.route('/api/bridge', methods=['POST'])
def bridge():
    data = request.json
    mission = data.get('mission')
    user_id = data.get('user_id', 'telegram_user')
    engine.generate_project(mission, user_id=user_id)
    import time
    return jsonify({"status": "success", "url": f"/static/projects/index.html?t={int(time.time())}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
