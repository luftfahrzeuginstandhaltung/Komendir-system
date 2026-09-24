from flask import Flask, jsonify, send_from_directory
from pathlib import Path
import json

app = Flask(__name__, static_folder='.')
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / 'komendir_dados.json'


def load_data():
    if not DATA_FILE.exists():
        default = {
            'empresa': 'KOM-AK-X1-ALPHA',
            'dataAtual': '2026-09-24',
            'itens': [
                {'id': 'K-0001', 'nome': 'Propulsão', 'cliente': 'Aeronáutica Nacional', 'status': 'estável', 'valor': 9800, 'data': '2026-09-24'},
                {'id': 'K-0002', 'nome': 'Estrutura', 'cliente': 'Operação Aérea', 'status': 'verificado', 'valor': 7450, 'data': '2026-09-24'},
                {'id': 'K-0003', 'nome': 'Sistema de sinal', 'cliente': 'Controle de Tráfego', 'status': 'sincronizado', 'valor': 11240, 'data': '2026-09-24'}
            ]
        }
        DATA_FILE.write_text(json.dumps(default, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        return default
    return json.loads(DATA_FILE.read_text(encoding='utf-8'))


@app.route('/')
def home():
    return send_from_directory(BASE_DIR, 'index.html')


@app.route('/index_holograma.html')
def holograma():
    return send_from_directory(BASE_DIR, 'index_holograma.html')


@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory(BASE_DIR / 'assets', filename)


@app.route('/api/records')
def records():
    return jsonify(load_data().get('itens', []))


@app.route('/api/summary')
def summary():
    data = load_data()
    itens = data.get('itens', [])
    return jsonify({
        'empresa': data.get('empresa', 'KOM-AK-X1-ALPHA'),
        'total': len(itens),
        'valor_total': sum(float(item.get('valor', 0)) for item in itens),
        'status': {
            'estável': sum(1 for item in itens if item.get('status') == 'estável'),
            'verificado': sum(1 for item in itens if item.get('status') == 'verificado'),
            'sincronizado': sum(1 for item in itens if item.get('status') == 'sincronizado')
        }
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
