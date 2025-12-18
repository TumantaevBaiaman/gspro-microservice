from fastapi import FastAPI, APIRouter

from app.api.routes import (
    user_router,
    auth_router,
    course_router,
    admin_router,
    category_router,
    profiles_router,
)
from app.core.config import settings

app = FastAPI(
    title=settings.app.APP_NAME,
)

router = (APIRouter(prefix="/api"))
router.include_router(auth_router.router)
router.include_router(user_router.router)
router.include_router(profiles_router.router)
router.include_router(category_router.router)
router.include_router(course_router.router)
router.include_router(admin_router.router)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.app.APP_PORT, reload=True)
