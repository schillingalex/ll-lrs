import os

from sqlalchemy import URL


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
        database=os.environ["POSTGRES_DB"],
    )
