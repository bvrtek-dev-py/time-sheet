from time_sheet.src.core.modules.common.exceptions.domain import ObjectDoesNotExist

from time_sheet.src.core.modules.task.dto.task import TaskDTO
from time_sheet.src.core.modules.task.repositories.task_repository import (
    ITaskRepository,
)


class TaskGetByIdUseCase:
    def __init__(self, repository: ITaskRepository):
        self._repository = repository

    async def execute(self, task_id: str) -> TaskDTO:
        task = await self._repository.get_by_id(task_id=task_id)

        if task is None:
            raise ObjectDoesNotExist

        return task
