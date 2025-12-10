from dataclasses import dataclass
from uuid import UUID


@dataclass
class ProfileEntity:
    user_id: UUID
    full_name: str | None
    bio: str | None
    city: str | None
    industry: str | None
    experience_level: str | None

    @staticmethod
    def create(
        user_id: UUID,
        full_name: str | None = None,
        bio: str | None = None,
        city: str | None = None,
        industry: str | None = None,
        experience_level: str | None = None,
    ) -> "ProfileEntity":
        return ProfileEntity(
            user_id=user_id,
            full_name=full_name,
            bio=bio,
            city=city,
            industry=industry,
            experience_level=experience_level,
        )