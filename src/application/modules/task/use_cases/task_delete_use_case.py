from time_sheet.src.application.modules.task.use_cases.task_get_by_id_use_case import (
    TaskGetByIdUseCase,
)
from time_sheet.src.core.modules.task.repositories.task_repository import (
    ITaskRepository,
)


class TaskDeleteUseCase:
    def __init__(
        self, repository: ITaskRepository, get_by_id_use_case: TaskGetByIdUseCase
    ):
        self._repository = repository
        self._get_by_id_use_case = get_by_id_use_case

    async def execute(self, task_id: str) -> None:
        await self._get_by_id_use_case.execute(task_id)

        return await self._repository.delete(task_id=task_id)
