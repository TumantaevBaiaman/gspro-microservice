from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class UserEducationEntity:
    id: UUID
    user_id: UUID

    institution: str
    degree: str | None

    start_year: int | None
    end_year: int | None

    created_at: datetime
