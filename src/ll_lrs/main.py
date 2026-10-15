from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from starlette import status
from starlette.requests import Request

from ll_lrs.database import create_db_url_from_env


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = create_engine(create_db_url_from_env())
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
