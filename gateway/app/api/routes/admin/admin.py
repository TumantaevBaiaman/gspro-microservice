from fastapi import APIRouter

from .category import admin_category_router


router = APIRouter(prefix="/admin")

router.include_router(admin_category_router)