# pylint: disable=R0801, R0913
from typing import List
from time_sheet.src.application.modules.task.dto.task import (
    TaskCreateDTO,
    TaskUpdateDTO,
)
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
from time_sheet.src.core.modules.task.dto.task import TaskDTO


class TaskService:
    def __init__(
        self,
        create_use_case: TaskCreateUseCase,
        delete_use_case: TaskDeleteUseCase,
        update_use_case: TaskUpdateUseCase,
        get_all_use_case: TaskGetAllUseCase,
        get_by_id_use_case: TaskGetByIdUseCase,
        get_by_owner_id_use_case: TaskGetByOwnerIdUseCase,
    ):
        self._create_use_case = create_use_case
        self._delete_use_case = delete_use_case
        self._update_use_case = update_use_case
        self._get_all_use_case = get_all_use_case
        self._get_by_id_use_case = get_by_id_use_case
        self._get_by_owner_id_use_case = get_by_owner_id_use_case

    async def create(self, request_dto: TaskCreateDTO) -> TaskDTO:
        return await self._create_use_case.execute(request_dto)

    async def update(self, task_id: str, request_dto: TaskUpdateDTO) -> TaskDTO:
        return await self._update_use_case.execute(
            request_dto=request_dto, task_id=task_id
        )

    async def delete(self, task_id: str) -> None:
        return await self._delete_use_case.execute(task_id)

    async def get_all(self) -> List[TaskDTO]:
        return await self._get_all_use_case.execute()

    async def get_by_id(self, task_id: str) -> TaskDTO:
        return await self._get_by_id_use_case.execute(task_id)

    async def get_by_owner_id(self, owner_id: str) -> List[TaskDTO]:
        return await self._get_by_owner_id_use_case.execute(owner_id)
