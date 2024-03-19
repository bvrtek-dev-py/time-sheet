from typing import Annotated, List

from fastapi import APIRouter, Depends, status

from time_sheet.src.application.modules.task.dto.task import (
    TaskCreateDTO,
    TaskUpdateDTO,
)
from time_sheet.src.application.modules.task.services.task_service import TaskService
from time_sheet.src.core.modules.auth.dto.auth import CurrentUserDTO
from time_sheet.src.infrastructure.dependencies.auth.permissions import get_current_user
from time_sheet.src.infrastructure.dependencies.task.factories import (
    get_task_service,
)
from time_sheet.src.infrastructure.ports.api.v1.common.responses import ErrorResponse
from time_sheet.src.infrastructure.ports.api.v1.task.requests import (
    TaskCreateRequest,
    TaskUpdateRequest,
)
from time_sheet.src.infrastructure.ports.api.v1.task.responses import TaskBaseResponse

router = APIRouter(prefix="/api/v1/tasks", tags=["APIv1 Task"])


@router.post(
    "/",
    response_model=TaskBaseResponse,
    responses={
        201: {"model": TaskBaseResponse},
        404: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
    },
    status_code=status.HTTP_201_CREATED,
)
async def create_task(
    current_user: Annotated[CurrentUserDTO, Depends(get_current_user)],
    request: TaskCreateRequest,
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    return await task_service.create(
        TaskCreateDTO(**request.model_dump() | {"owner_id": current_user.id})
    )


@router.put(
    "/{task_id}",
    response_model=TaskBaseResponse,
    responses={200: {"model": TaskBaseResponse}, 404: {"model": ErrorResponse}},
    status_code=status.HTTP_200_OK,
)
async def update_task(
    task_id: str,
    request: TaskUpdateRequest,
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    return await task_service.update(
        task_id=task_id, request_dto=TaskUpdateDTO(**request.model_dump())
    )


@router.delete(
    "/{task_id}",
    responses={204: {"model": None}, 404: {"model": ErrorResponse}},
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_task(
    task_id: str,
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    return await task_service.delete(task_id)


@router.get(
    "/",
    response_model=List[TaskBaseResponse],
    responses={200: {"model": List[TaskBaseResponse]}},
    status_code=status.HTTP_200_OK,
)
async def get_all_tasks(
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    return await task_service.get_all()


@router.get(
    "/owned/",
    response_model=List[TaskBaseResponse],
    responses={
        200: {"model": List[TaskBaseResponse]},
        401: {"model": ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
)
async def get_by_owner_id_tasks(
    current_user: Annotated[CurrentUserDTO, Depends(get_current_user)],
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    return await task_service.get_by_owner_id(current_user.id)


@router.get(
    "/{task_id}",
    response_model=TaskBaseResponse,
    responses={200: {"model": TaskBaseResponse}, 404: {"model": ErrorResponse}},
    status_code=status.HTTP_200_OK,
)
async def get_by_id(
    task_id: str,
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    return await task_service.get_by_id(task_id)
