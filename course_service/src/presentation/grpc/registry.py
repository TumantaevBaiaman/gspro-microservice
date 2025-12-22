from dataclasses import dataclass
from typing import Type, Callable

from src.application.services import (
    CourseService,
    AdminCategoryService,
    AdminCourseService,
    AdminModuleService,
    AdminLessonService,
    CategoryService,
)

from src.presentation.grpc.handlers import (
    CourseHandler,
    AdminCategoryHandler,
    AdminCourseHandler,
    AdminModuleHandler,
    AdminLessonHandler,
    CategoryHandler,
)

from generated.course.course_pb2_grpc import add_CourseServiceServicer_to_server
from generated.course.admin_category_pb2_grpc import add_AdminCategoryServiceServicer_to_server
from generated.course.admin_course_pb2_grpc import add_AdminCourseServiceServicer_to_server
from generated.course.admin_module_pb2_grpc import add_AdminModuleServiceServicer_to_server
from generated.course.admin_lesson_pb2_grpc import add_AdminLessonServiceServicer_to_server
from generated.course.category_pb2_grpc import add_CourseCategoryServiceServicer_to_server


@dataclass(frozen=True)
class GrpcServiceConfig:
    add_to_server: Callable
    service_cls: Type
    handler_cls: Type


GRPC_SERVICES: list[GrpcServiceConfig] = [
    GrpcServiceConfig(
        add_CourseServiceServicer_to_server,
        CourseService,
        CourseHandler,
    ),
    GrpcServiceConfig(
        add_AdminCategoryServiceServicer_to_server,
        AdminCategoryService,
        AdminCategoryHandler,
    ),
    GrpcServiceConfig(
        add_AdminCourseServiceServicer_to_server,
        AdminCourseService,
        AdminCourseHandler,
    ),
    GrpcServiceConfig(
        add_AdminModuleServiceServicer_to_server,
        AdminModuleService,
        AdminModuleHandler,
    ),
    GrpcServiceConfig(
        add_AdminLessonServiceServicer_to_server,
        AdminLessonService,
        AdminLessonHandler,
    ),
    GrpcServiceConfig(
        add_CourseCategoryServiceServicer_to_server,
        CategoryService,
        CategoryHandler,
    ),
]
