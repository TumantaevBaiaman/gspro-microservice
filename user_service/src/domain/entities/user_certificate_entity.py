from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class UserCertificateEntity:
    id: UUID
    user_id: UUID

    title: str
    issuer: str | None
    issued_at: datetime | None
    link: str | None

    created_at: datetime
