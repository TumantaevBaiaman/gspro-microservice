from fastapi import APIRouter
from app.clients.user import user_client

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{user_id}")
def get_user(user_id: int):
    return user_client.get_user(user_id)
