from src.domain.dto.course_dto import CourseCreateDTO
from src.domain.repositories.course_repository import ICourseRepository


class CourseService:
    def __init__(self, repo: ICourseRepository):
        self.repo = repo

    async def create_course(self, dto: CourseCreateDTO):
        return await self.repo.create_course(dto)

    async def get_course_by_id(self, course_id: str):
        return await self.repo.get_course_by_id(course_id)
