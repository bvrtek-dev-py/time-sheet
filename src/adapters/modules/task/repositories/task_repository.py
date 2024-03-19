from typing import List
from bson import ObjectId
from motor.core import AgnosticCollection, AgnosticClientSession
from time_sheet.src.core.modules.task.dto.task import TaskDTO
from time_sheet.src.core.modules.task.models.task import Task
from time_sheet.src.core.modules.task.repositories.task_repository import (
    ITaskRepository,
)


class TaskRepository(ITaskRepository):
    def __init__(self, session: AgnosticClientSession):
        self._session: AgnosticCollection = session.client.get_database()[  # type: ignore
            "tasks"
        ]

    async def save(self, task: TaskDTO) -> TaskDTO:
        model = Task(**task.model_dump())

        result = await self._session.insert_one(model.model_dump(exclude={"id"}))
        task.id = str(result.inserted_id)

        return task

    async def update(self, task: TaskDTO) -> TaskDTO:
        await self._session.update_one(
            {"_id": ObjectId(task.id)}, {"$set": task.model_dump(exclude={"id"})}
        )

        return task

    async def delete(self, task_id: str) -> None:
        await self._session.delete_one({"_id": ObjectId(task_id)})

    async def get_all(self) -> List[TaskDTO]:
        documents = await self._session.find().to_list(length=None)

        return [
            TaskDTO(**document | {"_id": str(document["_id"])})
            for document in documents
        ]

    async def get_by_id(self, task_id: str) -> TaskDTO | None:
        document = await self._session.find_one({"_id": ObjectId(task_id)})

        return TaskDTO(**document | {"_id": str(document["_id"])}) if document else None

    async def get_by_owner_id(self, owner_id: str) -> List[TaskDTO]:
        documents = await self._session.find({"owner_id": owner_id}).to_list(
            length=None
        )

        return [
            TaskDTO(**document | {"_id": str(document["_id"])})
            for document in documents
        ]
