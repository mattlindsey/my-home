"""SQLite access via SQLModel (Pydantic models backed by SQLAlchemy).

The schema is managed by Alembic migrations (see ``migrations/``), not created
at app startup. Run ``uv run alembic upgrade head`` to create/update the DB.
"""

import os
from collections.abc import Iterator

from sqlmodel import Field, Session, SQLModel, create_engine

DATABASE_URL = os.environ.get("MY_HOME_DATABASE_URL", "sqlite:///my_home.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


class Person(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)


def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session
