import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.course import media_pb2 as pb2
from generated.course import media_pb2_grpc as pb2_grpc


class MediaClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("course_service:50052")
        self.stub = pb2_grpc.CourseMediaServiceStub(self.channel)

    def upload_image(
        self,
        *,
        data: dict,
        type: str,
    ) -> dict:
        try:
            res = self.stub.UploadImage(
                pb2.UploadImageRequest(
                    data=pb2.MediaData(
                        original_url=data["original_url"],
                        thumb_small_url=data.get("thumb_small_url", ""),
                        thumb_medium_url=data.get("thumb_medium_url", ""),
                    ),
                    type=type,
                ),
                timeout=3.0,
            )
            return MessageToDict(
                res,
                preserving_proto_field_name=True,
            )
        except grpc.RpcError as e:
            self._err(e)

    def upload_file(
        self,
        *,
        data: dict,
        type: str,
        scope: str,
        filename: str,
        mime_type: str,
        size_bytes: int,
    ) -> dict:
        try:
            res = self.stub.UploadFile(
                pb2.UploadFileRequest(
                    data=pb2.MediaData(
                        original_url=data["path"],
                    ),
                    type=type,
                    scope=scope,
                    filename=filename,
                    mime_type=mime_type,
                    size_bytes=size_bytes,
                ),
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
            raise HTTPException(404, msg)
        if code == grpc.StatusCode.ALREADY_EXISTS:
            raise HTTPException(409, msg)
        if code == grpc.StatusCode.INVALID_ARGUMENT:
            raise HTTPException(422, msg)

        raise HTTPException(400, msg)


media_client = MediaClient()
