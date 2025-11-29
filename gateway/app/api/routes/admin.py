from fastapi import APIRouter

from app.clients.course import admin_category_client
from app.schemas.course import admin_category


router = APIRouter(prefix="/admin", tags=["Admin"])


@router.post("/categories/create")
def create_category(data: admin_category.AdminCategoryCreateRequestSchema):
    response = admin_category_client.create_category(data)
    return {
        "id": response.id
    }
