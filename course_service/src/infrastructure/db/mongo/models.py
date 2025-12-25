from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from src.core.config import settings
from src.core.logging import logger


async def init_mongo():
    client = AsyncIOMotorClient(
        settings.MONGO_URL,
        uuidRepresentation="standard"
    )

    from src.domain.entities.course_entity import CourseEntity
    from src.domain.entities.category_entity import CategoryEntity
    from src.domain.entities.module_entity import ModuleEntity
    from src.domain.entities.lesson_entity import LessonEntity
    from src.domain.entities.file_entity import FileEntity
    from src.domain.entities.image_entity import ImageEntity

    await init_beanie(
        database=client[settings.MONGO_DB_NAME],
        document_models=[
            CourseEntity,
            CategoryEntity,
            ModuleEntity,
            LessonEntity,
            FileEntity,
            ImageEntity,
        ],
    )
    try:
        await client.admin.command("ping")
        logger.success("MongoDB CONNECTED ✓")
    except Exception as e:
        logger.error(f"MongoDB CONNECTION ERROR: {e}")
