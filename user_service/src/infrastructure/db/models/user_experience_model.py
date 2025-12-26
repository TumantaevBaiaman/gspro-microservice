import datetime

from sqlalchemy import Column, String, ForeignKey, Date, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID

from src.core.database import Base


class UserExperienceModel(Base):
    __tablename__ = "user_experiences"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    company = Column(String(255), nullable=False)
    position = Column(String(255), nullable=False)

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)

    description = Column(Text, nullable=True)

