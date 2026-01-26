from fastapi import APIRouter, Depends, Path, Query

from app.api.dependencies.auth import get_current_user
from app.clients.chat import chat_client, chat_message_client
from app.clients.media import media_client
from app.clients.user import user_profile_client, sync_profile_client
from app.schemas.chat.chat import GetOrCreateChatResponse, GetOrCreateChatRequest, ChatMessageListResponse, \
    ChatListResponse

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
    limit: int = Query(5, ge=1, le=50),
    lesson_id: str = Query(None, description="Lesson ID"),
    user=Depends(get_current_user),
):

    data = chat_message_client.list_messages(
        chat_id=chat_id,
        limit=limit,
        offset=offset,
        lesson_id=lesson_id,
    )

    for message in data["messages"]:
        message["sender"] = sync_profile_client.profile_by_id(message["sender_id"]) if message["sender_id"] else None

    return data


@chat_router.get(
    "/{chat_id}/files",
    summary="Get Current User Portfolio",
    description="Endpoint to retrieve the portfolio information of the currently authenticated users."
)
async def get_chat_files(
        chat_id: str = Path(..., description="Chat ID"),
        user=Depends(get_current_user)
):
    file_items = media_client.list_media_by_owner(
        owner_service="chat",
        owner_id=chat_id,
        usage="message",
        kind="file",
    )
    return [file_item for file_item in file_items]


@chat_router.get(
    "/{chat_id}/images",
    summary="Get Current User Portfolio",
    description="Endpoint to retrieve the portfolio information of the currently authenticated users."
)
async def get_chat_images(
        chat_id: str = Path(..., description="Chat ID"),
        user=Depends(get_current_user)
):
    file_items = media_client.list_media_by_owner(
        owner_service="chat",
        owner_id=chat_id,
        usage="message",
        kind="image",
    )
    return [file_item for file_item in file_items]


@chat_router.get(
    "",
    response_model=ChatListResponse,
    summary="Get current user chats (inbox)",
)
def list_my_chats(
    limit: int = Query(20, ge=1, le=50),
    offset: int = Query(0, ge=0),
    chat_type: str | None = Query(None, description="DIRECT | COURSE_PRIVATE | COURSE_GROUP"),
    user=Depends(get_current_user),
):
    user_id = user["sub"]

    data = chat_client.list_user_chats(
        user_id=user_id,
        chat_type=chat_type,
        limit=limit,
        offset=offset,
    )

    chats = data.get("chats", [])
    for chat in chats:
        chat["participant_ids"] = (
            sync_profile_client.list_profiles_by_ids(chat.get("participant_ids", []))
            if chat.get("chat_type") == "direct" and chat.get("participant_ids")
            else None
        )


    return {
        "items": chats,
        "total": data.get("total", 0),
    }
