from src.infrastructure.db.mongo.repositories import *

from src.application.services import *


def build_services() -> dict[type, object]:
    return {
        PurchaseRequestService: PurchaseRequestService(
            repo=PurchaseRequestRepository()
        ),
        CourseAccessService: CourseAccessService(
            repo=CourseAccessRepository()
        )
    }
