from fastapi import APIRouter, Query

from app.clients.course import category_client
from app.schemas.course.category import *

router = APIRouter(prefix="/categories", tags=["Category"])

@router.get(
    "/{category_id}",
    response_model=CategoryGetResponseSchema,
    summary="Get category by ID",
    description="Retrieve detailed information about a specific category using its unique identifier.",
)
async def get_category(category_id: str):
    category_data = category_client.get_category(category_id)
    return CategoryGetResponseSchema(**category_data)


@router.get(
    "",
    response_model=CategoryListResponseSchema,
    summary="List categories",
    description="Retrieve a paginated list of categories.",
)
async def list_categories(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    data = category_client.list_categories(
        limit=limit,
        offset=offset
    )

    return CategoryListResponseSchema(
        items=[
            CategoryListItemSchema(**item)
            for item in data["items"]
        ],
        total=data["total"]
    )