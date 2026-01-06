from src.infrastructure.db.mongo.repositories import (
    CourseRepository,
    AdminCategoryRepository,
    AdminCourseRepository,
    AdminModuleRepository,
    AdminLessonRepository,
    CategoryRepository,
    ModuleRepository,
    LessonRepository,
    FileRepository,
    ImageRepository,
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
    MediaService,
)


def build_services() -> dict[type, object]:
    return {
        CourseService: CourseService(CourseRepository(), LessonService(LessonRepository())),
        AdminCategoryService: AdminCategoryService(AdminCategoryRepository()),
        AdminCourseService: AdminCourseService(AdminCourseRepository()),
        AdminModuleService: AdminModuleService(AdminModuleRepository()),
        AdminLessonService: AdminLessonService(AdminLessonRepository()),
        CategoryService: CategoryService(CategoryRepository()),
        ModuleService: ModuleService(ModuleRepository(), LessonService(LessonRepository()), LessonRepository()),
        LessonService: LessonService(LessonRepository()),
        MediaService: MediaService(
            image_repo=ImageRepository(),
            file_repo=FileRepository(),
        ),
    }
