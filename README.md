#  API Test Automation Framework

[![API Tests](https://github.com/Vianney97/api-test-framework/actions/workflows/tests.yml/badge.svg)](https://github.com/Vianney97/api-test-framework/actions/workflows/tests.yml)

Framework de tests automatisés pour API REST, construit avec **Python + Pytest**.  
Il met en avant les bonnes pratiques QA Automation :

- ✅ Tests fonctionnels (GET, POST, PUT, DELETE)
- ✅ Data-driven testing (JSON externe)
- ✅ Validation de schémas JSON (jsonschema)
- ✅ Reporting (pytest-html)
- ✅ CI/CD avec GitHub Actions

---

## Installation

Cloner le repo et installer les dépendances :

```bash
git clone https://github.com/Vianney97/api-test-framework.git
cd api-test-framework
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

## Exécution des tests
pytest

## Exécution avec rapport HTML
pytest --html=report.html --self-contained-html

📊 Reporting

pytest-html → génère un rapport HTML autonome (report.html)

GitHub Actions → génère le rapport et l’archive comme artifact téléchargeable
