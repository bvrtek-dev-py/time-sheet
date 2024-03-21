from time_sheet.src.application.modules.project.dto.project import ProjectWithOwnerDTO
from time_sheet.src.core.modules.project.dto.project import ProjectDTO


class ProjectDTOToWithOwnerMapper:
    def map(self, dto: ProjectDTO) -> ProjectWithOwnerDTO:
        return ProjectWithOwnerDTO(**dto.model_dump())
