from fastapi import APIRouter

from .auth_router import auth_router
from .profiles_router import profile_router
from .user_router import user_router
from .user_education_router import user_education_router
from .user_certificate_router import user_certificate_router
from .user_experience_router import user_experience_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(profile_router)
router.include_router(user_router)
router.include_router(user_education_router)
router.include_router(user_certificate_router)
router.include_router(user_experience_router)
