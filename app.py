from flask import Flask, render_template, request, jsonify, send_from_directory
from animus_engine import AnimusEngine
import os

app = Flask(__name__)
engine = AnimusEngine(output_dir="static/projects")

# AETHER_COMMAND Dashboard Template
DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AETHER_COMMAND | Nerve Center</title>
    <style>
        :root { --accent: #00ffcc; --bg: #050505; }
        body { background: var(--bg); color: white; font-family: 'Space Mono', monospace; margin: 0; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }
        .dashboard { width: 800px; padding: 4rem; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); backdrop-filter: blur(40px); border-radius: 24px; text-align: center; }
        h1 { font-size: 0.8rem; letter-spacing: 0.5em; opacity: 0.5; margin-bottom: 3rem; color: var(--accent); }
        .prompt-box { position: relative; margin-top: 2rem; }
        input { width: 100%; background: transparent; border: none; border-bottom: 1px solid rgba(255,255,255,0.1); color: white; font-size: 1.5rem; font-family: inherit; padding: 1rem 0; outline: none; transition: border 0.4s; }
        input:focus { border-bottom: 1px solid var(--accent); }
        .status { margin-top: 2rem; font-size: 0.7rem; opacity: 0.4; }
        .btn-ignite { margin-top: 3rem; background: white; color: black; border: none; padding: 1rem 3rem; border-radius: 50px; font-weight: 700; cursor: pointer; transition: transform 0.3s; }
        .btn-ignite:hover { transform: scale(1.05); box-shadow: 0 0 30px var(--accent); }
        #results { margin-top: 2rem; display: none; }
        a { color: var(--accent); text-decoration: none; font-size: 0.8rem; }
    </style>
</head>
<body>
    <div class="dashboard">
        <h1>AETHER_COMMAND v1.0</h1>
        <div class="prompt-box">
            <input type="text" id="mission" placeholder="WHAT ARE WE BUILDING TODAY?" autofocus>
        </div>
        <button class="btn-ignite" onclick="ignite()">EXECUTE_COMMAND</button>
        <div class="status" id="status">NEURAL_CORE: STANDBY</div>
        <div id="results">
            <p>PROJECT_ARCHITECTED: <a id="view-link" href="#" target="_blank">VIEW_LIVE_DEPLOYMENT</a></p>
        </div>
    </div>

    <script>
        async function ignite() {
            const mission = document.getElementById('mission').value;
            const status = document.getElementById('status');
            const results = document.getElementById('results');
            
            if (!mission) return;
            
            status.innerText = "SOUL_GENERATION: IN_PROGRESS...";
            const response = await fetch('/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ mission: mission })
            });
            
            const data = await response.json();
            status.innerText = "PROJECT_AUDIT: PASSED";
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
    data = request.json
    mission = data.get('mission')
    # Use index.html as the entry point
    engine.generate_project(mission)
    return jsonify({"status": "success", "url": "/static/projects/index.html"})

@app.route('/static/projects/<path:path>')
def serve_project(path):
    return send_from_directory('static/projects', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
