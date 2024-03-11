# pylint: disable=C0301
from time_sheet.src.application.modules.user.use_cases.user_get_by_email_or_username_use_case import (
    UserGetByEmailOrUsernameUseCase,
)
from time_sheet.src.core.modules.common.exceptions.domain import InvalidCredentials
from time_sheet.src.core.modules.auth.dto.auth import (
    SuccessAuthenticationDTO,
    AuthenticatedUserDTO,
)
from time_sheet.src.application.modules.auth.services.password_service import (
    PasswordVerifyService,
)
from time_sheet.src.application.modules.auth.services.token_service import TokenService


class LoginService:
    def __init__(
        self,
        verify_service: PasswordVerifyService,
        token_service: TokenService,
        user_get_by_email_or_username_use_case: UserGetByEmailOrUsernameUseCase,
    ):
        self._verify_service = verify_service
        self._token_service = token_service
        self._user_get_by_email_or_username_use_case = (
            user_get_by_email_or_username_use_case
        )

    async def login(self, username: str, password: str) -> SuccessAuthenticationDTO:
        user = await self._authenticate(username, password)

        return SuccessAuthenticationDTO(
            token_type="Bearer",
            access_token=self._token_service.create_access_token(user),
            refresh_token=self._token_service.create_refresh_token(user),
            expired_at=self._token_service.get_expire_token_datetime(),
        )

    async def _authenticate(self, username: str, password: str) -> AuthenticatedUserDTO:
        user = await self._user_get_by_email_or_username_use_case.execute(username)

        if not self._verify_service.verify(password, user.password):
            raise InvalidCredentials()

        return AuthenticatedUserDTO(id=user.id, sub=user.email)
