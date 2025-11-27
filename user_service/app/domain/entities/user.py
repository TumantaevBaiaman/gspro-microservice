from dataclasses import dataclass
from uuid import UUID, uuid4
from datetime import datetime


@dataclass
class User:
    id: UUID
    created_at: datetime

    @staticmethod
    def create():
        return User(
            id=uuid4(),
            created_at=datetime.utcnow(),
        )
