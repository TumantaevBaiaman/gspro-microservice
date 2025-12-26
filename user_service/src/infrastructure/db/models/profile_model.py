import datetime

from sqlalchemy import Column, String, ForeignKey, DateTime, Enum, Date
from sqlalchemy.dialects.postgresql import UUID

from src.core.database import Base
from src.domain.enums import City, Industry, ExperienceLevel


class UserProfileModel(Base):
    __tablename__ = "user_profiles"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )
    avatar_image_id = Column(
        UUID(as_uuid=True),
        ForeignKey("user_images.id", ondelete="SET NULL"),
        nullable=True,
    )
    phone_number = Column(String(20), nullable=True)

    full_name = Column(String(255), nullable=True)
    bio = Column(String, nullable=True)

    date_of_birth = Column(
        Date,
        nullable=True
    )

    city = Column(
        Enum(City, name="city_enum"),
        nullable=True,
        default=City.bishkek
    )

    industry = Column(
        Enum(Industry, name="industry_enum"),
        nullable=True
    )
    experience_level = Column(
        Enum(ExperienceLevel, name="experience_level_enum"),
        nullable=True,
        default=ExperienceLevel.beginner
    )