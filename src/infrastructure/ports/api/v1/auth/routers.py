from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from time_sheet.src.application.modules.auth.services.login_service import LoginService
from time_sheet.src.application.modules.auth.services.password_service import (
    PasswordChangeService,
)
from time_sheet.src.application.modules.auth.services.refresh_token_service import (
    RefreshTokenService,
)
from time_sheet.src.core.modules.auth.dto.auth import CurrentUserDTO, ChangePasswordDTO
from time_sheet.src.infrastructure.dependencies.auth.creators import (
    get_refresh_token_service,
)
from time_sheet.src.infrastructure.dependencies.auth.permissions import get_current_user
from time_sheet.src.infrastructure.dependencies.auth.providers import (
    get_password_change_service,
    get_login_service,
)
from time_sheet.src.infrastructure.ports.api.v1.auth.repsonses import (
    LoginSuccessResponse,
)
from time_sheet.src.infrastructure.ports.api.v1.auth.requests import (
    PasswordChangeRequest,
)
from time_sheet.src.infrastructure.ports.api.v1.common.responses import ErrorResponse
from time_sheet.src.infrastructure.ports.api.v1.user.responses import UserBaseResponse
from time_sheet.src.settings.oauth2 import oauth2_scheme

router = APIRouter(prefix="/api/v1/auth", tags=["APIv1 Auth"])


@router.post(
    "/login",
    responses={
        200: {"model": LoginSuccessResponse},
        404: {"model": ErrorResponse},
        409: {"model": ErrorResponse},
    },
    response_model=LoginSuccessResponse,
    status_code=status.HTTP_200_OK,
)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    login_service: Annotated[LoginService, Depends(get_login_service)],
):
    return await login_service.login(form_data.username, form_data.password)


@router.post(
    "/refresh-token",
    responses={
        200: {"model": LoginSuccessResponse},
        401: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
    response_model=LoginSuccessResponse,
    status_code=status.HTTP_200_OK,
)
async def refresh_token(
    token: Annotated[str, Depends(oauth2_scheme)],
    refresh_token_service: Annotated[
        RefreshTokenService, Depends(get_refresh_token_service)
    ],
):
    return refresh_token_service.refresh(token)


@router.post(
    "/change-password",
    responses={
        200: {"model": UserBaseResponse},
        401: {"model": ErrorResponse},
        409: {"model": ErrorResponse},
    },
    response_model=UserBaseResponse,
    status_code=status.HTTP_200_OK,
)
async def change_password(
    request: PasswordChangeRequest,
    current_user: Annotated[CurrentUserDTO, Depends(get_current_user)],
    password_change_service: Annotated[
        PasswordChangeService, Depends(get_password_change_service)
    ],
):
    return await password_change_service.change_password(
        current_user.id, ChangePasswordDTO(**request.model_dump())
    )
