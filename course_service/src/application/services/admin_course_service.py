from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError

from src.domain.dto.admin_course_dto import AdminCourseCreateDTO, AdminCourseUpdateDTO
from src.domain.repositories import IAdminCourseRepository


class AdminCourseService:
    def __init__(self, repo: IAdminCourseRepository):
        self.repo = repo

    async def create_course(self, dto: AdminCourseCreateDTO):
        try:
            return await self.repo.create(dto)
        except DuplicateKeyError:
            raise HTTPException(409, "Course with this title or codename already exists")

    async def get_course(self, course_id: str):
        course = await self.repo.get(course_id)
        if not course:
            raise HTTPException(404, "Course not found")
        return course

    async def delete_course(self, course_id: str):
        course = await self.get_course(course_id)
        await self.repo.delete(course)
        return True

    async def update_course(self, course_id: str, dto: AdminCourseUpdateDTO):
        course = await self.get_course(course_id)

        for key, value in dto.model_dump(exclude_unset=True).items():
            setattr(course, key, value)

        try:
            return await self.repo.save(course)
        except DuplicateKeyError:
            raise HTTPException(409, "Course already exists with given unique values")

    async def list_courses(self):
        return await self.repo.list()
