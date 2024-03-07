from time_sheet.src.application.modules.project.use_cases.project_get_by_id_use_case import (
    ProjectGetByIdUseCase,
)
from time_sheet.src.core.modules.project.repositories.project_repository import (
    IProjectRepository,
)


class ProjectDeleteUseCase:
    def __init__(
        self, repository: IProjectRepository, get_by_id_use_case: ProjectGetByIdUseCase
    ):
        self._repository = repository
        self._get_by_id_use_case = get_by_id_use_case

    async def execute(self, id: str) -> None:
        await self._get_by_id_use_case.execute(id)

        return await self._repository.delete(id=id)
