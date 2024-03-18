from time_sheet.src.application.modules.task.dto.task import TaskCreateDTO
from time_sheet.src.core.modules.task.dto.task import TaskDTO
from time_sheet.src.core.modules.task.repositories.task_repository import (
    ITaskRepository,
)


class TaskCreateUseCase:
    def __init__(self, repository: ITaskRepository):
        self._repository = repository

    async def execute(self, owner_id: str, request_dto: TaskCreateDTO) -> TaskDTO:
        project_dto = TaskDTO(**request_dto.dict(), _id=None, owner_id=owner_id)
        return await self._repository.save(project_dto)
