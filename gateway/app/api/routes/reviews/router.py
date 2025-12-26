from fastapi import APIRouter

from .course_review import course_review_router

router = APIRouter()

router.include_router(course_review_router)