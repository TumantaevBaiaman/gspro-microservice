from src.application.commands.lesson_progress.update import (
    UpdateLessonProgressCommand
)
from src.application.queries.lesson_progress.get import (
    GetLessonProgressQuery
)
from src.application.queries.lesson_progress.get_completed import GetCompletedLessonsCountQuery
from src.application.queries.user_daily_learning.get_user_learning_days import GetUserLearningDaysQuery
from src.domain.repositories.user_lesson_progress_repository import (
    IUserLessonProgressRepository
)
from src.domain.repositories.user_daily_learning_repository import (
    IUserDailyLearningRepository
)


class LessonProgressService:
    def __init__(
        self,
        lesson_repo: IUserLessonProgressRepository,
        daily_repo: IUserDailyLearningRepository,
    ):
        self.update_lesson = UpdateLessonProgressCommand(
            lesson_repo=lesson_repo,
            daily_repo=daily_repo,
        )
        self.get_lesson = GetLessonProgressQuery(
            repo=lesson_repo
        )
        self.get_completed_lessons_count = GetCompletedLessonsCountQuery(
            repo=lesson_repo
        )
        self.get_learning_days = GetUserLearningDaysQuery(
            repo=daily_repo
        )