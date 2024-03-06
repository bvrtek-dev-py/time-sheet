from time_sheet.src.core.modules.project.dto.project import ProjectDTO
from time_sheet.src.core.modules.project.repositories.project_repository import (
    IProjectRepository,
)


class ProjectGetByIdUseCase:
    def __init__(self, repository: IProjectRepository):
        self._repository = repository

    async def execute(self, id: str) -> ProjectDTO:
        return await self._repository.get_by_id(id=id)
