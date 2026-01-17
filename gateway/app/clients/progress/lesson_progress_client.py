from datetime import date

import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.progress import lesson_progress_pb2 as pb2
from generated.progress import lesson_progress_pb2_grpc as pb2_grpc


class LessonProgressClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("progress_service:50058")
        self.stub = pb2_grpc.ProgressServiceStub(self.channel)

    def update_lesson_progress(
        self,
        *,
        user_id: str,
        course_id: str,
        module_id: str,
        lesson_id: str,
        lesson_type: str,
        current_time: int | None = None,
        duration_seconds: int | None = None,
        last_scroll_percent: int | None = None,
    ) -> dict:
        try:
            res = self.stub.UpdateLessonProgress(
                pb2.UpdateLessonProgressRequest(
                    user_id=user_id,
                    course_id=course_id,
                    module_id=module_id,
                    lesson_id=lesson_id,
                    lesson_type=lesson_type,
                    current_time=current_time or 0,
                    duration_seconds=duration_seconds or 0,
                    last_scroll_percent=last_scroll_percent or 0,
                ),
                timeout=3.0,
            )

            return MessageToDict(
                res.progress,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def get_lesson_progress(
        self,
        *,
        user_id: str,
        lesson_id: str,
    ) -> dict:
        try:
            res = self.stub.GetLessonProgress(
                pb2.GetLessonProgressRequest(
                    user_id=user_id,
                    lesson_id=lesson_id,
                ),
                timeout=3.0,
            )

            return MessageToDict(
                res,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def get_completed_lessons_count(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> int:
        try:
            res = self.stub.GetCompletedLessonsCount(
                pb2.GetCompletedLessonsCountRequest(
                    user_id=user_id,
                    course_id=course_id,
                ),
                timeout=3.0,
            )

            return res.completed_lessons

        except grpc.RpcError as e:
            self._err(e)

    def get_learning_days(
            self,
            *,
            user_id: str,
            course_id: str,
            from_date: date | None = None,
            to_date: date | None = None,
    ) -> dict:
        try:
            req = pb2.GetLearningDaysRequest(
                user_id=user_id,
                course_id=course_id,
            )

            if from_date:
                req.from_date = from_date.isoformat()

            if to_date:
                req.to_date = to_date.isoformat()

            res = self.stub.GetLearningDays(
                req,
                timeout=3.0,
            )

            return MessageToDict(
                res,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    @staticmethod
    def _err(e: grpc.RpcError):
        code = e.code()
        msg = e.details()

        if code == grpc.StatusCode.NOT_FOUND:
            raise HTTPException(status_code=404, detail=msg)

        if code == grpc.StatusCode.INVALID_ARGUMENT:
            raise HTTPException(status_code=400, detail=msg)

        if code == grpc.StatusCode.PERMISSION_DENIED:
            raise HTTPException(status_code=403, detail=msg)

        raise HTTPException(status_code=500, detail=msg)


lesson_progress_client = LessonProgressClient()
