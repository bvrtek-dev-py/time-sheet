from typing import Annotated, List

from fastapi import APIRouter, Depends, status

from time_sheet.src.infrastructure.ports.api.v1.common.responses import (
    NoContentResponse,
)
from time_sheet.src.application.modules.project.services.project_service import (
    ProjectService,
)
from time_sheet.src.application.modules.project.dto.project import (
    ProjectCreateDTO,
    ProjectUpdateDTO,
)
from time_sheet.src.infrastructure.dependencies.project.factories import (
    get_project_service,
)
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
    responses={201: {"model": ProjectBaseResponse}},
    status_code=status.HTTP_201_CREATED,
)
async def create_project(
    request: ProjectCreateRequest,
    project_service: Annotated[ProjectService, Depends(get_project_service)],
):
    return await project_service.create(ProjectCreateDTO(**request.model_dump()))


@router.put(
    "/{id}",
    response_model=ProjectBaseResponse,
    responses={200: {"model": ProjectBaseResponse}},
    status_code=status.HTTP_200_OK,
)
async def update_project(
    id: str,
    request: ProjectUpdateRequest,
    project_service: Annotated[ProjectService, Depends(get_project_service)],
):
    return await project_service.update(
        id=id, request_dto=ProjectUpdateDTO(**request.model_dump())
    )


@router.delete(
    "/{id}",
    responses={204: {"model": NoContentResponse}},
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_project(
    id: str,
    project_service: Annotated[ProjectService, Depends(get_project_service)],
):
    return await project_service.delete(id)


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
    "/{id}",
    response_model=ProjectBaseResponse,
    responses={200: {"model": ProjectBaseResponse}},
    status_code=status.HTTP_200_OK,
)
async def get_by_id(
    id: str,
    project_service: Annotated[ProjectService, Depends(get_project_service)],
):
    return await project_service.get_by_id(id)