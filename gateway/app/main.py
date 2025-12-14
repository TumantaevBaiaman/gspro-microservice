from fastapi import FastAPI
from starlette.middleware import Middleware

from app.api.routes import users_router, auth_router, course_router, admin
from app.core.config import settings

app = FastAPI(
    title=settings.app.APP_NAME,
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(course.router)
app.include_router(admin.router)


@app.get("/")
def root():
    return {"message": f"{settings.app.APP_NAME} is running!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.app.APP_PORT, reload=True)
