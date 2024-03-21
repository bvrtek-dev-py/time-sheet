# pylint: disable=R0801, R0913
from typing import List

from time_sheet.src.application.modules.project.dto.project import (
    ProjectCreateDTO,
    ProjectUpdateDTO,
    ProjectWithOwnerDTO,
)
from time_sheet.src.application.modules.project.use_cases.project_create_use_case import (
    ProjectCreateUseCase,
)
from time_sheet.src.application.modules.project.use_cases.project_delete_use_case import (
    ProjectDeleteUseCase,
)
from time_sheet.src.application.modules.project.use_cases.project_get_all_use_case import (
    ProjectGetAllUseCase,
)
from time_sheet.src.application.modules.project.use_cases.project_get_by_id_use_case import (
    ProjectGetByIdUseCase,
)
from time_sheet.src.application.modules.project.use_cases.project_get_by_owner_id import (
    ProjectGetByOwnerIdUseCase,
)
from time_sheet.src.application.modules.project.use_cases.project_load_owner_use_case import (
    ProjectLoadOwnerUseCase,
)
from time_sheet.src.application.modules.project.use_cases.project_update_use_case import (
    ProjectUpdateUseCase,
)


class ProjectService:
    def __init__(
        self,
        create_use_case: ProjectCreateUseCase,
        delete_use_case: ProjectDeleteUseCase,
        update_use_case: ProjectUpdateUseCase,
        get_all_use_case: ProjectGetAllUseCase,
        get_by_id_use_case: ProjectGetByIdUseCase,
        get_by_owner_id: ProjectGetByOwnerIdUseCase,
        load_owner_use_case: ProjectLoadOwnerUseCase,
    ):
        self._create_use_case = create_use_case
        self._delete_use_case = delete_use_case
        self._update_use_case = update_use_case
        self._get_all_use_case = get_all_use_case
        self._get_by_id_use_case = get_by_id_use_case
        self._get_by_owner_id = get_by_owner_id
        self._load_owner_use_case = load_owner_use_case

    async def create(self, request_dto: ProjectCreateDTO) -> ProjectWithOwnerDTO:
        project = await self._create_use_case.execute(request_dto)

        return await self._load_owner_use_case.execute(project)

    async def update(
        self, project_id: str, request_dto: ProjectUpdateDTO
    ) -> ProjectWithOwnerDTO:
        project = await self._update_use_case.execute(
            request_dto=request_dto, project_id=project_id
        )

        return await self._load_owner_use_case.execute(project)

    async def delete(self, project_id: str) -> None:
        return await self._delete_use_case.execute(project_id)

    async def get_all(self) -> List[ProjectWithOwnerDTO]:
        projects = await self._get_all_use_case.execute()

        return [
            await self._load_owner_use_case.execute(project) for project in projects
        ]

    async def get_by_id(self, project_id: str) -> ProjectWithOwnerDTO:
        project = await self._get_by_id_use_case.execute(project_id)

        return await self._load_owner_use_case.execute(project)

    async def get_by_owner_id(self, owner_id: str) -> List[ProjectWithOwnerDTO]:
        projects = await self._get_by_owner_id.execute(owner_id)

        return [
            await self._load_owner_use_case.execute(project) for project in projects
        ]
