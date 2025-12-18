from typing import TypedDict

from src.application.services import (
    CourseService,
    AdminCategoryService,
    AdminCourseService,
    AdminModuleService,
    AdminLessonService,
    CategoryService
)

from src.infrastructure.db.mongo.repositories import (
    CourseRepository,
    AdminCategoryRepository,
    AdminCourseRepository,
    AdminModuleRepository,
    AdminLessonRepository,
    CategoryRepository,
)


class Services(TypedDict):
    course: CourseService
    admin_category: AdminCategoryService
    admin_course: AdminCourseService
    admin_module: AdminModuleService
    admin_lesson: AdminLessonService
    category: CategoryService


def build_repositories():
    return {
        "course": CourseRepository(),
        "admin_category": AdminCategoryRepository(),
        "admin_course": AdminCourseRepository(),
        "admin_module": AdminModuleRepository(),
        "admin_lesson": AdminLessonRepository(),
        "category": CategoryRepository(),
    }


def build_services() -> Services:
    repos = build_repositories()

    return {
        "course": CourseService(repos["course"]),
        "admin_category": AdminCategoryService(repos["admin_category"]),
        "admin_course": AdminCourseService(repos["admin_course"]),
        "admin_module": AdminModuleService(repos["admin_module"]),
        "admin_lesson": AdminLessonService(repos["admin_lesson"]),
        "category": CategoryService(repos["category"]),
    }