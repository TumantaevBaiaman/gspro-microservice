from fastapi import APIRouter

from .purchase_request import purchase_request_router
from .course_access import course_access_router

router = APIRouter()

router.include_router(purchase_request_router)
router.include_router(course_access_router)