from fastapi import APIRouter, Depends

from app.api.dependencies.auth import get_current_user
from app.clients.favorite import course_favorite_client
from app.schemas.favorite.course_favorite import IsFavoriteResponseSchema

course_favorite_router = APIRouter(
    prefix="/courses/{course_id}/favorite",
    tags=["Course Favorites"],
)


@course_favorite_router.get(
    "",
    response_model=IsFavoriteResponseSchema,
)
def is_favorite(
    course_id: str,
    user=Depends(get_current_user),
):
    user_id = user.get("sub")
    return {
        "is_favorite": course_favorite_client.is_favorite(
            user_id=user_id,
            course_id=course_id,
        )
    }


@course_favorite_router.post("")
def add_to_favorites(
    course_id: str,
    user = Depends(get_current_user),
):
    user_id = user.get("sub")

    return course_favorite_client.add_to_favorites(
        user_id=user_id,
        course_id=course_id,
    )


@course_favorite_router.delete("")
def remove_from_favorites(
    course_id: str,
    user = Depends(get_current_user),
):
    user_id = user.get("sub")
    return {
        "success": course_favorite_client.remove_from_favorites(
            user_id=user_id,
            course_id=course_id,
        )
    }