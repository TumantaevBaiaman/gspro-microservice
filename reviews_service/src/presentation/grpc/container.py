from src.infrastructure.db.mongo.repositories import *

from src.application.services import *


def build_services() -> dict[type, object]:
    return {
        CourseReviewService: CourseReviewService(
            repo=CourseReviewRepository(),
        ),
    }
