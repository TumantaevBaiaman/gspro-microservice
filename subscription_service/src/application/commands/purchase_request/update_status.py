from src.domain.enums.purchase_request import (
    PurchaseRequestStatus,
    PurchaseTargetType,
)
from src.domain.repositories.purchase_request_repository import (
    IPurchaseRequestRepository,
)
from src.domain.repositories.course_access_repository import (
    ICourseAccessRepository,
)


class UpdatePurchaseRequestStatusCommand:
    def __init__(
        self,
        repo: IPurchaseRequestRepository,
        course_access_repo: ICourseAccessRepository,
    ):
        self.repo = repo
        self.course_access_repo = course_access_repo

    async def execute(
        self,
        *,
        request_id: str,
        status: PurchaseRequestStatus,
    ) -> bool:
        pr = await self.repo.get_by_id(request_id)

        old_status = pr.status

        if old_status == status:
            return True

        await self.repo.update_status(
            request_id=request_id,
            status=status,
        )

        await self._handle_status_change(
            pr=pr,
            new_status=status,
            old_status=old_status,
        )

        return True

    async def _handle_status_change(
        self,
        *,
        pr,
        old_status: PurchaseRequestStatus,
        new_status: PurchaseRequestStatus,
    ) -> None:
        if pr.target_type != PurchaseTargetType.COURSE:
            return

        if not pr.user_id:
            return

        if (
            old_status != PurchaseRequestStatus.PAID
            and new_status == PurchaseRequestStatus.PAID
        ):
            has = await self.course_access_repo.has_access(
                user_id=pr.user_id,
                course_id=pr.target_id,
            )
            if not has:
                await self.course_access_repo.grant(
                    user_id=pr.user_id,
                    course_id=pr.target_id,
                )

        elif (
            old_status == PurchaseRequestStatus.PAID
            and new_status != PurchaseRequestStatus.PAID
        ):
            await self.course_access_repo.revoke(
                user_id=pr.user_id,
                course_id=pr.target_id,
            )

