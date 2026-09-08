from fastapi import FastAPI

app = FastAPI(title="JLL - Learning Record Store")


@app.get("/health")
def health():
    return {"status": "ok"}
