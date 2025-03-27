"""Agregar el usuario por defecto

Revision ID: 6d059d816fbc
Revises: 56a8233da4f1
Create Date: 2025-03-27 08:12:41.365706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d059d816fbc'
down_revision: Union[str, None] = '56a8233da4f1'
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
    op.execute("INSERT INTO usuario (name, username, email, password, active) VALUES('Administrador del sistema', 'admin', 'admin@email.com', '123456', 1);")


def downgrade_engine1() -> None:
    """Downgrade engine1 schema."""
    op.execute("DELETE FROM usuario WHERE username= 'admin';")


def upgrade_engine2() -> None:
    """Upgrade engine2 schema."""
    pass


def downgrade_engine2() -> None:
    """Downgrade engine2 schema."""
    pass


def upgrade_engine3() -> None:
    """Upgrade engine3 schema."""
    pass


def downgrade_engine3() -> None:
    """Downgrade engine3 schema."""
    pass

