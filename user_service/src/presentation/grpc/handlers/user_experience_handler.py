from uuid import UUID
from datetime import date
import grpc

import generated.user.user_experience_pb2 as pb2
import generated.user.user_experience_pb2_grpc as pb2_grpc
from src.application.commands.user_experience.dto import CreateUserExperienceDTO

from src.infrastructure.db.session import async_session_maker
from src.presentation.grpc.container import Container
from src.domain.exceptions.experience import ExperienceNotFoundError


class UserExperienceHandler(pb2_grpc.UserExperienceServiceServicer):

    async def Create(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            dto = CreateUserExperienceDTO(
                company=request.company,
                position=request.position,
                start_date=date.fromisoformat(request.start_date),
                end_date=date.fromisoformat(request.end_date) if request.end_date else None,
                description=request.description or None,
            )

            experience = await container.experience_service.create.execute(
                user_id=UUID(request.user_id),
                dto=dto,
            )

            return pb2.UserExperienceResponse(
                id=str(experience.id),
                user_id=str(experience.user_id),
                company=experience.company,
                position=experience.position,
                start_date=experience.start_date.isoformat(),
                end_date=experience.end_date.isoformat() if experience.end_date else "",
                description=experience.description or "",
                created_at=experience.created_at,
            )

    async def ListByUser(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            items, total = await container.experience_service.list_by_user.execute(
                user_id=UUID(request.user_id),
                limit=request.limit,
                offset=request.offset,
            )

            return pb2.ListUserExperiencesResponse(
                items=[
                    pb2.UserExperienceResponse(
                        id=str(item.id),
                        user_id=str(item.user_id),
                        company=item.company,
                        position=item.position,
                        start_date=item.start_date.isoformat(),
                        end_date=item.end_date.isoformat() if item.end_date else "",
                        description=item.description or "",
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
                await container.experience_service.delete.execute(
                    UUID(request.experience_id)
                )
                await container.uow.commit()
            except ExperienceNotFoundError as e:
                await container.uow.rollback()
                await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

            return pb2.DeleteUserExperienceResponse()
