from fastapi import APIRouter

from .chat import chat_router

router = APIRouter()

router.include_router(chat_router)
