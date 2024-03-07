from time_sheet.src.application.modules.user.dto.user import (
    UserUpdateDTO,
)
from time_sheet.src.application.modules.user.use_cases.user_get_by_id_use_case import (
    UserGetByIdUseCase,
)
from time_sheet.src.core.modules.user.dto.user import UserDTO
from time_sheet.src.core.modules.user.repositories.user_repository import (
    IUserRepository,
)


class UserUpdateUseCase:
    def __init__(
        self, repository: IUserRepository, get_by_id_use_case: UserGetByIdUseCase
    ):
        self._repository = repository
        self._get_by_id_use_case = get_by_id_use_case

    async def execute(self, request_dto: UserUpdateDTO, user_id: str) -> UserDTO:
        user_dto = await self._get_by_id_use_case.execute(user_id)
        user_dto.fullname = request_dto.fullname

        return await self._repository.update(user_dto)
