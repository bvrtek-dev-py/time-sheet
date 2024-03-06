from time_sheet.src.core.modules.common.exceptions.domain import ObjectDoesNotExist

from time_sheet.src.core.modules.user.dto.user import UserDTO
from time_sheet.src.core.modules.user.repositories.user_repository import (
    IUserRepository,
)


class UserGetByIdUseCase:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def execute(self, id: str) -> UserDTO:
        user = await self._repository.get_by_id(id=id)

        if user is None:
            raise ObjectDoesNotExist

        return user
