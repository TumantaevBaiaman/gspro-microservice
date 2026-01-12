from fastapi import FastAPI
from app.api.routes import get_api_router
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(title=settings.app.APP_NAME)
    app.include_router(get_api_router(), prefix="/api")
    return app

app = create_app()
