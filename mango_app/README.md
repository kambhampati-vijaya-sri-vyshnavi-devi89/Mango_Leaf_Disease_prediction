# 🌿 MangoScan — Advanced Django Disease Classifier

## New Features in This Version

- 📊 **Scan History** — every scan is saved to SQLite database with full search & filter
- 💬 **Feedback System** — rate each diagnosis (1-5 stars), mark if correct, suggest correct disease
- 📄 **Professional Report** — download Word (.docx) report with full disease info, treatment, and confidence scores
- 🌱 **Disease Knowledge Base** — detailed info on all 8 diseases: symptoms, causes, treatment, prevention, organic options
- 🚫 **Spread Control** — specific steps to stop each disease from spreading to other trees
- 🗃️ **Database** — SQLite database stores all scans, predictions, and feedback

---

## 📁 Project Structure

```
mango_app/
├── manage.py
├── requirements.txt
├── mangoscan.db               ← created automatically after migrations
├── mango_leaf_model.keras     ← PLACE YOUR MODEL HERE
├── mango_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── classifier/
│   ├── models.py              ← ScanHistory + Feedback database models
│   ├── views.py               ← All endpoints
│   ├── ml.py                  ← TensorFlow inference
│   ├── disease_data.py        ← Full disease knowledge base
│   ├── report.py              ← Word document report generator
│   └── urls.py
├── templates/
│   └── classifier/
│       ├── index.html         ← Main scanner page
│       ├── history.html       ← Scan history with search/filter
│       └── detail.html        ← Individual scan detail + feedback
└── media/
    └── uploads/               ← Uploaded leaf images stored here
```

---

## 🚀 Setup (3 Steps)

### 1. Place your model file
```
mango_app/mango_leaf_model.keras
```

### 2. Install dependencies
```bash
cd mango_app
pip install -r requirements.txt
```

### 3. Run migrations & start server
```bash
python manage.py makemigrations classifier
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000/**

---

## 🌐 Pages

| URL | Description |
|-----|-------------|
| `/` | Main scanner — upload & analyze |
| `/history/` | All scan history with search/filter |
| `/scan/<id>/` | Detailed view for a specific scan |
| `/scan/<id>/report/` | Download Word report |
| `/scan/<id>/feedback/` | Submit feedback (POST) |
| `/api/stats/` | JSON stats API |

---

## ⚠️ Important: Class Names

Edit `DEFAULT_CLASS_NAMES` in `classifier/ml.py` to match your training folder order (alphabetical):
```python
DEFAULT_CLASS_NAMES = [
    'Anthracnose', 'Bacterial Canker', 'Cutting Weevil', 'Die Back',
    'Gall Midge', 'Healthy', 'Powdery Mildew', 'Sooty Mould',
]
```

---

## 🏭 Production

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
