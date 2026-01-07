from dataclasses import dataclass
from typing import Optional

from src.infrastructure.db.mongo.models.chat_message_document import ChatMessagePayload, ChatMessageContext


@dataclass(slots=True)
class SendMessageDTO:
    chat_id: str
    sender_id: str
    payload: ChatMessagePayload
    context: ChatMessageContext


@dataclass(slots=True)
class EditMessageDTO:
    message_id: str
    editor_id: str
    new_text: str


@dataclass(slots=True)
class DeleteMessageDTO:
    message_id: str
    user_id: str