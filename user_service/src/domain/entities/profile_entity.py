from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass
class ProfileEntity:
    user_id: UUID
    full_name: str | None
    bio: str | None
    date_of_birth: date | None
    city: str | None
    industry: str | None
    experience_level: str | None
