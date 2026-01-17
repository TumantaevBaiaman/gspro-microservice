from src.domain.repositories.course_access_repository import (
    ICourseAccessRepository,
)
from src.infrastructure.db.mongo.models.course_access_document import (
    CourseAccessDocument,
)


class CourseAccessRepository(ICourseAccessRepository):

    async def grant(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> CourseAccessDocument:
        doc = CourseAccessDocument(
            user_id=user_id,
            course_id=course_id,
        )
        await doc.insert()
        return doc

    async def revoke(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> bool:
        result = await CourseAccessDocument.find(
            CourseAccessDocument.user_id == user_id,
            CourseAccessDocument.course_id == course_id,
        ).delete()
        return result.deleted_count > 0

    async def has_access(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> bool:
        return await CourseAccessDocument.find(
            CourseAccessDocument.user_id == user_id,
            CourseAccessDocument.course_id == course_id,
        ).exists()

    async def list_user_courses(
            self,
            *,
            user_id: str,
    ) -> list[str]:
        docs = await CourseAccessDocument.find(
            CourseAccessDocument.user_id == user_id
        ).to_list()

        return [doc.course_id for doc in docs]