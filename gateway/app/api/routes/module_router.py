from http.client import HTTPException

from fastapi import APIRouter, Depends

from app.core.media.base import MediaProvider
from app.core.media.provider import get_media_provider
from app.clients.course import lesson_client
from app.schemas.course.lesson import *

router = APIRouter(prefix="/modules", tags=["Module"])


@router.get(
    "/{module_id}/lessons",
    response_model=LessonListResponse,
    summary="List lessons by module ID",
    description="Retrieve a list of lessons associated with a specific module using the module's unique identifier.",
)
def list_lessons_by_module(module_id: str):
    data = lesson_client.list_lessons_by_module(module_id)
    return LessonListResponse(items=[LessonShortSchema(**item) for item in data])


@router.get(
    "/{module_id}/lessons/{lesson_id}",
    response_model=LessonSchema,
    summary="Get lesson by ID within a module",
    description="Retrieve detailed information about a specific lesson within a module using the lesson's unique identifier.",
)
def get_lesson(module_id: str, lesson_id: str):
    lesson = lesson_client.get_lesson(lesson_id)

    if lesson["module_id"] != module_id:
        raise HTTPException(404, "Lesson not found")

    return lesson


@router.get(
    "/{module_id}/lessons/{lesson_id}/stream",
    response_model=LessonStreamResponse,
    summary="Get lesson stream URL",
    description="Generate a temporary streaming URL for a specific lesson's video content within a module.",
)
def get_lesson_stream(
    module_id: str,
    lesson_id: str,
    media_provider: MediaProvider = Depends(get_media_provider),
):
    lesson = lesson_client.get_lesson(lesson_id)

    if lesson["module_id"] != module_id:
        raise HTTPException(404, "Lesson not found")

    if not lesson.get("video_id"):
        raise HTTPException(404, "Video not found")

    embed_url, expires_at = media_provider.generate_stream_url(
        video_id=lesson["video_id"],
        expires_in_seconds=300,
    )

    return LessonStreamResponse(
        embed_url=embed_url,
        expires_at=expires_at,
    )


