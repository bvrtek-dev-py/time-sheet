from time_sheet.src.application.modules.project.dto.project import ProjectWithOwnerDTO
from time_sheet.src.application.modules.user.use_cases.user_get_by_id_use_case import (
    UserGetByIdUseCase,
)
from time_sheet.src.application.modules.project.mapper.project_dto_to_with_owner_mapper import (
    ProjectDTOToWithOwnerMapper,
)
from time_sheet.src.application.modules.user.mapper.user_dto_to_get_mapper import (
    UserDTOToGetMapper,
)
from time_sheet.src.core.modules.project.dto.project import ProjectDTO


class ProjectLoadOwnerUseCase:
    def __init__(
        self,
        project_dto_to_with_owner_mapper: ProjectDTOToWithOwnerMapper,
        user_dto_to_get_mapper: UserDTOToGetMapper,
        user_get_by_id_use_case: UserGetByIdUseCase,
    ):
        self._project_dto_to_with_owner_mapper = project_dto_to_with_owner_mapper
        self._user_dto_to_get_mapper = user_dto_to_get_mapper
        self._user_get_by_id_use_case = user_get_by_id_use_case

    async def execute(self, project: ProjectDTO) -> ProjectWithOwnerDTO:
        user = await self._user_get_by_id_use_case.execute(project.owner_id)

        mapped_project = self._project_dto_to_with_owner_mapper.map(project)
        mapped_project.owner = self._user_dto_to_get_mapper.map(user)

        return mapped_project
