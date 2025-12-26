from fastapi import APIRouter

from .auth_router import auth_router
from .profiles_router import profile_router
from .user_router import user_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(profile_router)
router.include_router(user_router)