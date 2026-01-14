from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes import get_api_router
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(title=settings.app.APP_NAME)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(get_api_router(), prefix="/api")
    return app

app = create_app()
