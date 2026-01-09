from fastapi import APIRouter, Depends, Query
from google.protobuf.json_format import MessageToDict

from app.api.dependencies.auth import get_current_user
from app.clients.user.user_education_client import user_education_client
from app.schemas.user.user_education import (
    CreateUserEducationSchema,
    ListUserEducationsResponseSchema,
    UserEducationItemSchema,
)


user_education_router = APIRouter(
    prefix="/users/me/educations",
    tags=["User Education"],
)


@user_education_router.post(
    "",
    response_model=UserEducationItemSchema,
    summary="Create education",
    description="Create a new education entry for the current users."
)
async def create_education(
    data: CreateUserEducationSchema,
    user=Depends(get_current_user),
):
    user_id = user["sub"]
    response = await user_education_client.create(
        user_id=user_id,
        institution=data.institution,
        degree=data.degree,
        start_year=data.start_year,
        end_year=data.end_year,
    )

    return UserEducationItemSchema(
        **MessageToDict(response, preserving_proto_field_name=True)
    )


@user_education_router.get(
    "",
    response_model=ListUserEducationsResponseSchema,
    summary="List educations",
    description="Retrieve a list of education entries for the current users with pagination support."
)
async def list_educations(
    user=Depends(get_current_user),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    user_id = user["sub"]
    response = await user_education_client.list_by_user(
        user_id=user_id,
        limit=limit,
        offset=offset,
    )

    return ListUserEducationsResponseSchema(
        **MessageToDict(response, preserving_proto_field_name=True)
    )


@user_education_router.delete(
    "/{education_id}",
    summary="Delete education",
    description="Delete an education entry by its ID for the current users."
)
async def delete_education(
    education_id: str,
    user=Depends(get_current_user),
):
    user_id = user["sub"]
    await user_education_client.delete(education_id)
    return {"success": True}
