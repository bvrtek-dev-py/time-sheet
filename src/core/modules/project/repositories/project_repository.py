from abc import ABC, abstractmethod
from typing import List

from time_sheet.src.core.modules.project.dto.project import ProjectDTO


class IProjectRepository(ABC):
    @abstractmethod
    async def save(self, project: ProjectDTO) -> ProjectDTO:
        pass

    @abstractmethod
    async def get_all(self, name: str = None) -> List[ProjectDTO]:
        pass

    @abstractmethod
    async def get_by_id(self, project_id: str) -> ProjectDTO | None:
        pass

    @abstractmethod
    async def get_by_owner_id(self, owner_id: str) -> List[ProjectDTO]:
        pass

    @abstractmethod
    async def delete(self, project_id: str) -> None:
        pass

    @abstractmethod
    async def update(self, project: ProjectDTO) -> ProjectDTO:
        pass
