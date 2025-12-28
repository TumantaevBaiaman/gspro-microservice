from abc import ABC, abstractmethod
from src.infrastructure.db.mongo.models.app_feedback import AppFeedbackDocument


class IAppFeedbackRepository(ABC):

    @abstractmethod
    async def create(
        self,
        *,
        user_id: str,
        message: str,
        type: str = "feedback",
        is_public: bool = False,
    ) -> AppFeedbackDocument:
        ...

    @abstractmethod
    async def list(
        self,
        *,
        limit: int,
        offset: int,
    ) -> tuple[list[AppFeedbackDocument], int]:
        ...
