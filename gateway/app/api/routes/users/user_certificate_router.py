from fastapi import APIRouter, Depends, Query
from google.protobuf.json_format import MessageToDict

from app.clients.user.user_certificate_client import user_certificate_client
from app.schemas.user.user_certificate import (
    CreateUserCertificateSchema,
    ListUserCertificatesResponseSchema,
    UserCertificateItemSchema,
)

from app.api.dependencies.auth import get_current_user

user_certificate_router = APIRouter(
    prefix="/users/me/certificates",
    tags=["User Certificate"],
)


@user_certificate_router.post(
    "",
    response_model=UserCertificateItemSchema,
    summary="Create certificate",
    description="Create a new certificate for the current users",
)
async def create_certificate(
    data: CreateUserCertificateSchema,
    user=Depends(get_current_user),
):
    user_id = user["sub"]
    response = await user_certificate_client.create(
        user_id=user_id,
        title=data.title,
        issuer=data.issuer,
        issued_at=data.issued_at,
        link=data.link,
    )

    return UserCertificateItemSchema(
        **MessageToDict(response, preserving_proto_field_name=True)
    )


@user_certificate_router.get(
    "",
    response_model=ListUserCertificatesResponseSchema,
    summary="List certificates",
    description="List all certificates for the current users",
)
async def list_certificates(
    user=Depends(get_current_user),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    user_id = user["sub"]
    response = await user_certificate_client.list_by_user(
        user_id=user_id,
        limit=limit,
        offset=offset,
    )

    return ListUserCertificatesResponseSchema(
        **MessageToDict(response, preserving_proto_field_name=True)
    )


@user_certificate_router.delete(
    "/{certificate_id}",
    summary="Delete certificate",
    description="Delete a certificate by its ID",
)
async def delete_certificate(
    certificate_id: str,
    user=Depends(get_current_user),
):
    await user_certificate_client.delete(certificate_id)
    return {"success": True}
