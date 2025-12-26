from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID

from src.core.database import Base


class UserEducationModel(Base):
    __tablename__ = "user_educations"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    institution = Column(String(255), nullable=False)
    degree = Column(String(255), nullable=True)

    start_year = Column(Integer, nullable=True)
    end_year = Column(Integer, nullable=True)
