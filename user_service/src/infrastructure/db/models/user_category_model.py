
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from src.core.database import Base


class UserCategoriesModel(Base):
    __tablename__ = "user_categories"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )

    category_id = Column(
        String(64),
        nullable=False,
        primary_key=True,
    )