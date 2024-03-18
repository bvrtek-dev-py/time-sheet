from typing import List

from time_sheet.src.core.modules.task.dto.task import TaskDTO
from time_sheet.src.core.modules.task.repositories.task_repository import (
    ITaskRepository,
)


class TaskGetByOwnerIdUseCase:
    def __init__(self, repository: ITaskRepository):
        self._repository = repository

    async def execute(self, owner_id: str) -> List[TaskDTO]:
        return await self._repository.get_by_owner_id(owner_id)
