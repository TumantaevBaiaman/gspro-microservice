from fastapi import APIRouter
from google.protobuf.json_format import MessageToDict

from app.clients.course import admin_module_client
from app.schemas.course.admin_module import *


admin_module_router = APIRouter(prefix="/modules", tags=["Admin Modules"])


@admin_module_router.post(
    "/create",
    response_model=AdminModuleCreateResponseSchema,
    summary="Create a new module",
    description="Endpoint to create a new module in a courses."
)
def create_module(data: AdminModuleCreateRequestSchema):
    response = admin_module_client.create_module(data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminModuleCreateResponseSchema(**response_data)


@admin_module_router.get(
    "/{module_id}",
    response_model=AdminModuleGetResponseSchema,
    summary="Get module by ID",
    description="Endpoint to retrieve a module by its ID."
)
def get_module(module_id: str):
    response_data = admin_module_client.get_module(module_id)
    return AdminModuleGetResponseSchema(**response_data)


@admin_module_router.patch(
    "/{module_id}/update",
    response_model=AdminModuleUpdateResponseSchema,
    summary="Update module by ID",
    description="Endpoint to update a module by its ID."
)
def update_module(module_id: str, data: AdminModuleUpdateRequestSchema):
    response = admin_module_client.update_module(module_id, data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminModuleUpdateResponseSchema(**response_data)


@admin_module_router.delete(
    "/{module_id}/delete",
    response_model=AdminModuleDeleteResponseSchema,
    summary="Delete module by ID",
    description="Endpoint to delete a module by its ID."
)
def delete_module(module_id: str):
    response = admin_module_client.delete_module(module_id)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminModuleDeleteResponseSchema(**response_data)


@admin_module_router.get(
    "",
    response_model=AdminModuleListResponseSchema,
    summary="List modules",
    description="Endpoint to retrieve a list of modules (optionally filtered by courses)."
)
def list_modules(course_id: str | None = None):
    response = admin_module_client.list_modules(course_id=course_id)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminModuleListResponseSchema(**response_data)
