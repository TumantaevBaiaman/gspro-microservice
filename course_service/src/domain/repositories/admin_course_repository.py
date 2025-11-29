from src.domain.dto.admin_course_dto import AdminCourseCreateDTO, AdminCourseUpdateDTO
from src.domain.entities import CourseEntity


class AdminCourseRepository:

    async def create(self, dto: AdminCourseCreateDTO) -> CourseEntity:
        course = CourseEntity(**dto.dict())
        return await course.insert()

    async def get(self, course_id: str) -> CourseEntity | None:
        return await CourseEntity.get(course_id)

    async def list(self) -> list[CourseEntity]:
        return await CourseEntity.find_all().to_list()

    async def save(self, course: CourseEntity) -> CourseEntity:
        return await course.save()

    async def delete(self, course: CourseEntity):
        return await course.delete()
