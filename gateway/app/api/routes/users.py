from fastapi import APIRouter
from app.clients.user import user_client

router = APIRouter(prefix="/users", tags=["Users"])
