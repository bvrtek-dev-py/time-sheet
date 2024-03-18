# pylint: disable=R0913
from typing import Annotated

from fastapi import Depends
from motor.core import AgnosticClientSession

from time_sheet.src.adapters.modules.task.repositories.task_repository import (
    TaskRepository,
)
from time_sheet.src.application.modules.task.services.task_service import TaskService
from time_sheet.src.application.modules.task.use_cases.task_create_use_case import (
    TaskCreateUseCase,
)
from time_sheet.src.application.modules.task.use_cases.task_delete_use_case import (
    TaskDeleteUseCase,
)
from time_sheet.src.application.modules.task.use_cases.task_get_all_use_case import (
    TaskGetAllUseCase,
)
from time_sheet.src.application.modules.task.use_cases.task_get_by_id_use_case import (
    TaskGetByIdUseCase,
)
from time_sheet.src.application.modules.task.use_cases.task_get_by_owner_id import (
    TaskGetByOwnerIdUseCase,
)
from time_sheet.src.application.modules.task.use_cases.task_update_use_case import (
    TaskUpdateUseCase,
)
from time_sheet.src.core.modules.task.repositories.task_repository import (
    ITaskRepository,
)
from time_sheet.src.infrastructure.dependencies.database.setup import get_session


def get_task_repository(
    session: Annotated[AgnosticClientSession, Depends(get_session)]
) -> ITaskRepository:
    return TaskRepository(session)


def get_task_create_use_case(
    repository: Annotated[ITaskRepository, Depends(get_task_repository)]
) -> TaskCreateUseCase:
    return TaskCreateUseCase(repository)


def get_task_get_by_id_use_case(
    repository: Annotated[ITaskRepository, Depends(get_task_repository)]
) -> TaskGetByIdUseCase:
    return TaskGetByIdUseCase(repository)


def get_task_get_all_use_case(
    repository: Annotated[ITaskRepository, Depends(get_task_repository)]
) -> TaskGetAllUseCase:
    return TaskGetAllUseCase(repository)


def get_task_get_by_owner_id_use_case(
    repository: Annotated[ITaskRepository, Depends(get_task_repository)]
) -> TaskGetByOwnerIdUseCase:
    return TaskGetByOwnerIdUseCase(repository)


def get_task_update_use_case(
    repository: Annotated[ITaskRepository, Depends(get_task_repository)],
    get_by_id_use_case: Annotated[
        TaskGetByIdUseCase, Depends(get_task_get_by_id_use_case)
    ],
) -> TaskUpdateUseCase:
    return TaskUpdateUseCase(
        repository=repository, get_by_id_use_case=get_by_id_use_case
    )


def get_task_delete_use_case(
    repository: Annotated[ITaskRepository, Depends(get_task_repository)],
    get_by_id_use_case: Annotated[
        TaskGetByIdUseCase, Depends(get_task_get_by_id_use_case)
    ],
) -> TaskDeleteUseCase:
    return TaskDeleteUseCase(
        repository=repository, get_by_id_use_case=get_by_id_use_case
    )


def get_task_service(
    task_create_use_case: Annotated[
        TaskCreateUseCase, Depends(get_task_create_use_case)
    ],
    task_update_use_case: Annotated[
        TaskUpdateUseCase, Depends(get_task_update_use_case)
    ],
    task_delete_use_case: Annotated[
        TaskDeleteUseCase, Depends(get_task_delete_use_case)
    ],
    task_get_by_id_use_case: Annotated[
        TaskGetByIdUseCase, Depends(get_task_get_by_id_use_case)
    ],
    task_get_all_use_case: Annotated[
        TaskGetAllUseCase, Depends(get_task_get_all_use_case)
    ],
    task_get_by_owner_id_use_case: Annotated[
        TaskGetByOwnerIdUseCase, Depends(get_task_get_by_owner_id_use_case)
    ],
) -> TaskService:
    return TaskService(
        create_use_case=task_create_use_case,
        update_use_case=task_update_use_case,
        delete_use_case=task_delete_use_case,
        get_all_use_case=task_get_all_use_case,
        get_by_id_use_case=task_get_by_id_use_case,
        get_by_owner_id_use_case=task_get_by_owner_id_use_case,
    )
