const layers = {
  dados: {
    name: 'DADOS',
    title: 'Matriz de dados operacionais',
    text: 'Monitoramento conceitual de integridade, latência e sincronização de sistemas aeronáuticos em tempo real.',
    metrics: ['99.7%', '11 ms', '32.4k ft']
  },
  analise: {
    name: 'ANÁLISE',
    title: 'Análise de comportamento estrutural',
    text: 'Mapeamento de vibração, carga, estabilidade e variação térmica em seções críticas.',
    metrics: ['96.8%', '14 ms', '28.9k ft']
  },
  previsao: {
    name: 'PREVISÃO',
    title: 'Previsão de resposta de missão',
    text: 'Simulação de cenários de risco, manutenção e rotas futuras sob parâmetros climáticos.',
    metrics: ['92.4%', '18 ms', '35.1k ft']
  },
  quantico: {
    name: 'QUÂNTICO',
    title: 'Camada quântica operacional',
    text: 'Sincronização adaptativa, aprendizagem contínua e detecção antecipada de resposta autônoma.',
    metrics: ['99.9%', '9 ms', '41.0k ft']
  }
};

const setLayer = (key) => {
  const layer = layers[key];
  if (!layer) return;

  document.getElementById('layerBadge').textContent = layer.name;
  document.getElementById('layerTitle').textContent = layer.title;
  document.getElementById('layerText').textContent = layer.text;
  document.getElementById('metric1').textContent = layer.metrics[0];
  document.getElementById('metric2').textContent = layer.metrics[1];
  document.getElementById('metric3').textContent = layer.metrics[2];

  document.querySelectorAll('.nav-item').forEach((button) => {
    button.classList.toggle('active', button.dataset.layer === key);
  });
};

const refreshStats = () => {
  document.getElementById('missions').textContent = 18 + Math.floor(Math.random() * 18);
  document.getElementById('risk').textContent = Math.random() > 0.72 ? 'MODERADO' : 'BAIXO';
  document.getElementById('fuel').textContent = `${Math.floor(45 + Math.random() * 55)}%`;
  document.getElementById('signalValue').textContent = (90 + Math.random() * 9).toFixed(1);
  document.getElementById('statusText').textContent = Math.random() > 0.3 ? 'ONLINE' : 'SYNC';
};

const buttons = document.querySelectorAll('.nav-item');
buttons.forEach((button) => {
  button.addEventListener('click', () => setLayer(button.dataset.layer));
});

document.getElementById('generateReport').addEventListener('click', () => {
  const btn = document.getElementById('generateReport');
  btn.textContent = 'RELATÓRIO GERADO';
  document.getElementById('statusText').textContent = 'SYNC';
  refreshStats();

  setTimeout(() => {
    btn.textContent = 'GERAR RELATÓRIO';
    document.getElementById('statusText').textContent = 'ONLINE';
  }, 1200);
});

setLayer('dados');
refreshStats();
