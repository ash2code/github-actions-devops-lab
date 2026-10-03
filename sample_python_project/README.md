# Flask App for GitHub Actions Practice

This project contains a small Flask application and unit tests for GitHub Actions practice.

## Project structure

- `src/app.py` - Flask application
- `tests/test_calculator.py` - basic Flask API tests
- `requirements.txt` - app and test dependencies
- `.github/workflows/python-tests.yml` - CI workflow
- `.gitignore` - ignores Python artifacts.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src pytest -q
```

## Run the app

```bash
PYTHONPATH=src python src/app.py
```

Then open:

- `http://localhost:5000/`
- `http://localhost:5000/health`
- `http://localhost:5000/add?a=5&b=7`

The app exposes a simple health check and integer addition endpoint..
