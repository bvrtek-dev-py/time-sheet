from time_sheet.src.core.modules.project.repositories.project_repository import (
    IProjectRepository,
)


class ProjectDeleteUseCase:
    def __init__(self, repository: IProjectRepository):
        self._repository = repository

    async def execute(self, id: str) -> None:
        return await self._repository.delete(id=id)
