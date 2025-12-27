

import datetime

from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID

from src.core.database import Base


class UserCertificateModel(Base):
    __tablename__ = "user_certificates"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    title = Column(String(255), nullable=False)
    issuer = Column(String(255), nullable=True)

    issued_at = Column(DateTime, nullable=True)

    link = Column(String, nullable=True)
