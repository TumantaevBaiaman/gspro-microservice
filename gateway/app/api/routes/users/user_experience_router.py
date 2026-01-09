from fastapi import APIRouter, Depends, Query
from google.protobuf.json_format import MessageToDict

from app.api.dependencies.auth import get_current_user
from app.clients.user.user_experience_client import user_experience_client
from app.schemas.user.user_experience import (
    CreateUserExperienceSchema,
    ListUserExperiencesResponseSchema,
    UserExperienceItemSchema,
)


user_experience_router = APIRouter(
    prefix="/users/me/experiences",
    tags=["User Experience"],
)


@user_experience_router.post(
    "",
    response_model=UserExperienceItemSchema,
    summary="Create experience",
    description="Create a new experience entry for the current users."
)
async def create_experience(
    data: CreateUserExperienceSchema,
    user=Depends(get_current_user),
):
    user_id = user["sub"]
    response = await user_experience_client.create(
        user_id=user_id,
        company=data.company,
        position=data.position,
        start_date=data.start_date.isoformat(),
        end_date=data.end_date.isoformat() if data.end_date else None,
        description=data.description,
    )

    return UserExperienceItemSchema(
        **MessageToDict(response, preserving_proto_field_name=True)
    )


@user_experience_router.get(
    "",
    response_model=ListUserExperiencesResponseSchema,
    summary="List experiences",
    description="Retrieve a list of experience entries for the current users with pagination support."
)
async def list_experiences(
    user=Depends(get_current_user),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    user_id = user["sub"]
    response = await user_experience_client.list_by_user(
        user_id=user_id,
        limit=limit,
        offset=offset,
    )

    return ListUserExperiencesResponseSchema(
        **MessageToDict(response, preserving_proto_field_name=True)
    )


@user_experience_router.delete(
    "/{experience_id}",
    summary="Delete experience",
    description="Delete an experience by its ID",
)
async def delete_experience(
    experience_id: str,
    user=Depends(get_current_user),
):
    await user_experience_client.delete(experience_id)
    return {"success": True}
