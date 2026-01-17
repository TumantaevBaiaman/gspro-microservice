from fastapi import APIRouter

from .users import router as users_router
from .courses import router as courses_router
from .reviews import router as reviews_router
from .favorites import router as favorites_router
from .chats import router as chats_router
from .media import router as media_router
from .subscriptions import router as subscriptions_router
from .admin import router as admin_router
from .progress import router as progress_router


def get_api_router() -> APIRouter:
    router = APIRouter()

    router.include_router(users_router)
    router.include_router(courses_router)
    router.include_router(reviews_router)
    router.include_router(favorites_router)
    router.include_router(chats_router)
    router.include_router(media_router)
    router.include_router(subscriptions_router)
    router.include_router(progress_router)
    router.include_router(admin_router)

    return router
