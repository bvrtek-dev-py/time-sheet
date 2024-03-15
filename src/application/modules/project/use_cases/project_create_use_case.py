from time_sheet.src.application.modules.project.dto.project import ProjectCreateDTO
from time_sheet.src.core.modules.project.dto.project import ProjectDTO
from time_sheet.src.core.modules.project.repositories.project_repository import (
    IProjectRepository,
)


class ProjectCreateUseCase:
    def __init__(self, repository: IProjectRepository):
        self._repository = repository

    async def execute(self, owner_id: str, request_dto: ProjectCreateDTO) -> ProjectDTO:
        project_dto = ProjectDTO(**request_dto.dict(), _id=None, owner_id=owner_id)
        return await self._repository.save(project_dto)
