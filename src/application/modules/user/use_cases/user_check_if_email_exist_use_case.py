from time_sheet.src.core.modules.user.repositories.user_repository import (
    IUserRepository,
)


class UserCheckIfEmailExistUseCase:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def execute(self, field: str) -> bool:
        user = await self._repository.get_by_email(field)
        if user is not None:
            return True

        return False
