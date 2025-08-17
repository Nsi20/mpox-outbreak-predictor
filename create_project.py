import os
from pathlib import Path
import textwrap

# === CONFIG ===
BASE_DIR = Path.cwd()  # Current directory

# === FOLDERS ===
folders = [
    "data/raw",
    "data/processed",
    "data/external",
    "data/interim",
    "notebooks/eda",
    "notebooks/modeling",
    "notebooks/experiments",
    "src/app",
    "src/api",
    "src/data",
    "src/features",
    "src/models",
    "src/visualization",
    "src/utils",
    "docs",
    "reports/figures",
    "tests"
]

# === FILE WRITER ===
def write_file(path, content=""):
    path = BASE_DIR / path
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(textwrap.dedent(content).lstrip())

# === CREATE FOLDERS & .gitkeep ===
for folder in folders:
    (BASE_DIR / folder).mkdir(parents=True, exist_ok=True)
    write_file(f"{folder}/.gitkeep", "")

# === BASIC FILES ===
write_file("README.md", "# Mpox Outbreak Predictor\n\nEarly warning and risk prediction for Mpox outbreaks in Africa.")
write_file(".gitignore", """
__pycache__/
*.pyc
*.pyo
*.pyd
.venv/
env/
venv/
.ipynb_checkpoints/
data/raw/*
data/processed/*
data/external/*
data/interim/*
!data/**/.gitkeep
reports/figures/*
!reports/**/.gitkeep
.env
""")
write_file("requirements.txt", """
pandas
numpy
scikit-learn
xgboost
matplotlib
plotly
geopandas
folium
streamlit
shap
fastapi
uvicorn
python-dotenv
requests
""")
write_file(".env.example", "# Example environment variables\n# MAPBOX_TOKEN=your_mapbox_token_here")

# === STREAMLIT APP STUB ===
write_file("src/app/streamlit_app.py", """
import streamlit as st
st.set_page_config(page_title="Mpox Outbreak Predictor", layout="wide")
st.title("🧭 Mpox Outbreak Predictor")
st.write("This is the dashboard scaffold. Data visualizations will appear here.")
""")

# === FASTAPI API STUB ===
write_file("src/api/main.py", """
from fastapi import FastAPI
app = FastAPI(title="Mpox Outbreak Predictor API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}
""")

# === TEST STUB ===
write_file("tests/test_smoke.py", "def test_smoke():\n    assert 2 + 2 == 4\n")

print(f"✅ Project structure created successfully at {BASE_DIR.resolve()}")
