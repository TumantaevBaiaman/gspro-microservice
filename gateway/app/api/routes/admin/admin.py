from fastapi import APIRouter

from .category import admin_category_router
from .course import admin_course_router


router = APIRouter(prefix="/admin")

router.include_router(admin_category_router)
router.include_router(admin_course_router)