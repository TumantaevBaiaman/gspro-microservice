from src.infrastructure.db.mongo.repositories import (
    CourseRepository,
    AdminCategoryRepository,
    AdminCourseRepository,
    AdminModuleRepository,
    AdminLessonRepository,
    CategoryRepository,
    ModuleRepository,
    LessonRepository,
)

from src.application.services import (
    CourseService,
    AdminCategoryService,
    AdminCourseService,
    AdminModuleService,
    AdminLessonService,
    CategoryService,
    ModuleService,
    LessonService,
)


def build_services() -> dict[type, object]:
    return {
        CourseService: CourseService(CourseRepository()),
        AdminCategoryService: AdminCategoryService(AdminCategoryRepository()),
        AdminCourseService: AdminCourseService(AdminCourseRepository()),
        AdminModuleService: AdminModuleService(AdminModuleRepository()),
        AdminLessonService: AdminLessonService(AdminLessonRepository()),
        CategoryService: CategoryService(CategoryRepository()),
        ModuleService: ModuleService(ModuleRepository()),
        LessonService: LessonService(LessonRepository()),
    }
