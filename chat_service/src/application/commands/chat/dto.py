from dataclasses import dataclass
from typing import Optional

from src.domain.enums.chat_type_enum import ChatTypeEnum


@dataclass(slots=True)
class GetOrCreateChatDTO:
    type: ChatTypeEnum
    unique_key: str
    course_id: Optional[str] = None



@dataclass(slots=True)
class ArchiveChatDTO:
    chat_id: str


@dataclass(slots=True)
class UnarchiveChatDTO:
    chat_id: str
