from src.domain.dto.profile_dto import (
    ListProfilesRequestDTO,
    ListProfilesResponseDTO,
    ListProfilesItemDTO
)


class ListProfilesQuery:
    def __init__(self, repo):
        self.repo = repo

    async def execute(
            self,
            dto: ListProfilesRequestDTO
    ) -> ListProfilesResponseDTO:
        profiles, total = await self.repo.list_profiles(
            limit=dto.limit,
            offset=dto.offset
        )

        items = [
            ListProfilesItemDTO(
                user_id=str(profile.user_id),
                full_name=profile.full_name,
                phone_number=profile.phone_number,
                city=profile.city,
                industry=profile.industry,
                experience_level=profile.experience_level,
            )
            for profile in profiles
        ]

        return ListProfilesResponseDTO(
            items=items,
            total=total
        )