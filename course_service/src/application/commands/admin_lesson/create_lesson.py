from src.domain.dto.admin_lesson_dto import AdminLessonCreateDTO
from src.domain.repositories.admin_lesson_repository import IAdminLessonRepository


class CreateLessonCommand:
    def __init__(self, repo: IAdminLessonRepository):
        self.repo = repo

    async def execute(self, dto: AdminLessonCreateDTO):
        return await self.repo.create(dto)
