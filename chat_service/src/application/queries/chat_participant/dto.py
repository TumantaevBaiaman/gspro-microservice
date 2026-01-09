from dataclasses import dataclass


@dataclass(slots=True)
class ListChatParticipantsDTO:
    chat_id: str


@dataclass(slots=True)
class ListChatIdsByUserDTO:
    user_id: str


@dataclass(slots=True)
class CheckChatParticipantDTO:
    chat_id: str
    user_id: str