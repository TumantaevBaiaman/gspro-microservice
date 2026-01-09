from fastapi import APIRouter
from google.protobuf.json_format import MessageToDict

from app.clients.course import admin_category_client
from app.schemas.course.admin_category import *


admin_category_router = APIRouter(prefix="/categories", tags=["Admin Categories"])


@admin_category_router.post(
    "/create",
    response_model=AdminCategoryCreateResponseSchema,
    summary="Create a new category",
    description="Endpoint to create a new category in the courses management system."
)
def create_category(data: AdminCategoryCreateRequestSchema):
    response = admin_category_client.create_category(data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminCategoryCreateResponseSchema(
        **response_data
    )


@admin_category_router.get(
    "/{category_id}",
    response_model=AdminCategoryGetResponseSchema,
    summary="Get category by ID",
    description="Endpoint to retrieve a category by its ID."
)
def get_category(category_id: str):
    response = admin_category_client.get_category(category_id)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminCategoryGetResponseSchema(
        **response_data
    )


@admin_category_router.patch(
    "/{category_id}/update",
    response_model=AdminCategoryUpdateResponseSchema,
    summary="Update category by ID",
    description="Endpoint to update a category by its ID."
)
def update_category(category_id: str, data: AdminCategoryUpdateRequestSchema):
    response = admin_category_client.update_category(category_id, data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminCategoryUpdateResponseSchema(
        **response_data
    )


@admin_category_router.delete(
    "/{category_id}/delete",
    response_model=AdminCategoryDeleteResponseSchema,
    summary="Delete category by ID",
    description="Endpoint to delete a category by its ID."
)
def delete_category(category_id: str):
    response = admin_category_client.delete_category(category_id)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminCategoryDeleteResponseSchema(
        **response_data
    )

