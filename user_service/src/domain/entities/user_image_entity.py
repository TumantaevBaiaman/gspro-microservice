from dataclasses import dataclass
from uuid import UUID
from typing import Optional

from src.domain.enums import UserImageType


@dataclass
class UserImageEntity:
    id: Optional[UUID]
    user_id: UUID
    type: UserImageType
    original_url: str
    thumb_small_url: Optional[str]
    thumb_medium_url: Optional[str]

    @staticmethod
    def create_avatar(
        *,
        user_id: UUID,
        original_url: str,
        thumb_small_url: Optional[str],
        thumb_medium_url: Optional[str],
    ) -> "UserImageEntity":
        return UserImageEntity(
            id=None,
            user_id=user_id,
            type=UserImageType.avatar,
            original_url=original_url,
            thumb_small_url=thumb_small_url,
            thumb_medium_url=thumb_medium_url,
        )
