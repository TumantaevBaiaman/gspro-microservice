from fastapi import APIRouter

from .test import router as media_router

router = APIRouter()

router.include_router(media_router)
