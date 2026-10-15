from datetime import datetime
import os

from sqlalchemy import URL, BIGINT, TIMESTAMP, String
from sqlalchemy.orm import DeclarativeBase


def create_db_url_from_env() -> URL:
    """
    Retrieves environment variables (preferrably populated by .env) and generates a database URL usable by SQLAlchemy.

    Uses the following environment variables:
    POSTGRES_HOST
    POSTGRES_DB
    POSTGRES_USER
    POSTGRES_PASSWORD

    :return: sqlalchemy.URL Database location for SQLAlchemy configured through env.
    """
    return URL.create(
        "postgresql+psycopg",
        username=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        host=os.environ["POSTGRES_HOST"],
        port=int(os.environ["POSTGRES_PORT"]),
        database=os.environ["POSTGRES_DB"],
    )


class Base(DeclarativeBase):
    type_annotation_map = {
        datetime: TIMESTAMP(timezone=True),
        str: String(),
    }
