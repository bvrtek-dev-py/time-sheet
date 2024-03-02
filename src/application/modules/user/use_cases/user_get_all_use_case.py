from typing import List

from time_sheet.src.core.modules.user.dto.user import UserDTO
from time_sheet.src.core.modules.user.repositories.user_repository import (
    IUserRepository,
)


class UserGetAllUseCase:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def execute(self) -> List[UserDTO]:
        return await self._repository.get_all()
