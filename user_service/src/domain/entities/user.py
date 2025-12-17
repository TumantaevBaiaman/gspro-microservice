import datetime

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class User:
    id: UUID
    email: str
    is_active: bool

    @staticmethod
    def create(email: str) -> "User":
        if not email:
            raise ValueError("Email is required")

        return User(
            id=uuid4(),
            email=email,
            is_active=True,
        )
