from src.application.commands.user_certificate.create import (
    CreateUserCertificateCommand,
)
from src.application.commands.user_certificate.delete import (
    DeleteUserCertificateCommand,
)
from src.application.queries.user_certificate.list import (
    ListUserCertificatesQuery,
)


class UserCertificateService:

    def __init__(self, certificate_repo):
        self.create = CreateUserCertificateCommand(certificate_repo)
        self.list_by_user = ListUserCertificatesQuery(certificate_repo)
        self.delete = DeleteUserCertificateCommand(certificate_repo)
