from uuid import UUID
import grpc

import generated.user.user_education_pb2 as pb2
import generated.user.user_education_pb2_grpc as pb2_grpc
from src.application.commands.user_education.dto import CreateUserEducationDTO

from src.infrastructure.db.session import async_session_maker
from src.presentation.grpc.container import Container
from src.domain.exceptions.education import EducationNotFoundError


class UserEducationHandler(pb2_grpc.UserEducationServiceServicer):

    async def Create(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            dto = CreateUserEducationDTO(
                institution=request.institution,
                degree=request.degree or None,
                start_year=request.start_year or None,
                end_year=request.end_year or None,
            )

            education = await container.education_service.create.execute(
                user_id=UUID(request.user_id),
                dto=dto,
            )

            return pb2.UserEducationResponse(
                id=str(education.id),
                user_id=str(education.user_id),
                institution=education.institution,
                degree=education.degree or "",
                start_year=education.start_year or 0,
                end_year=education.end_year or 0,
            )

    async def ListByUser(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            items, total = await container.education_service.list_by_user.execute(
                user_id=UUID(request.user_id),
                limit=request.limit,
                offset=request.offset,
            )

            return pb2.ListUserEducationsResponse(
                items=[
                    pb2.UserEducationResponse(
                        id=str(item.id),
                        user_id=str(item.user_id),
                        institution=item.institution,
                        degree=item.degree or "",
                        start_year=item.start_year or 0,
                        end_year=item.end_year or 0,
                    )
                    for item in items
                ],
                total=total,
            )

    async def Delete(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            try:
                await container.education_service.delete.execute(
                    UUID(request.education_id)
                )
                await container.uow.commit()
            except EducationNotFoundError as e:
                await container.uow.rollback()
                await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

            return pb2.DeleteUserEducationResponse()
