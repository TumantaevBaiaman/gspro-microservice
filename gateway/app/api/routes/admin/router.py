from fastapi import APIRouter, Depends

from app.core.security.permissions import require_admin
from .category_router import admin_category_router
from .course_router import admin_course_router
from .module_router import admin_module_router
from .lesson_router import admin_lesson_router


router = APIRouter(
    prefix="/admin",
    # dependencies=[Depends(require_admin)]
)

router.include_router(admin_category_router)
router.include_router(admin_course_router)
router.include_router(admin_module_router)
router.include_router(admin_lesson_router)