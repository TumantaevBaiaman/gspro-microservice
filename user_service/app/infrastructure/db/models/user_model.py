import datetime

from sqlalchemy import Column, DateTime
from app.core.database import Base


class UserModel(Base):
    __tablename__ = "users"

    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )
