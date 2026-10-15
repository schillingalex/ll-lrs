from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.exc import OperationalError

from ll_lrs.main import app


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("POSTGRES_HOST", "db")
    monkeypatch.setenv("POSTGRES_DB", "ll")
    monkeypatch.setenv("POSTGRES_USER", "user")
    monkeypatch.setenv("POSTGRES_PASSWORD", "pw")

    with TestClient(app) as test_client:
        yield test_client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ready(client):
    fake_engine = MagicMock()
    fake_connection = fake_engine.connect.return_value.__enter__.return_value
    client.app.state.db = fake_engine

    response = client.get("/ready")

    assert response.status_code == 200
    fake_connection.execute.assert_called_once()


def test_ready_db_fail(client):
    fake_engine = MagicMock()
    fake_connection = fake_engine.connect.return_value.__enter__.return_value
    fake_connection.execute.side_effect = OperationalError(
        "SELECT 1", {}, Exception("Connection failed")
    )
    client.app.state.db = fake_engine

    response = client.get("/ready")

    assert response.status_code == 503
    assert response.json() == {"detail": "Database unavailable"}
