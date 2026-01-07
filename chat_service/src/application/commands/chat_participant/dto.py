from dataclasses import dataclass
from datetime import datetime

from src.domain.enums.chat_participant_role_enum import ChatParticipantRole


@dataclass(slots=True)
class AddChatParticipantDTO:
    chat_id: str
    user_id: str
    role: ChatParticipantRole


@dataclass(slots=True)
class UpdateLastReadDTO:
    chat_id: str
    user_id: str
    last_read_at: datetime


@dataclass(slots=True)
class CheckChatParticipantDTO:
    chat_id: str
    user_id: str


@dataclass(slots=True)
class MuteChatParticipantDTO:
    chat_id: str
    user_id: str


@dataclass(slots=True)
class UnmuteChatParticipantDTO:
    chat_id: str
    user_id: str


@dataclass(slots=True)
class ArchiveChatForUserDTO:
    chat_id: str
    user_id: str


@dataclass(slots=True)
class UnarchiveChatForUserDTO:
    chat_id: str
    user_id: str