from time_sheet.src.application.modules.user.use_cases.user_get_by_id_use_case import (
    UserGetByIdUseCase,
)
from time_sheet.src.core.modules.user.repositories.user_repository import (
    IUserRepository,
)


class UserDeleteUseCase:
    def __init__(
        self, repository: IUserRepository, get_by_id_use_case: UserGetByIdUseCase
    ):
        self._repository = repository
        self._get_by_id_use_case = get_by_id_use_case

    async def execute(self, user_id: str) -> None:
        await self._get_by_id_use_case.execute(user_id)

        return await self._repository.delete(user_id=user_id)
