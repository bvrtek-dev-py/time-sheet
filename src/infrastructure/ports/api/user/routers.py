from typing import Annotated, List

from fastapi import APIRouter, Depends

from infrastructure.ports.api.common.responses import NoContentResponse
from time_sheet.src.application.modules.user.services.user_service import UserService
from time_sheet.src.application.modules.user.dto.user import (
    UserCreateDTO,
    UserUpdateDTO,
)
from time_sheet.src.application.modules.user.use_cases.user_create_use_case import (
    UserCreateUseCase,
)
from time_sheet.src.infrastructure.dependencies.user.factories import (
    get_user_create_use_case,
    get_user_service,
)
from time_sheet.src.infrastructure.ports.api.user.requests import (
    UserCreateRequest,
    UserUpdateRequest,
)
from time_sheet.src.infrastructure.ports.api.user.responses import UserBaseResponse

router = APIRouter(prefix="/api/v1/users", tags=["APIv1 User"])


@router.post("/", response_model=UserBaseResponse)
async def create_user(
    request: UserCreateRequest,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    return await user_service.create(UserCreateDTO(**request.model_dump()))


@router.put("/{id}", response_model=UserBaseResponse)
async def update_user(
    id: str,
    request: UserUpdateRequest,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    return await user_service.update(
        id=id, request_dto=UserUpdateDTO(**request.model_dump())
    )


@router.delete("/{id}")
async def delete_user(
    id: str,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    return await user_service.delete(id)


@router.get("/", response_model=List[UserBaseResponse])
async def get_all_users(
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    return await user_service.get_all()


@router.get("/{id}", response_model=UserBaseResponse)
async def get_by_id(
    id: str,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    return await user_service.get_by_id(id)
