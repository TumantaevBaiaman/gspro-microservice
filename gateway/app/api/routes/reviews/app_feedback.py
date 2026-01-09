from fastapi import APIRouter, Depends

from app.api.dependencies.auth import get_current_user
from app.schemas.reviews.app_feedback import (
    CreateAppFeedbackSchema,
    AppFeedbackSchema,
    AppFeedbackListSchema,
)
from app.clients.review import app_feedback_client

app_feedback_router = APIRouter(prefix="/feedback", tags=["Feedback"])


@app_feedback_router.post(
    "",
    response_model=AppFeedbackSchema,
    summary="Create App Feedback",
    description="Create a new feedback entry from a users."
)
def create_feedback(
    body: CreateAppFeedbackSchema,
    user=Depends(get_current_user),
):
    user_id = user["sub"]
    return app_feedback_client.create_feedback(
        user_id=user_id,
        message=body.message,
        type=body.type,
        is_public=body.is_public,
    )


@app_feedback_router.get(
    "",
    response_model=AppFeedbackListSchema,
    summary="List App Feedback",
    description="Retrieve a list of feedback entries with pagination."
)
def list_feedback(
    limit: int = 20,
    offset: int = 0,
):
    return app_feedback_client.list_feedback(
        limit=limit,
        offset=offset,
    )
