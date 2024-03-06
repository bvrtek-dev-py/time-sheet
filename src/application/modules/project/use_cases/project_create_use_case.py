from time_sheet.src.application.modules.project.dto.project import ProjectCreateDTO
from time_sheet.src.core.modules.project.dto.project import ProjectDTO
from time_sheet.src.core.modules.project.repositories.project_repository import (
    IProjectRepository,
)


class ProjectCreateUseCase:
    def __init__(self, repository: IProjectRepository):
        self._repository = repository

    async def execute(self, request_dto: ProjectCreateDTO) -> ProjectDTO:
        return await self._repository.save(
            ProjectDTO(**request_dto.model_dump(), _id=None)
        )
