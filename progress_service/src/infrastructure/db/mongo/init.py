from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from src.core.config import settings
from src.core.logging import logger


async def init_mongo():
    client = AsyncIOMotorClient(
        settings.MONGO_URL,
        uuidRepresentation="standard"
    )
    from src.infrastructure.db.mongo.models.user_daily_learning_document import UserDailyLearningDocument
    from src.infrastructure.db.mongo.models.user_lesson_progress_document import UserLessonProgressDocument

    await init_beanie(
        database=client[settings.MONGO_DB_NAME],
        document_models=[
            UserDailyLearningDocument,
            UserLessonProgressDocument,
        ],
    )
    try:
        await client.admin.command("ping")
        logger.success("MongoDB CONNECTED ✓")
    except Exception as e:
        logger.error(f"MongoDB CONNECTION ERROR: {e}")
