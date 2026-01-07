from dataclasses import dataclass


@dataclass(slots=True)
class GetMessageByIdDTO:
    message_id: str


@dataclass(slots=True)
class ListMessagesByChatDTO:
    chat_id: str
    limit: int = 50
    offset: int = 0


@dataclass(slots=True)
class ListMessagesByReferenceDTO:
    chat_id: str
    reference_type: str
    reference_id: str
    limit: int = 50
    offset: int = 0
