from fastapi import FastAPI
from starlette.middleware import Middleware

from app.api.routes import users_router, auth_router, course_router, admin_router
from app.core.config import settings

app = FastAPI(
    title=settings.app.APP_NAME,
)

app.include_router(users_router.router)
app.include_router(auth_router.router)
app.include_router(course_router.router)
app.include_router(admin_router.router)


@app.get("/")
def root():
    return {"message": f"{settings.app.APP_NAME} is running!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.app.APP_PORT, reload=True)
