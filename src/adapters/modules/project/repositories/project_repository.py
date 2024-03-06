from typing import List

from bson import ObjectId
from motor.core import AgnosticCollection
from motor.motor_asyncio import AsyncIOMotorClientSession

from core.modules.project.models.project import Project
from time_sheet.src.core.modules.project.dto.project import ProjectDTO
from time_sheet.src.core.modules.project.repositories.project_repository import (
    IProjectRepository,
)


class ProjectRepository(IProjectRepository):
    def __init__(self, session: AsyncIOMotorClientSession):
        self._session: AgnosticCollection = session.client.get_database()["projects"]

    async def save(self, project: ProjectDTO) -> ProjectDTO:
        model = Project(**project.model_dump())

        result = await self._session.insert_one(model.model_dump(exclude={"id"}))
        project.id = str(result.inserted_id)

        return project

    async def update(self, project: ProjectDTO) -> ProjectDTO:
        await self._session.update_one(
            {"_id": ObjectId(project.id)}, {"$set": project.model_dump(exclude={"id"})}
        )

        return project

    async def delete(self, id: str) -> None:
        await self._session.delete_one({"_id": ObjectId(id)})

    async def get_all(self) -> List[ProjectDTO]:
        documents = await self._session.find().to_list(length=None)

        return [
            ProjectDTO(**document | {"_id": str(document["_id"])})
            for document in documents
        ]

    async def get_by_id(self, id: str) -> ProjectDTO | None:
        document = await self._session.find_one({"_id": ObjectId(id)})

        return ProjectDTO(**document | {"_id": str(document["_id"])}) if document else None
