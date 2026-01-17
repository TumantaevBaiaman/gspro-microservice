from fastapi import APIRouter

from .progress import lesson_progress_router

router = APIRouter()

router.include_router(lesson_progress_router)
