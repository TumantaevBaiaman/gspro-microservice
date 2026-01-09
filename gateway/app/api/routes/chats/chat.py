from fastapi import APIRouter, Depends

from app.schemas.chat.chat_message import (
    SendMessageSchema,
    SendMessageResponseSchema,
    ListMessagesResponseSchema,
)
from app.clients.chat import chat_message_client

chat_router = APIRouter(prefix="/chats", tags=["Chat"])


@chat_router.post(
    "/messages",
    response_model=SendMessageResponseSchema,
    summary="Send a chats message",
    description="Send a message in a chats, creating the chats if it does not exist.",
)
def send_message(data: SendMessageSchema):
    return chat_message_client.send_message(
        scope=data.scope,
        sender_id=data.sender_id,
        participants=[p.model_dump() for p in data.participants],
        payload=data.payload.model_dump(),
        course_id=data.course_id,
        context=data.context.model_dump() if data.context else None,
    )


@chat_router.get(
    "/{chat_id}/messages",
    response_model=ListMessagesResponseSchema,
    summary="List chats messages",
    description="Retrieve a list of messages for a specific chats with pagination.",
)
def list_messages(
    chat_id: str,
    limit: int = 20,
    offset: int = 0,
):
    return chat_message_client.list_messages(
        chat_id=chat_id,
        limit=limit,
        offset=offset,
    )
