from time_sheet.src.core.modules.user.repositories.user_repository import (
    IUserRepository,
)


class UserDeleteUseCase:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def execute(self, id: str) -> None:
        return await self._repository.delete(id=id)
