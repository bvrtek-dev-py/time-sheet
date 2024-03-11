from typing import Annotated
from fastapi import Depends

from time_sheet.src.application.modules.auth.services.login_service import LoginService
from time_sheet.src.application.modules.auth.services.password_service import (
    PasswordChangeService,
    PasswordHashService,
    PasswordVerifyService,
)
from time_sheet.src.application.modules.auth.services.token_service import TokenService
from time_sheet.src.application.modules.user.services.user_service import UserService
from time_sheet.src.application.modules.user.use_cases.user_get_by_id_use_case import (
    UserGetByIdUseCase,
)
from time_sheet.src.core.modules.user.repositories.user_repository import (
    IUserRepository,
)


from time_sheet.src.infrastructure.dependencies.auth.creators import (
    get_password_hash_service,
    get_password_verify_service,
    get_token_service,
)
from time_sheet.src.infrastructure.dependencies.user.factories import (
    get_user_repository,
    get_user_get_by_id_use_case,
    get_user_service,
)


def get_password_change_service(
    get_by_id_use_case: Annotated[
        UserGetByIdUseCase, Depends(get_user_get_by_id_use_case)
    ],
    user_repository: Annotated[IUserRepository, Depends(get_user_repository)],
    hash_service: Annotated[PasswordHashService, Depends(get_password_hash_service)],
    verify_service: Annotated[
        PasswordVerifyService, Depends(get_password_verify_service)
    ],
) -> PasswordChangeService:
    return PasswordChangeService(
        user_repository=user_repository,
        get_by_id_use_case=get_by_id_use_case,
        hash_service=hash_service,
        verify_service=verify_service,
    )


def get_login_service(
    user_service: Annotated[UserService, Depends(get_user_service)],
    verify_service: Annotated[
        PasswordVerifyService, Depends(get_password_verify_service)
    ],
    token_service: Annotated[TokenService, Depends(get_token_service)],
) -> LoginService:
    return LoginService(
        verify_service=verify_service,
        token_service=token_service,
        user_service=user_service,
    )
