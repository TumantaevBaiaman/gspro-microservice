from fastapi import APIRouter

from .ws_chat_message import ws_chat_router

router = APIRouter()

router.include_router(ws_chat_router)
