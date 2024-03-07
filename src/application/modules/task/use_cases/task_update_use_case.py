from time_sheet.src.application.modules.task.dto.task import (
    TaskUpdateDTO,
)
from time_sheet.src.application.modules.task.use_cases.task_get_by_id_use_case import (
    TaskGetByIdUseCase,
)
from time_sheet.src.core.modules.task.dto.task import TaskDTO
from time_sheet.src.core.modules.task.repositories.task_repository import (
    ITaskRepository,
)


class TaskUpdateUseCase:
    def __init__(
        self, repository: ITaskRepository, get_by_id_use_case: TaskGetByIdUseCase
    ):
        self._repository = repository
        self._get_by_id_use_case = get_by_id_use_case

    async def execute(self, request_dto: TaskUpdateDTO, task_id: str) -> TaskDTO:
        task_dto = await self._get_by_id_use_case.execute(task_id)
        task_dto.name = request_dto.name
        task_dto.start = request_dto.start
        task_dto.end = request_dto.end
        task_dto.additional_information = request_dto.additional_information

        return await self._repository.update(task_dto)
