from sqlalchemy import (
    Column,
    String,
    Enum,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID

from src.core.database import Base
from src.domain.enums import UserImageType


class UserImageModel(Base):
    __tablename__ = "user_images"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    type = Column(
        Enum(UserImageType, name="user_image_type_enum"),
        nullable=False,
    )

    original_url = Column(String, nullable=False)
    thumb_small_url = Column(String, nullable=True)
    thumb_medium_url = Column(String, nullable=True)