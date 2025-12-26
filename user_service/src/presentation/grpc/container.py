from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.uow import UnitOfWork
from src.infrastructure.db.repositories import (
    UserRepository,
    ProfileRepository,
    UserCategoryRepository,
    UserImageRepository,
    UserEducationRepository,
    UserCertificateRepository,
    UserExperienceRepository,
)
from src.application.services import (
    UserService,
    ProfileService,
    UserCategoryService,
    UserEducationService,
    UserExperienceService,
    UserCertificateService,
)


class Container:
    def __init__(self, session: AsyncSession):
        self.uow = UnitOfWork(session)

        self.user_repo = UserRepository(session)
        self.profile_repo = ProfileRepository(session)
        self.user_category_repo = UserCategoryRepository(session)
        self.user_image_repo = UserImageRepository(session)
        self.user_education_repo = UserEducationRepository(session)
        self.user_certificate_repo = UserCertificateRepository(session)
        self.user_experience_repo = UserExperienceRepository(session)

        self.user_service = UserService(self.user_repo)
        self.profile_service = ProfileService(self.profile_repo, self.user_image_repo, self.user_repo)
        self.user_category_service = UserCategoryService(self.user_category_repo)
        self.education_service = UserEducationService(self.user_education_repo)
        self.experience_service = UserExperienceService(self.user_experience_repo)
        self.certificate_service = UserCertificateService(self.user_certificate_repo)
