# pylint: disable=R0801
from abc import ABC, abstractmethod
from typing import List
from time_sheet.src.core.modules.task.dto.task import TaskDTO


class ITaskRepository(ABC):
    @abstractmethod
    async def save(self, task: TaskDTO) -> TaskDTO:
        pass

    @abstractmethod
    async def get_all(self) -> List[TaskDTO]:
        pass

    @abstractmethod
    async def get_by_id(self, task_id: str) -> TaskDTO | None:
        pass

    @abstractmethod
    async def get_by_owner_id(self, owner_id: str) -> List[TaskDTO]:
        pass

    @abstractmethod
    async def delete(self, task_id: str) -> None:
        pass

    @abstractmethod
    async def update(self, task: TaskDTO) -> TaskDTO:
        pass
