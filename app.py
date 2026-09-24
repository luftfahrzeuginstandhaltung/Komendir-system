from flask import Flask, jsonify, send_from_directory
from pathlib import Path
import json

app = Flask(__name__, static_folder='.')
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / 'komendir_dados.json'

def load_data():
    if not DATA_FILE.exists():
        default = {'empresa': 'LexKomendirAircraft', 'dataAtual': '2026-09-24', 'itens': []}
        DATA_FILE.write_text(json.dumps(default, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        return default
    return json.loads(DATA_FILE.read_text(encoding='utf-8'))

@app.route('/')
def home(): return send_from_directory(BASE_DIR, 'index.html')

@app.route('/index_holograma.html')
def holograma(): return send_from_directory(BASE_DIR, 'index_holograma.html')

@app.route('/investidor.html')
def investidor(): return send_from_directory(BASE_DIR, 'investidor.html')

@app.route('/assets/<path:filename>')
def assets(filename): return send_from_directory(BASE_DIR / 'assets', filename)

@app.route('/api/records')
def records(): return jsonify(load_data().get('itens', []))

@app.route('/api/summary')
def summary():
    data = load_data(); items = data.get('itens', [])
    return jsonify({'empresa': data.get('empresa', 'LexKomendirAircraft'), 'total': len(items), 'valor_total': sum(float(x.get('valor', 0)) for x in items)})

if __name__ == '__main__': app.run(debug=True, host='0.0.0.0', port=5000)
