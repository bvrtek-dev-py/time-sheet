# pylint: disable=R0801, R0913
from typing import List

from time_sheet.src.application.modules.project.dto.project import (
    ProjectCreateDTO,
    ProjectUpdateDTO,
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
from time_sheet.src.application.modules.project.use_cases.project_update_use_case import (
    ProjectUpdateUseCase,
)
from time_sheet.src.core.modules.project.dto.project import ProjectDTO


class ProjectService:
    def __init__(
        self,
        create_use_case: ProjectCreateUseCase,
        delete_use_case: ProjectDeleteUseCase,
        update_use_case: ProjectUpdateUseCase,
        get_all_use_case: ProjectGetAllUseCase,
        get_by_id_use_case: ProjectGetByIdUseCase,
    ):
        self._create_use_case = create_use_case
        self._delete_use_case = delete_use_case
        self._update_use_case = update_use_case
        self._get_all_use_case = get_all_use_case
        self._get_by_id_use_case = get_by_id_use_case

    async def create(self, request_dto: ProjectCreateDTO) -> ProjectDTO:
        return await self._create_use_case.execute(request_dto)

    async def update(
        self, project_id: str, request_dto: ProjectUpdateDTO
    ) -> ProjectDTO:
        return await self._update_use_case.execute(
            request_dto=request_dto, project_id=project_id
        )

    async def delete(self, project_id: str) -> None:
        return await self._delete_use_case.execute(project_id)

    async def get_all(self) -> List[ProjectDTO]:
        return await self._get_all_use_case.execute()

    async def get_by_id(self, project_id: str) -> ProjectDTO:
        return await self._get_by_id_use_case.execute(project_id)
