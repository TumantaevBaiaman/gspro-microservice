from datetime import datetime
from typing import Optional, List

from beanie import before_event, Insert, after_event
from bson import ObjectId
from pydantic import Field, BaseModel

from src.domain.enums.chat_message_reference_type_enum import MessageReferenceTypeEnum
from src.domain.enums.chat_message_type_enum import ChatMessageTypeEnum
from .chat_document import ChatDocument
from .base import BaseDocument


class ChatAttachment(BaseModel):
    file_id: str
    url: str

    filename: Optional[str] = None
    mime_type: Optional[str] = None
    size: Optional[int] = None
    duration: Optional[int] = None


class ChatMessagePayload(BaseModel):
    type: ChatMessageTypeEnum

    text: Optional[str] = None
    attachments: List[ChatAttachment] = Field(default_factory=list)


class MessageReference(BaseModel):
    type: MessageReferenceTypeEnum
    id: str


class ChatMessageContext(BaseModel):
    reference: Optional[MessageReference] = None
    reply_to_message_id: Optional[str] = None


class ChatMessageMeta(BaseModel):
    edited_at: Optional[datetime] = None


class ChatMessageDocument(BaseDocument):
    chat_id: str
    sender_id: str

    payload: ChatMessagePayload
    context: ChatMessageContext = Field(default_factory=ChatMessageContext)
    meta: ChatMessageMeta = Field(default_factory=ChatMessageMeta)

    @before_event(Insert)
    def validate(self):
        if not self.payload.text and not self.payload.attachments:
            raise ValueError("message must contain text or attachments")

    @after_event(Insert)
    async def update_chat_last_message(self):
        payload = self.payload
        preview = {
            "type": payload.type,
            "text": payload.text,
            "attachments_count": len(payload.attachments),
            "sender_id": self.sender_id,
        }

        await ChatDocument.find_one(
            ChatDocument.id == ObjectId(self.chat_id)
        ).update_one(
            {
                "$set": {
                    "last_message": preview,
                    "last_message_sender_id": self.sender_id,
                },
                "$max": {
                    "last_message_at": self.created_at,
                },
            }
        )

    class Settings:
        name = "chat_messages"