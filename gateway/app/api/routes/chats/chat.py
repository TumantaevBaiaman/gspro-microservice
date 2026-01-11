from fastapi import APIRouter, Depends, Path, Query

from app.api.dependencies.auth import get_current_user
from app.clients.chat import chat_client, chat_message_client
from app.schemas.chat.chat import GetOrCreateChatResponse, GetOrCreateChatRequest, ChatMessageListResponse

chat_router = APIRouter(prefix="/chat", tags=["Chat"])


@chat_router.post(
    "/get-or-create",
    response_model=GetOrCreateChatResponse,
    summary="Get or create chat",
)
def get_or_create_chat(
        body: GetOrCreateChatRequest,
        user=Depends(get_current_user),
):
    user_id = user["sub"]
    return chat_client.get_or_create(
        chat_type=body.chat_type,
        sender_id=user_id,
        peer_id=body.peer_id,
        course_id=body.course_id,
        student_id=body.student_id,
    )


@chat_router.get(
    "/{chat_id}/messages",
    response_model=ChatMessageListResponse,
    summary="Get chat message history",
)
def get_chat_messages(
    chat_id: str = Path(..., description="Chat ID"),
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50),
    user=Depends(get_current_user),
):

    data = chat_message_client.list_messages(
        chat_id=chat_id,
        limit=limit,
        offset=offset,
    )

    return data

