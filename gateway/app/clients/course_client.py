import grpc
from fastapi import HTTPException

from generated.course import course_pb2, course_pb2_grpc


class CourseClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("course_service:50052")
        self.stub = course_pb2_grpc.CourseServiceStub(self.channel)

    def create_course(self, data):
        request = course_pb2.CreateCourseRequest(
            title=data.title,
            description=data.description,
        )
        try:
            response = self.stub.CreateCourse(request)
            return response
        except grpc.RpcError as e:
            status = e.code()
            message = e.details()

            if status == grpc.StatusCode.ALREADY_EXISTS:
                raise HTTPException(status_code=409, detail=message)

            raise HTTPException(status_code=400, detail=message)


course_client = CourseClient()
