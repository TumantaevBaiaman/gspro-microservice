"""add users and auth accounts

Revision ID: ae5baa1f354e
Revises: dd0059a09dcc
Create Date: 2025-12-16 18:02:32.754973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae5baa1f354e'
down_revision: Union[str, Sequence[str], None] = 'dd0059a09dcc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
