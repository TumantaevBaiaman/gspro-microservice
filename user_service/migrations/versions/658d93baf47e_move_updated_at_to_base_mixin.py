"""move updated_at to base mixin

Revision ID: 658d93baf47e
Revises: b370503641a4
Create Date: 2025-12-16 17:54:24.304849

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '658d93baf47e'
down_revision: Union[str, Sequence[str], None] = 'b370503641a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
