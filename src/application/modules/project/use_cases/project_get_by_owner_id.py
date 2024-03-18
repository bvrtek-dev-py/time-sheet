from typing import List

from time_sheet.src.core.modules.project.dto.project import ProjectDTO
from time_sheet.src.core.modules.project.repositories.project_repository import (
    IProjectRepository,
)


class ProjectGetByOwnerIdUseCase:
    def __init__(self, repository: IProjectRepository):
        self._repository = repository

    async def execute(self, owner_id: str) -> List[ProjectDTO]:
        return await self._repository.get_by_owner_id(owner_id)
