from dataclasses import dataclass


@dataclass(slots=True)
class ListChatMessagesDTO:
    chat_id: str
    limit: int
    offset: int
