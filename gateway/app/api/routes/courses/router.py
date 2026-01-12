from fastapi import APIRouter

from .module_router import module_router
from .course_router import course_router
from .category_router import category_router

router = APIRouter()

router.include_router(module_router)
router.include_router(course_router)
router.include_router(category_router)
