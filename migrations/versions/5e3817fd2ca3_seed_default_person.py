"""seed default person

Revision ID: 5e3817fd2ca3
Revises: ec3a0a74d7e6
Create Date: 2026-11-09 17:10:37.380588

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel  # noqa: F401  (autogenerate may emit sqlmodel types)


# revision identifiers, used by Alembic.
revision: str = '5e3817fd2ca3'
down_revision: Union[str, Sequence[str], None] = 'ec3a0a74d7e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


person = sa.table("person", sa.column("id", sa.Integer), sa.column("name", sa.String))


def upgrade() -> None:
    """Insert the default person."""
    op.bulk_insert(person, [{"name": "Matt"}])


def downgrade() -> None:
    """Remove the default person."""
    op.execute(person.delete().where(person.c.name == "Matt"))
