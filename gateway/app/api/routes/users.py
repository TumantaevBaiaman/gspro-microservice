from fastapi import APIRouter, Depends

from app.api.dependencies.auth import get_current_user
from app.clients.user import user_client

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
async def get_current_user_info(user=Depends(get_current_user)):
    user_id = user.get("sub")

    return {"user_id": user_id}
