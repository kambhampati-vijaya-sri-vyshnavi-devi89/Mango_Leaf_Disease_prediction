<div align="center">

<img src="https://img.shields.io/badge/🥭-MangoScan-ff6b35?style=for-the-badge&labelColor=1a1a2e&color=ff6b35" height="40"/>

# 🌿 MangoScan
### *AI-Powered Mango Leaf Disease Detection System*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=flat-square&logo=django&logoColor=white)](https://djangoproject.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

> Upload a mango leaf → Get instant AI diagnosis → Download professional report

---

</div>

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🔍 **AI Disease Detection** | Deep learning model classifies 8 mango diseases with confidence scores |
| 📊 **Scan History** | Every scan saved to SQLite with full search & filter support |
| 💬 **Feedback System** | Rate diagnoses (1–5 stars), mark accuracy, suggest corrections |
| 📄 **Word Reports** | Download `.docx` reports with disease info, treatment & confidence |
| 🌱 **Disease Knowledge Base** | Symptoms, causes, treatment & prevention for all 8 diseases |
| 🚫 **Spread Control** | Specific steps to stop disease spreading to nearby trees |

---

## 🦠 Supported Diseases

```
Anthracnose  •  Bacterial Canker  •  Cutting Weevil  •  Die Back
Gall Midge   •  Healthy           •  Powdery Mildew  •  Sooty Mould
```

---

## 📁 Project Structure

```
mango_app/
├── 📄 manage.py
├── 📋 requirements.txt
├── 🗃️  mangoscan.db               ← created automatically after migrations
├── 🧠 mango_leaf_model.keras      ← PLACE YOUR MODEL HERE
│
├── mango_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── classifier/
│   ├── models.py              ← ScanHistory + Feedback database models
│   ├── views.py               ← All endpoints
│   ├── ml.py                  ← TensorFlow inference engine
│   ├── disease_data.py        ← Full disease knowledge base
│   ├── report.py              ← Word document report generator
│   └── urls.py
│
├── templates/
│   └── classifier/
│       ├── index.html         ← Main scanner page
│       ├── history.html       ← Scan history with search/filter
│       └── detail.html        ← Individual scan detail + feedback
│
└── media/
    └── uploads/               ← Uploaded leaf images stored here
```

---

## 🚀 Quick Start

### Step 1 — Place Your Model

```
mango_app/mango_leaf_model.keras
```

### Step 2 — Navigate & Install Dependencies

```bash
cd mango_app
pip install -r requirements.txt
```

### Step 3 — Migrate & Launch

```bash
python manage.py makemigrations classifier
python manage.py migrate
python manage.py runserver
```

### 🌐 Open in Browser

```
http://127.0.0.1:8000/
```

---

## 🗺️ Available Pages

| Route | Page | Description |
|-------|------|-------------|
| `/` | 🏠 Home | Upload leaf & get instant diagnosis |
| `/history/` | 📋 History | All scans with search & filter |
| `/scan/<id>/` | 🔎 Detail | Full scan details & feedback form |
| `/scan/<id>/report/` | 📄 Report | Download Word (.docx) report |
| `/scan/<id>/feedback/` | 💬 Feedback | Submit rating & correction (POST) |
| `/api/stats/` | 📊 Stats API | JSON stats endpoint |

---

## ⚠️ Important: Class Name Configuration

Edit `DEFAULT_CLASS_NAMES` in `classifier/ml.py` to match your model's training folder order **(must be alphabetical)**:

```python
DEFAULT_CLASS_NAMES = [
    'Anthracnose',
    'Bacterial Canker',
    'Cutting Weevil',
    'Die Back',
    'Gall Midge',
    'Healthy',
    'Powdery Mildew',
    'Sooty Mould',
]
```

---

## 🏭 Production Deployment

```python
# settings.py
DEBUG = False
SECRET_KEY = 'your-secure-random-key-here'
ALLOWED_HOSTS = ['your-domain.com']
```

```bash
python manage.py collectstatic
gunicorn mango_project.wsgi:application
```

---

## 🤝 Contributing

Contributions are welcome! Please open an issue first for major changes.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ to help Mango Farmers 🌾

**MangoScan** — *Protecting Mango Crops with AI*

</div>
