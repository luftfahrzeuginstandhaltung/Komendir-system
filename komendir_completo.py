from pathlib import Path
import json
from datetime import date

DATA_FILE = Path('komendir_dados.json')
def load():
    return json.loads(DATA_FILE.read_text(encoding='utf-8')) if DATA_FILE.exists() else {'empresa':'Komendir','dataAtual':str(date.today()),'itens':[]}
def save(data): DATA_FILE.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if __name__ == '__main__':
    data=load(); print(f"{data.get('empresa','Komendir')}: {len(data.get('itens',[]))} registros")
