import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.media import media_pb2 as pb2
from generated.media import media_pb2_grpc as pb2_grpc


class MediaClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("media_service:50056")
        self.stub = pb2_grpc.MediaServiceStub(self.channel)

    def create_media(
        self,
        *,
        kind: str,
        usage: str | None = None,
        original_url: str,
        metadata: dict | None = None,
    ) -> dict:
        try:
            res = self.stub.CreateMedia(
                pb2.CreateMediaRequest(
                    kind=kind,
                    usage=usage or "",
                    original_url=original_url,
                    metadata=metadata or {},
                ),
                timeout=3.0,
            )

            return MessageToDict(
                res.media,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def attach_media(
        self,
        *,
        media_id: str,
        owner_service: str,
        owner_id: str,
    ) -> dict:
        try:
            res = self.stub.AttachMedia(
                pb2.AttachMediaRequest(
                    media_id=media_id,
                    owner_service=owner_service,
                    owner_id=owner_id,
                ),
                timeout=3.0,
            )

            return MessageToDict(
                res.media,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def get_media(
        self,
        *,
        media_id: str,
    ) -> dict:
        try:
            res = self.stub.GetMedia(
                pb2.GetMediaRequest(
                    media_id=media_id,
                ),
                timeout=3.0,
            )

            return MessageToDict(
                res.media,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def get_media_batch(
        self,
        *,
        media_ids: list[str],
    ) -> list[dict]:
        try:
            res = self.stub.GetMediaBatch(
                pb2.GetMediaBatchRequest(
                    media_ids=media_ids,
                ),
                timeout=3.0,
            )

            return [
                MessageToDict(item, preserving_proto_field_name=True)
                for item in res.items
            ]

        except grpc.RpcError as e:
            self._err(e)

    def list_media_by_owner(
        self,
        *,
        owner_service: str,
        owner_id: str,
        kind: str | None = None,
        usage: str | None = None,
    ) -> list[dict]:
        try:
            res = self.stub.ListMediaByOwner(
                pb2.ListMediaByOwnerRequest(
                    owner_service=owner_service,
                    owner_id=owner_id,
                    kind=kind or "",
                    usage=usage or "",
                ),
                timeout=3.0,
            )

            return [
                MessageToDict(item, preserving_proto_field_name=True)
                for item in res.items
            ]

        except grpc.RpcError as e:
            self._err(e)

    def delete_media(
        self,
        *,
        media_id: str,
    ) -> bool:
        try:
            res = self.stub.DeleteMedia(
                pb2.DeleteMediaRequest(
                    media_id=media_id,
                ),
                timeout=3.0,
            )

            return res.success

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

        raise HTTPException(status_code=500, detail=msg)


media_client = MediaClient()
