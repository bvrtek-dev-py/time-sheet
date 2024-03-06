from abc import ABC, abstractmethod
from typing import List

from time_sheet.src.core.modules.project.dto.project import ProjectDTO


class IProjectRepository(ABC):
    @abstractmethod
    async def save(self, project: ProjectDTO) -> ProjectDTO:
        pass

    @abstractmethod
    async def get_all(self) -> List[ProjectDTO]:
        pass

    @abstractmethod
    async def get_by_id(self, id: str) -> ProjectDTO:
        pass

    @abstractmethod
    async def delete(self, id: str) -> None:
        ...

    @abstractmethod
    async def update(self, project: ProjectDTO) -> ProjectDTO:
        ...
