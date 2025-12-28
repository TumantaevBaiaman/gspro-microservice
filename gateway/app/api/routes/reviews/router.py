from fastapi import APIRouter

from .course_review import course_review_router
from .app_feedback import app_feedback_router

router = APIRouter()

router.include_router(course_review_router)
router.include_router(app_feedback_router)