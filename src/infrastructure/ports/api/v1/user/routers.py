from typing import Annotated, List

from fastapi import APIRouter, Depends, status

from time_sheet.src.infrastructure.ports.api.v1.common.responses import ErrorResponse
from time_sheet.src.application.modules.user.dto.user import (
    UserCreateDTO,
    UserUpdateDTO,
)
from time_sheet.src.application.modules.user.services.user_service import UserService
from time_sheet.src.infrastructure.dependencies.user.factories import (
    get_user_service,
)
from time_sheet.src.infrastructure.ports.api.v1.user.requests import (
    UserCreateRequest,
    UserUpdateRequest,
)
from time_sheet.src.infrastructure.ports.api.v1.user.responses import UserBaseResponse

router = APIRouter(prefix="/api/v1/users", tags=["APIv1 User"])


@router.post(
    "/",
    response_model=UserBaseResponse,
    responses={201: {"model": UserBaseResponse}},
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    request: UserCreateRequest,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    return await user_service.create(UserCreateDTO(**request.model_dump()))


@router.put(
    "/{user_id}",
    response_model=UserBaseResponse,
    responses={200: {"model": UserBaseResponse}, 404: {"model": ErrorResponse}},
    status_code=status.HTTP_200_OK,
)
async def update_user(
    user_id: str,
    request: UserUpdateRequest,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    return await user_service.update(
        user_id=user_id, request_dto=UserUpdateDTO(**request.model_dump())
    )


@router.delete(
    "/{user_id}",
    responses={204: {"model": None}, 404: {"model": ErrorResponse}},
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    user_id: str,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    return await user_service.delete(user_id)


@router.get(
    "/",
    response_model=List[UserBaseResponse],
    responses={200: {"model": List[UserBaseResponse]}},
    status_code=status.HTTP_200_OK,
)
async def get_all_users(
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    return await user_service.get_all()


@router.get(
    "/{user_id}",
    response_model=UserBaseResponse,
    responses={200: {"model": UserBaseResponse}, 404: {"model": ErrorResponse}},
    status_code=status.HTTP_200_OK,
)
async def get_by_id(
    user_id: str,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    return await user_service.get_by_id(user_id)
