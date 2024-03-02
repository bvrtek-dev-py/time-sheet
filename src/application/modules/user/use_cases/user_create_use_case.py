from time_sheet.src.application.modules.user.dto.user import UserCreateDTO
from time_sheet.src.core.modules.user.dto.user import UserDTO
from time_sheet.src.core.modules.user.repositories.user_repository import (
    IUserRepository,
)


class UserCreateUseCase:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def execute(self, request_dto: UserCreateDTO) -> UserDTO:
        return await self._repository.save(
            UserDTO(**request_dto.model_dump(), _id=None)
        )
