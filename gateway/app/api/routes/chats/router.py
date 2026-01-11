from fastapi import APIRouter

from .ws_chat import ws_chat_router
from .media import chat_media_router
from .chat import chat_router

router = APIRouter()

router.include_router(ws_chat_router)
router.include_router(chat_media_router)
router.include_router(chat_router)
