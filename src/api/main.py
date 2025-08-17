from fastapi import FastAPI
app = FastAPI(title="Mpox Outbreak Predictor API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}
