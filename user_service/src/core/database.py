import datetime
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime, Boolean


class BaseMixin:
    id = Column(
        UUID(as_uuid=True),
        default=uuid.uuid4,
        primary_key=True,
        index=True
    )

    created_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        nullable=False
    )

    is_active = Column(Boolean, default=True, nullable=False)


Base = declarative_base(cls=BaseMixin)

