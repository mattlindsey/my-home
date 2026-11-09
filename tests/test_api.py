from collections.abc import Iterator
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlmodel import create_engine

from my_home import db
from my_home.api import app

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[TestClient]:
    """Build a fresh SQLite DB by running the real Alembic migrations."""
    url = f"sqlite:///{tmp_path / 'test.db'}"
    monkeypatch.setattr(db, "DATABASE_URL", url)
    monkeypatch.setattr(
        db, "engine", create_engine(url, connect_args={"check_same_thread": False})
    )

    cfg = Config(str(ROOT / "alembic.ini"))
    cfg.set_main_option("script_location", str(ROOT / "migrations"))
    command.upgrade(cfg, "head")

    with TestClient(app) as c:
        yield c


def test_hi_returns_greeting_from_db(client: TestClient) -> None:
    resp = client.get("/api/hi")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Hi Matt!"}
