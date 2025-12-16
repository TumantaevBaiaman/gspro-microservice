"""move updated_at to auth account

Revision ID: dd0059a09dcc
Revises: 658d93baf47e
Create Date: 2025-12-16 17:55:14.230558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd0059a09dcc'
down_revision: Union[str, Sequence[str], None] = '658d93baf47e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
