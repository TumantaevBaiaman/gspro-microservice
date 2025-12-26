import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.reviews import course_reviews_pb2 as pb2
from generated.reviews import course_reviews_pb2_grpc as pb2_grpc


class ReviewClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("reviews_service:50053")
        self.stub = pb2_grpc.ReviewServiceStub(self.channel)


    def create_review(
        self,
        *,
        course_id: str,
        user_id: str,
        rating: int,
        comment: str,
        tags: list[str],
    ) -> dict:
        try:
            res = self.stub.CreateReview(
                pb2.CreateReviewRequest(
                    course_id=course_id,
                    user_id=user_id,
                    rating=rating,
                    comment=comment,
                    tags=tags,
                ),
                timeout=3.0,
            )

            return MessageToDict(
                res.review,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def list_reviews_by_course(
        self,
        *,
        course_id: str,
        limit: int,
        offset: int,
    ) -> dict:
        try:
            res = self.stub.ListReviewsByCourse(
                pb2.ListReviewsByCourseRequest(
                    course_id=course_id,
                    limit=limit,
                    offset=offset,
                ),
                timeout=3.0,
            )

            return {
                "items": [
                    MessageToDict(
                        item,
                        preserving_proto_field_name=True,
                    )
                    for item in res.items
                ],
                "total": res.total,
            }

        except grpc.RpcError as e:
            self._err(e)

    def get_course_rating(self, course_id: str) -> dict:
        try:
            res = self.stub.GetCourseRating(
                pb2.GetCourseRatingRequest(course_id=course_id),
                timeout=3.0,
            )

            return MessageToDict(
                res,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def set_course_review_requirement(
        self,
        *,
        course_id: str,
        required_reviews_count: int,
    ) -> dict:
        try:
            res = self.stub.SetCourseReviewRequirement(
                pb2.SetCourseReviewRequirementRequest(
                    course_id=course_id,
                    required_reviews_count=required_reviews_count,
                ),
                timeout=3.0,
            )

            return MessageToDict(
                res.requirement,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def get_course_review_requirement(self, course_id: str) -> dict:
        try:
            res = self.stub.GetCourseReviewRequirement(
                pb2.GetCourseReviewRequirementRequest(
                    course_id=course_id,
                ),
                timeout=3.0,
            )

            return MessageToDict(
                res.requirement,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    @staticmethod
    def _err(e: grpc.RpcError):
        code = e.code()
        msg = e.details()

        if code == grpc.StatusCode.NOT_FOUND:
            raise HTTPException(404, msg)

        if code == grpc.StatusCode.ALREADY_EXISTS:
            raise HTTPException(409, msg)

        raise HTTPException(400, msg)


course_review_client = ReviewClient()
