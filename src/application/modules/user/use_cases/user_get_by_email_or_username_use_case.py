from time_sheet.src.core.modules.common.exceptions.domain import ObjectDoesNotExist
from time_sheet.src.core.modules.user.dto.user import UserDTO
from time_sheet.src.core.modules.user.repositories.user_repository import (
    IUserRepository,
)


class UserGetByEmailOrUsernameUseCase:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def execute(self, field: str) -> UserDTO:
        user = await self._repository.get_by_email(field)
        if user is not None:
            return user

        user = await self._repository.get_by_username(field)
        if user is not None:
            return user

        raise ObjectDoesNotExist()
