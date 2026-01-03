from datetime import datetime
from typing import Optional, List

from beanie import before_event, Insert
from pydantic import Field, BaseModel

from src.domain.enums.chat_message_reference_type_enum import MessageReferenceTypeEnum
from src.domain.enums.chat_message_type_enum import ChatMessageTypeEnum
from .base import BaseDocument


class ChatAttachment(BaseModel):
    file_id: str
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
    created_at: datetime = Field(default_factory=datetime.utcnow)
    edited_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class ChatMessageDocument(BaseDocument):
    chat_id: str
    sender_id: str

    payload: ChatMessagePayload
    context: ChatMessageContext = Field(default_factory=ChatMessageContext)
    meta: ChatMessageMeta = Field(default_factory=ChatMessageMeta)

    @before_event(Insert)
    def validate(self):
        if self.payload.type == ChatMessageTypeEnum.TEXT:
            if not self.payload.text:
                raise ValueError(
                    "TEXT message must contain text"
                )

        if self.payload.type != ChatMessageTypeEnum.TEXT:
            if not self.payload.attachments:
                raise ValueError(
                    "Non-text message must contain attachments"
                )

    class Settings:
        name = "chat_messages"
        indexes = [
            "chat_id",
            "sender_id",
            "context.reference.type",
            "context.reference.id",
            "context.reply_to_message_id",
            "meta.created_at",
        ]