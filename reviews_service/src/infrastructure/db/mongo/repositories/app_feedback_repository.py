from src.domain.repositories.app_feedback_repository import (
    IAppFeedbackRepository,
)
from src.infrastructure.db.mongo.models.app_feedback import (
    AppFeedbackDocument,
)


class AppFeedbackRepository(IAppFeedbackRepository):

    async def create(
        self,
        *,
        user_id: str,
        message: str,
        type: str = "feedback",
        is_public: bool = False,
    ) -> AppFeedbackDocument:
        doc = AppFeedbackDocument(
            user_id=user_id,
            message=message,
            type=type,
            is_public=is_public,
        )
        await doc.insert()
        return doc

    async def list(
        self,
        *,
        limit: int,
        offset: int,
    ) -> tuple[list[AppFeedbackDocument], int]:
        query = AppFeedbackDocument.find()

        total = await query.count()

        items = await (
            query
            .skip(offset)
            .limit(limit)
            .to_list()
        )

        return items, total
