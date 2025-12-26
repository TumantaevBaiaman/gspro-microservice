from uuid import UUID
import grpc

import generated.user.user_certificate_pb2 as pb2
import generated.user.user_certificate_pb2_grpc as pb2_grpc
from src.application.commands.user_certificate.dto import CreateUserCertificateDTO

from src.infrastructure.db.session import async_session_maker
from src.presentation.grpc.container import Container
from src.domain.exceptions.certificate import CertificateNotFoundError


class UserCertificateHandler(pb2_grpc.UserCertificateServiceServicer):

    async def Create(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            certificate = await container.certificate_service.create.execute(
                user_id=UUID(request.user_id),
                dto=CreateUserCertificateDTO(
                    title=request.title,
                    issuer=request.issuer or None,
                    issued_at=request.issued_at.ToDatetime() if request.HasField("issued_at") else None,
                    link=request.link or None,
                ),
            )

            await container.uow.commit()

            return pb2.UserCertificateResponse(
                id=str(certificate.id),
                user_id=str(certificate.user_id),
                title=certificate.title,
                issuer=certificate.issuer or "",
                issued_at=certificate.issued_at,
                link=certificate.link or "",
                created_at=certificate.created_at,
            )

    async def ListByUser(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            items, total = await container.certificate_service.list_by_user.execute(
                user_id=UUID(request.user_id),
                limit=request.limit,
                offset=request.offset,
            )

            return pb2.ListUserCertificatesResponse(
                items=[
                    pb2.UserCertificateResponse(
                        id=str(item.id),
                        user_id=str(item.user_id),
                        title=item.title,
                        issuer=item.issuer or "",
                        issued_at=item.issued_at,
                        link=item.link or "",
                        created_at=item.created_at,
                    )
                    for item in items
                ],
                total=total,
            )

    async def Delete(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            try:
                await container.certificate_service.delete.execute(
                    UUID(request.certificate_id)
                )
                await container.uow.commit()
            except CertificateNotFoundError as e:
                await container.uow.rollback()
                await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

            return pb2.DeleteUserCertificateResponse()
