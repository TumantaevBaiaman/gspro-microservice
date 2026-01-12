from fastapi import APIRouter, Depends

from app.api.dependencies.auth import get_current_user
from app.clients.favorite import course_favorite_client
from app.schemas.favorite.course_favorite import ListUserFavoritesResponseSchema


user_favorite_router = APIRouter(
    prefix="/me/favorites",
    tags=["My Favorites"],
)


@user_favorite_router.get(
    "/course",
    response_model=ListUserFavoritesResponseSchema,
    summary="List My Favorite Courses",
    description="Retrieve a list of the currently authenticated users's favorites courses with pagination support."
)
def list_my_favorites(
    limit: int = 10,
    offset: int = 0,
    user = Depends(get_current_user),
):
    user_id = user.get("sub")
    return course_favorite_client.list_user_favorites(
        user_id=user_id,
        limit=limit,
        offset=offset,
    )