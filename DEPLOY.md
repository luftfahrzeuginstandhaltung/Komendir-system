# LexKomendirAirCraft Deployment Guide

## 1) Local execution

### macOS / Linux
```bash
chmod +x start.sh
./start.sh
```

### Windows
```bat
start.bat
```

Then open:
```text
http://localhost:5000
```

## 2) GitHub Pages publication

1. Open the GitHub repository.
2. Go to Settings.
3. Open Pages.
4. Select:
   - Source: Deploy from a branch
   - Branch: main
   - Folder: /root
5. Save.

The site should become available at:
```text
https://luftfahrzeuginstandhaltung.github.io/Komendir-system/
```

## 3) Web app (Flask)

The project also includes a Flask app for API access.

Routes:
- `/` -> main landing page
- `/index_holograma.html` -> second holographic concept page
- `/api/records` -> JSON records
- `/api/summary` -> summary statistics

## 4) Requirements

```bash
pip install -r requirements.txt
pip install matplotlib
```

## 5) Project structure

```text
.
├── app.py
├── README.md
├── requirements.txt
├── start.sh
├── start.bat
├── index.html
├── index_holograma.html
├── komendir_completo.py
├── komendir_dados.json
├── assets/
│   ├── script.js
│   └── styles.css
└── .gitignore
```
