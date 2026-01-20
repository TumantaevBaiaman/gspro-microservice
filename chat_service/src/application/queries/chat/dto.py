from dataclasses import dataclass
from typing import Iterable, Optional

from src.domain.enums.chat_type_enum import ChatTypeEnum


@dataclass(slots=True)
class GetChatByIdDTO:
    chat_id: str


@dataclass(slots=True)
class GetChatByUniqueKeyDTO:
    unique_key: str


@dataclass(slots=True)
class ListChatsByIdsDTO:
    chat_ids: Iterable[str]


@dataclass(slots=True)
class ListUserChatsDTO:
    user_id: str
    chat_type: Optional[ChatTypeEnum] = None
    limit: int = 50
    offset: int = 0
