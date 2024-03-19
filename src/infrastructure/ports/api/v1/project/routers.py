from typing import Annotated, List

from fastapi import APIRouter, Depends, status

from time_sheet.src.application.modules.project.dto.project import (
    ProjectCreateDTO,
    ProjectUpdateDTO,
)
from time_sheet.src.application.modules.project.services.project_service import (
    ProjectService,
)
from time_sheet.src.core.modules.auth.dto.auth import CurrentUserDTO
from time_sheet.src.infrastructure.dependencies.auth.permissions import get_current_user
from time_sheet.src.infrastructure.dependencies.project.factories import (
    get_project_service,
)
from time_sheet.src.infrastructure.ports.api.v1.common.responses import ErrorResponse
from time_sheet.src.infrastructure.ports.api.v1.project.requests import (
    ProjectCreateRequest,
    ProjectUpdateRequest,
)
from time_sheet.src.infrastructure.ports.api.v1.project.responses import (
    ProjectBaseResponse,
)

router = APIRouter(prefix="/api/v1/projects", tags=["APIv1 Project"])


@router.post(
    "/",
    response_model=ProjectBaseResponse,
    responses={
        201: {"model": ProjectBaseResponse},
        404: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
    },
    status_code=status.HTTP_201_CREATED,
)
async def create_project(
    current_user: Annotated[CurrentUserDTO, Depends(get_current_user)],
    request: ProjectCreateRequest,
    project_service: Annotated[ProjectService, Depends(get_project_service)],
):
    return await project_service.create(
        ProjectCreateDTO(**request.dict(), owner_id=current_user.id)
    )


@router.put(
    "/{project_id}",
    response_model=ProjectBaseResponse,
    responses={
        200: {"model": ProjectBaseResponse},
        404: {"model": ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
)
async def update_project(
    project_id: str,
    request: ProjectUpdateRequest,
    project_service: Annotated[ProjectService, Depends(get_project_service)],
):
    return await project_service.update(
        project_id=project_id, request_dto=ProjectUpdateDTO(**request.model_dump())
    )


@router.delete(
    "/{project_id}",
    responses={204: {"model": None}, 404: {"model": ErrorResponse}},
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_project(
    project_id: str,
    project_service: Annotated[ProjectService, Depends(get_project_service)],
):
    return await project_service.delete(project_id)


@router.get(
    "/owned/",
    response_model=List[ProjectBaseResponse],
    responses={
        200: {"model": List[ProjectBaseResponse]},
        401: {"model": ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
)
async def get_by_owner_id_projects(
    current_user: Annotated[CurrentUserDTO, Depends(get_current_user)],
    project_service: Annotated[ProjectService, Depends(get_project_service)],
):
    return await project_service.get_by_owner_id(current_user.id)


@router.get(
    "/",
    response_model=List[ProjectBaseResponse],
    responses={200: {"model": List[ProjectBaseResponse]}},
    status_code=status.HTTP_200_OK,
)
async def get_all_projects(
    project_service: Annotated[ProjectService, Depends(get_project_service)],
):
    return await project_service.get_all()


@router.get(
    "/{project_id}",
    response_model=ProjectBaseResponse,
    responses={200: {"model": ProjectBaseResponse}, 404: {"model": ErrorResponse}},
    status_code=status.HTTP_200_OK,
)
async def get_by_id(
    project_id: str,
    project_service: Annotated[ProjectService, Depends(get_project_service)],
):
    return await project_service.get_by_id(project_id)
