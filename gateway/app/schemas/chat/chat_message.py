from enum import IntEnum
from typing import Optional, List
from pydantic import BaseModel, Field


class ChatScope(IntEnum):
    PRIVATE = 1
    COURSE_PRIVATE = 2
    COURSE_GROUP = 3


class ChatParticipantSchema(BaseModel):
    user_id: str
    role: str


class ChatMessagePayloadSchema(BaseModel):
    type: str
    text: Optional[str] = None


class MessageReferenceSchema(BaseModel):
    type: str
    id: str


class ChatMessageContextSchema(BaseModel):
    reply_to_message_id: Optional[str] = None
    reference: Optional[MessageReferenceSchema] = None


class SendMessageSchema(BaseModel):
    scope: ChatScope
    sender_id: str
    participants: List[ChatParticipantSchema]
    payload: ChatMessagePayloadSchema
    course_id: Optional[str] = None
    context: Optional[ChatMessageContextSchema] = None


class ChatSchema(BaseModel):
    id: str
    scope: int
    course_id: Optional[str] = None
    participant_ids: list[str]
    last_message_at: Optional[str] = None


class ChatMessageSchema(BaseModel):
    id: str
    chat_id: str
    sender_id: str
    payload: dict
    created_at: str


class SendMessageResponseSchema(BaseModel):
    chat: ChatSchema
    message: ChatMessageSchema


class ListMessagesResponseSchema(BaseModel):
    items: list[ChatMessageSchema]
    total: int
