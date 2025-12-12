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
