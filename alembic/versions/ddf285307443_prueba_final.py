"""Prueba final

Revision ID: ddf285307443
Revises: 0c79c46d09e8
Create Date: 2025-03-27 09:22:27.311998

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ddf285307443'
down_revision: Union[str, None] = '0c79c46d09e8'
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
    op.execute("DELETE FROM usuario WHERE username= 'admin';")
    pass


def downgrade_engine1() -> None:
    """Downgrade engine1 schema."""
    op.execute("INSERT INTO usuario (name, username, email, password, active) VALUES('Administrador del sistema', 'admin', 'admin@email.com', '123456', 0);")
    pass

