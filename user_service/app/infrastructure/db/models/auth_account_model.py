import datetime

from sqlalchemy import Column, String, Boolean, Enum, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base
from app.domain.enums import AuthProvider


class AuthAccountModel(Base):
    __tablename__ = "auth_accounts"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    provider = Column(
        Enum(AuthProvider, name="auth_provider_enum"),
        nullable=False,
    )

    identifier = Column(
        String(255),
        nullable=False,
    )

    password_hash = Column(
        String(255),
        nullable=True,
    )

    verified = Column(Boolean, default=False, nullable=False)

    last_login = Column(
        String,
        nullable=True,
    )

    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )