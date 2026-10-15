from contextlib import asynccontextmanager
import os

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, URL, text
from sqlalchemy.exc import OperationalError
from starlette import status
from starlette.requests import Request


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine_url = URL.create(
        "postgresql+psycopg",
        username=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        host=os.environ["POSTGRES_HOST"],
        database=os.environ["POSTGRES_DB"],
    )
    db = create_engine(engine_url)
    app.state.db = db

    yield

    db.dispose()


app = FastAPI(
    title="JLL - Learning Record Store",
    lifespan=lifespan,
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready(request: Request):
    try:
        with request.app.state.db.connect() as connection:
            connection.execute(text("SELECT 1"))
    except OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database unavailable"
        ) from e

    return {"status": "ok"}
