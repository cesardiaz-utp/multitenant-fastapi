"""Inactivar el usuario admin

Revision ID: 0c79c46d09e8
Revises: 6d059d816fbc
Create Date: 2025-03-27 08:19:10.040893

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c79c46d09e8'
down_revision: Union[str, None] = '6d059d816fbc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    """Upgrade schema."""
    # globals()["upgrade_%s" % engine_name]()
    upgrade_engine1()


def downgrade(engine_name: str) -> None:
    """Downgrade schema."""
    # globals()["downgrade_%s" % engine_name]()
    downgrade_engine1()





def upgrade_engine1() -> None:
    """Upgrade engine1 schema."""
    op.execute("UPDATE usuario SET active = 0 WHERE username = 'admin';")
    pass


def downgrade_engine1() -> None:
    """Downgrade engine1 schema."""
    op.execute("UPDATE usuario SET active = 1 WHERE username = 'admin';")
    pass

