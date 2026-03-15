# API Test Automation Framework

[![API Tests](https://github.com/Vianney97/api-test-framework/actions/workflows/tests.yml/badge.svg)](https://github.com/Vianney97/api-test-framework/actions/workflows/tests.yml)

Framework de tests automatisés pour API REST, construit avec **Python + Pytest**.  
Il illustre les bonnes pratiques QA Automation appliquées à une API publique ([JSONPlaceholder](https://jsonplaceholder.typicode.com)).

## Fonctionnalités

| Fonctionnalité | Détail |
|---|---|
| ✅ Tests CRUD complets | GET, POST, PUT, DELETE |
| ✅ Data-driven testing | Cas de test chargés depuis des fichiers JSON |
| ✅ Validation de schémas | Vérification de la structure des réponses via `jsonschema` |
| ✅ Reporting HTML | Rapport autonome généré par `pytest-html` |
| ✅ Reporting Allure | Rapport interactif avec `allure-pytest` |
| ✅ CI/CD | Pipeline GitHub Actions automatique sur chaque push / PR |

---

## Structure du projet

```
api-test-framework/
├── .github/
│   └── workflows/
│       └── tests.yml        # Pipeline CI/CD GitHub Actions
├── data/
│   ├── posts.json           # Données de test pour les posts (data-driven)
│   └── users.json           # Données de test pour les utilisateurs
├── schemas/
│   ├── post_schema.json     # Schéma JSON attendu pour /posts
│   └── user_schema.json     # Schéma JSON attendu pour /users
├── tests/
│   ├── conftest.py          # Fixtures Pytest (client HTTP, chargeur JSON)
│   ├── test_posts.py        # Tests sur l'endpoint /posts
│   └── test_users.py        # Tests sur l'endpoint /users
├── utils/
│   └── api_client.py        # Client HTTP réutilisable (wrapper requests)
├── pytest.ini               # Configuration Pytest et marqueurs
└── requirements.txt         # Dépendances Python
```

---

## Prérequis

- Python 3.9+
- pip

---

## Installation

```bash
git clone https://github.com/Vianney97/api-test-framework.git
cd api-test-framework

# Créer et activer l'environnement virtuel
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

# Installer les dépendances
pip install -r requirements.txt
pip install pytest-html       # pour le rapport HTML (optionnel)
```

---

## Configuration

Par défaut, les tests ciblent `https://jsonplaceholder.typicode.com`.  
Vous pouvez pointer vers une autre API en définissant la variable d'environnement `BASE_URL` :

```bash
export BASE_URL=https://mon-api.example.com   # Linux / macOS
set BASE_URL=https://mon-api.example.com      # Windows
```

---

## Exécution des tests

### Tous les tests
```bash
pytest
```

### Uniquement les smoke tests
```bash
pytest -m smoke
```

### Uniquement les tests de contrat (validation de schéma)
```bash
pytest -m contract
```

### Avec rapport HTML
```bash
pytest --html=report.html --self-contained-html
```

### Avec rapport Allure
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## Marqueurs Pytest

| Marqueur | Description |
|---|---|
| `smoke` | Tests rapides de vérification de base |
| `contract` | Tests de validation de schéma JSON |

---

## 📊 Reporting

- **pytest-html** → génère un fichier `report.html` autonome consultable dans un navigateur.
- **Allure** → génère un rapport interactif avec détails des requêtes/réponses en cas d'échec.
- **GitHub Actions** → exécute les tests à chaque push/PR et archive le rapport HTML comme artifact téléchargeable.

---

## CI/CD

Le pipeline défini dans `.github/workflows/tests.yml` :

1. Installe Python 3.11 (version minimale requise : 3.9) et les dépendances.
2. Exécute l'ensemble des tests avec génération du rapport HTML.
3. Archive `report.html` comme artifact téléchargeable depuis l'onglet **Actions** de GitHub.
