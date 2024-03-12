from passlib.context import CryptContext

from time_sheet.src.application.modules.user.use_cases.user_get_by_id_use_case import (
    UserGetByIdUseCase,
)
from time_sheet.src.core.modules.auth.dto.auth import ChangePasswordDTO
from time_sheet.src.core.modules.common.exceptions.domain import InvalidCredentials
from time_sheet.src.core.modules.user.dto.user import UserDTO
from time_sheet.src.core.modules.user.repositories.user_repository import (
    IUserRepository,
)


class PasswordHashService:
    def __init__(self, crypt: CryptContext):
        self._crypt = crypt

    def hash(self, password: str) -> str:
        return self._crypt.hash(password)


class PasswordVerifyService:
    def __init__(self, crypt: CryptContext):
        self._crypt = crypt

    def verify(self, password: str, password_hash: str) -> bool:
        return self._crypt.verify(password, password_hash)


class PasswordChangeService:
    def __init__(
        self,
        user_repository: IUserRepository,
        get_by_id_use_case: UserGetByIdUseCase,
        hash_service: PasswordHashService,
        verify_service: PasswordVerifyService,
    ):
        self._user_repository = user_repository
        self._get_by_id_use_case = get_by_id_use_case
        self._hash_service = hash_service
        self._verify_service = verify_service

    async def change_password(
        self, user_id: str, request: ChangePasswordDTO
    ) -> UserDTO:
        user = await self._get_by_id_use_case.execute(user_id)

        if not self._verify_service.verify(request.current_password, user.password):
            raise InvalidCredentials()

        user.password = self._hash_service.hash(request.password)
        user = await self._user_repository.update(user)

        return user
