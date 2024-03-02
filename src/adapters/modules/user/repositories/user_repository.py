from typing import List

from bson import ObjectId
from motor.core import AgnosticCollection
from motor.motor_asyncio import AsyncIOMotorClientSession

from core.modules.user.models.user import User
from time_sheet.src.core.modules.user.dto.user import UserDTO
from time_sheet.src.core.modules.user.repositories.user_repository import (
    IUserRepository,
)


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncIOMotorClientSession):
        self._session: AgnosticCollection = session.client.get_database()["users"]

    async def save(self, user: UserDTO) -> UserDTO:
        model = User(**user.model_dump())

        result = await self._session.insert_one(model.model_dump(exclude={"id"}))
        user.id = str(result.inserted_id)

        return user

    async def update(self, user: UserDTO) -> UserDTO:
        await self._session.update_one(
            {"_id": ObjectId(user.id)}, {"$set": user.model_dump(exclude={"id"})}
        )

        return user

    async def delete(self, id: str) -> None:
        await self._session.delete_one({"_id": ObjectId(id)})

    async def get_all(self) -> List[UserDTO]:
        documents = await self._session.find().to_list(length=None)

        return [
            UserDTO(**document | {"_id": str(document["_id"])})
            for document in documents
        ]

    async def get_by_id(self, id: str) -> UserDTO | None:
        document = await self._session.find_one({"_id": ObjectId(id)})

        return UserDTO(**document | {"_id": str(document["_id"])}) if document else None
