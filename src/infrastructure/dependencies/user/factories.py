# pylint: disable=R0913, C0301
from typing import Annotated

from fastapi import Depends
from motor.core import AgnosticClientSession

from time_sheet.src.adapters.modules.user.repositories.user_repository import (
    UserRepository,
)
from time_sheet.src.application.modules.auth.services.password_service import (
    PasswordHashService,
)
from time_sheet.src.application.modules.user.services.user_service import UserService
from time_sheet.src.application.modules.user.use_cases.user_check_if_email_exist_use_case import (
    UserCheckIfEmailExistUseCase,
)
from time_sheet.src.application.modules.user.use_cases.user_create_use_case import (
    UserCreateUseCase,
)
from time_sheet.src.application.modules.user.use_cases.user_delete_use_case import (
    UserDeleteUseCase,
)
from time_sheet.src.application.modules.user.use_cases.user_get_all_use_case import (
    UserGetAllUseCase,
)
from time_sheet.src.application.modules.user.use_cases.user_get_by_email_or_username_use_case import (
    UserGetByEmailOrUsernameUseCase,
)
from time_sheet.src.application.modules.user.use_cases.user_get_by_id_use_case import (
    UserGetByIdUseCase,
)
from time_sheet.src.application.modules.user.use_cases.user_update_use_case import (
    UserUpdateUseCase,
)
from time_sheet.src.core.modules.user.repositories.user_repository import (
    IUserRepository,
)
from time_sheet.src.infrastructure.dependencies.auth.creators import (
    get_password_hash_service,
)
from time_sheet.src.infrastructure.dependencies.database.setup import get_session


def get_user_repository(
    session: Annotated[AgnosticClientSession, Depends(get_session)]
) -> IUserRepository:
    return UserRepository(session)


def get_user_create_use_case(
    repository: Annotated[UserRepository, Depends(get_user_repository)]
) -> UserCreateUseCase:
    return UserCreateUseCase(repository)


def get_user_get_by_id_use_case(
    repository: Annotated[UserRepository, Depends(get_user_repository)]
) -> UserGetByIdUseCase:
    return UserGetByIdUseCase(repository)


def get_user_get_all_use_case(
    repository: Annotated[UserRepository, Depends(get_user_repository)]
) -> UserGetAllUseCase:
    return UserGetAllUseCase(repository)


def get_user_update_use_case(
    repository: Annotated[UserRepository, Depends(get_user_repository)],
    get_by_id_use_case: Annotated[
        UserGetByIdUseCase, Depends(get_user_get_by_id_use_case)
    ],
) -> UserUpdateUseCase:
    return UserUpdateUseCase(
        repository=repository, get_by_id_use_case=get_by_id_use_case
    )


def get_user_delete_use_case(
    repository: Annotated[UserRepository, Depends(get_user_repository)],
    get_by_id_use_case: Annotated[
        UserGetByIdUseCase, Depends(get_user_get_by_id_use_case)
    ],
) -> UserDeleteUseCase:
    return UserDeleteUseCase(
        repository=repository, get_by_id_use_case=get_by_id_use_case
    )


def get_user_by_email_or_username_use_case(
    repository: Annotated[UserRepository, Depends(get_user_repository)]
) -> UserGetByEmailOrUsernameUseCase:
    return UserGetByEmailOrUsernameUseCase(repository)


def get_user_email_exist_use_case(
    repository: Annotated[UserRepository, Depends(get_user_repository)]
) -> UserCheckIfEmailExistUseCase:
    return UserCheckIfEmailExistUseCase(repository)


def get_user_service(
    user_create_use_case: Annotated[
        UserCreateUseCase, Depends(get_user_create_use_case)
    ],
    user_update_use_case: Annotated[
        UserUpdateUseCase, Depends(get_user_update_use_case)
    ],
    user_delete_use_case: Annotated[
        UserDeleteUseCase, Depends(get_user_delete_use_case)
    ],
    user_get_by_id_use_case: Annotated[
        UserGetByIdUseCase, Depends(get_user_get_by_id_use_case)
    ],
    user_get_all_use_case: Annotated[
        UserGetAllUseCase, Depends(get_user_get_all_use_case)
    ],
    user_get_by_email_or_username_use_case: Annotated[
        UserGetByEmailOrUsernameUseCase, Depends(get_user_by_email_or_username_use_case)
    ],
    password_hash_service: Annotated[
        PasswordHashService, Depends(get_password_hash_service)
    ],
    user_check_email_exist: Annotated[
        UserCheckIfEmailExistUseCase, Depends(get_user_email_exist_use_case)
    ],
) -> UserService:
    return UserService(
        create_use_case=user_create_use_case,
        update_use_case=user_update_use_case,
        delete_use_case=user_delete_use_case,
        get_all_use_case=user_get_all_use_case,
        get_by_id_use_case=user_get_by_id_use_case,
        get_by_email_or_username_use_case=user_get_by_email_or_username_use_case,
        password_hash_service=password_hash_service,
        check_if_email_exist_use_case=user_check_email_exist,
    )
