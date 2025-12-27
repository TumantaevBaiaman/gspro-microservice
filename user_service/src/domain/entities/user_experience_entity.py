from dataclasses import dataclass
from datetime import date, datetime
from uuid import UUID


@dataclass(slots=True)
class UserExperienceEntity:
    id: UUID
    user_id: UUID

    company: str
    position: str

    start_date: date
    end_date: date | None

    description: str | None

    created_at: datetime
