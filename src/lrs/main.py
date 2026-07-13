from fastapi import FastAPI

app = FastAPI(title="LL - Learning Record Store")


@app.get("/health")
def health():
    return {"status": "ok"}
