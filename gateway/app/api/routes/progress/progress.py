from datetime import date

from fastapi import APIRouter, Depends, Query

from app.api.dependencies.auth import get_current_user
from app.clients.progress import lesson_progress_client
from app.schemas.progress.lesson_progress import (
    UpdateLessonProgressRequestSchema,
    LessonProgressResponseSchema,
    GetLessonProgressResponseSchema,
    CompletedLessonsCountResponseSchema, LearningDaysResponseSchema,
)

lesson_progress_router = APIRouter(
    prefix="/me/progress",
    tags=["Lesson Progress"],
)

@lesson_progress_router.post(
    "/lesson",
    response_model=LessonProgressResponseSchema,
    summary="Update lesson progress",
)
def update_lesson_progress(
    payload: UpdateLessonProgressRequestSchema,
    user=Depends(get_current_user),
):

    res = lesson_progress_client.update_lesson_progress(
        user_id=user["sub"],
        course_id=payload.course_id,
        module_id=payload.module_id,
        lesson_id=payload.lesson_id,
        lesson_type=payload.lesson_type,
        current_time=payload.current_time,
        duration_seconds=payload.duration_seconds,
        last_scroll_percent=payload.last_scroll_percent,
    )
    print(res)
    return res


@lesson_progress_router.get(
    "/lesson/{lesson_id}",
    response_model=GetLessonProgressResponseSchema,
    summary="Get lesson progress",
)
def get_lesson_progress(
    lesson_id: str,
    user=Depends(get_current_user),
):
    return lesson_progress_client.get_lesson_progress(
        user_id=user["sub"],
        lesson_id=lesson_id,
    )


@lesson_progress_router.get(
    "/course/{course_id}/completed-count",
    response_model=CompletedLessonsCountResponseSchema,
    summary="Get completed lessons count",
)
def get_completed_lessons_count(
    course_id: str,
    user=Depends(get_current_user),
):
    count = lesson_progress_client.get_completed_lessons_count(
        user_id=user["sub"],
        course_id=course_id,
    )
    return {"completed_lessons": count}


@lesson_progress_router.get(
    "/course/{course_id}/learning-days",
    response_model=LearningDaysResponseSchema,
    summary="Get learning days for course",
)
def get_learning_days(
    course_id: str,
    from_date: date | None = Query(
        default=None,
        description="Start date (YYYY-MM-DD)",
    ),
    to_date: date | None = Query(
        default=None,
        description="End date (YYYY-MM-DD)",
    ),
    user=Depends(get_current_user),
):
    return lesson_progress_client.get_learning_days(
        user_id=user["sub"],
        course_id=course_id,
        from_date=from_date,
        to_date=to_date,
    )

