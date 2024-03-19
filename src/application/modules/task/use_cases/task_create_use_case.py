from time_sheet.src.application.modules.task.dto.task import TaskCreateDTO
from time_sheet.src.core.modules.task.dto.task import TaskDTO
from time_sheet.src.core.modules.task.repositories.task_repository import (
    ITaskRepository,
)


class TaskCreateUseCase:
    def __init__(self, repository: ITaskRepository):
        self._repository = repository

    async def execute(self, request_dto: TaskCreateDTO) -> TaskDTO:
        task_dto = TaskDTO(**request_dto.model_dump(), _id=None)
        return await self._repository.save(task_dto)
