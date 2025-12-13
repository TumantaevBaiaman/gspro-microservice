from generated.course.course_pb2_grpc import add_CourseServiceServicer_to_server
from generated.course.admin_category_pb2_grpc import add_AdminCategoryServiceServicer_to_server
from generated.course.admin_course_pb2_grpc import add_AdminCourseServiceServicer_to_server
from generated.course.admin_module_pb2_grpc import add_AdminModuleServiceServicer_to_server
from generated.course.admin_lesson_pb2_grpc import add_AdminLessonServiceServicer_to_server

from src.presentation.grpc.handlers import (
    CourseHandler,
    AdminCategoryHandler,
    AdminCourseHandler,
    AdminModuleHandler,
    AdminLessonHandler,
)


GRPC_SERVICES = [
    (add_CourseServiceServicer_to_server, "course", CourseHandler),
    (add_AdminCategoryServiceServicer_to_server, "admin_category", AdminCategoryHandler),
    (add_AdminCourseServiceServicer_to_server, "admin_course", AdminCourseHandler),
    (add_AdminModuleServiceServicer_to_server, "admin_module", AdminModuleHandler),
    (add_AdminLessonServiceServicer_to_server, "admin_lesson", AdminLessonHandler),
]
