# pylint: disable=R0913
from typing import Annotated

from fastapi import Depends
from motor.core import AgnosticClientSession

from time_sheet.src.adapters.modules.project.repositories.project_repository import (
    ProjectRepository,
)
from time_sheet.src.application.modules.project.services.project_service import (
    ProjectService,
)
from time_sheet.src.application.modules.project.use_cases.project_create_use_case import (
    ProjectCreateUseCase,
)
from time_sheet.src.application.modules.project.use_cases.project_delete_use_case import (
    ProjectDeleteUseCase,
)
from time_sheet.src.application.modules.project.use_cases.project_get_by_owner_id import (
    ProjectGetByOwnerIdUseCase,
)
from time_sheet.src.application.modules.project.use_cases.project_get_all_use_case import (
    ProjectGetAllUseCase,
)
from time_sheet.src.application.modules.project.use_cases.project_get_by_id_use_case import (
    ProjectGetByIdUseCase,
)
from time_sheet.src.application.modules.project.use_cases.project_update_use_case import (
    ProjectUpdateUseCase,
)
from time_sheet.src.application.modules.user.services.user_service import UserService
from time_sheet.src.core.modules.project.repositories.project_repository import (
    IProjectRepository,
)
from time_sheet.src.infrastructure.dependencies.database.setup import get_session
from time_sheet.src.infrastructure.dependencies.user.factories import get_user_service


def get_project_repository(
    session: Annotated[AgnosticClientSession, Depends(get_session)]
) -> IProjectRepository:
    return ProjectRepository(session)


def get_project_create_use_case(
    repository: Annotated[IProjectRepository, Depends(get_project_repository)]
) -> ProjectCreateUseCase:
    return ProjectCreateUseCase(repository)


def get_project_get_by_id_use_case(
    repository: Annotated[IProjectRepository, Depends(get_project_repository)]
) -> ProjectGetByIdUseCase:
    return ProjectGetByIdUseCase(repository)


def get_project_get_all_use_case(
    repository: Annotated[IProjectRepository, Depends(get_project_repository)]
) -> ProjectGetAllUseCase:
    return ProjectGetAllUseCase(repository)


def get_project_get_by_owner_id_use_case(
    repository: Annotated[IProjectRepository, Depends(get_project_repository)]
) -> ProjectGetByOwnerIdUseCase:
    return ProjectGetByOwnerIdUseCase(repository)


def get_project_update_use_case(
    repository: Annotated[IProjectRepository, Depends(get_project_repository)],
    get_by_id_use_case: Annotated[
        ProjectGetByIdUseCase, Depends(get_project_get_by_id_use_case)
    ],
) -> ProjectUpdateUseCase:
    return ProjectUpdateUseCase(
        repository=repository, get_by_id_use_case=get_by_id_use_case
    )


def get_project_delete_use_case(
    repository: Annotated[IProjectRepository, Depends(get_project_repository)],
    get_by_id_use_case: Annotated[
        ProjectGetByIdUseCase, Depends(get_project_get_by_id_use_case)
    ],
) -> ProjectDeleteUseCase:
    return ProjectDeleteUseCase(
        repository=repository, get_by_id_use_case=get_by_id_use_case
    )


def get_project_service(
    project_create_use_case: Annotated[
        ProjectCreateUseCase, Depends(get_project_create_use_case)
    ],
    project_update_use_case: Annotated[
        ProjectUpdateUseCase, Depends(get_project_update_use_case)
    ],
    project_delete_use_case: Annotated[
        ProjectDeleteUseCase, Depends(get_project_delete_use_case)
    ],
    project_get_by_id_use_case: Annotated[
        ProjectGetByIdUseCase, Depends(get_project_get_by_id_use_case)
    ],
    project_get_all_use_case: Annotated[
        ProjectGetAllUseCase, Depends(get_project_get_all_use_case)
    ],
    project_get_by_owner_id_use_case: Annotated[
        ProjectGetByOwnerIdUseCase, Depends(get_project_get_by_owner_id_use_case)
    ],
    user_service: Annotated[UserService, Depends(get_user_service)],
) -> ProjectService:
    return ProjectService(
        create_use_case=project_create_use_case,
        update_use_case=project_update_use_case,
        delete_use_case=project_delete_use_case,
        get_all_use_case=project_get_all_use_case,
        get_by_id_use_case=project_get_by_id_use_case,
        get_by_owner_id=project_get_by_owner_id_use_case,
        user_service=user_service,
    )
