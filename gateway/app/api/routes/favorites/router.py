from fastapi import APIRouter

from .course_favorite import course_favorite_router
from .me_favorite import user_favorite_router

router = APIRouter()

router.include_router(course_favorite_router)
router.include_router(user_favorite_router)
