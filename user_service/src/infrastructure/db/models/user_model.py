from sqlalchemy import func, String, Enum

from sqlalchemy import Column, DateTime
from src.core.database import Base
from src.domain.enums.user_role import UserRole


class UserModel(Base):
    __tablename__ = "users"

    email = Column(
        String(255),
        unique=True,
        nullable=True,
        index=True,
    )

    role = Column(
        Enum(UserRole, name="user_role_enum"),
        nullable=False,
        server_default=UserRole.user.value,
    )

