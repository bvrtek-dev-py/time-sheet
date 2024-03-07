# pylint: disable=R0801, R0913
from typing import List

from time_sheet.src.application.modules.user.dto.user import (
    UserCreateDTO,
    UserUpdateDTO,
)
from time_sheet.src.application.modules.user.use_cases.user_create_use_case import (
    UserCreateUseCase,
)
from time_sheet.src.application.modules.user.use_cases.user_delete_use_case import (
    UserDeleteUseCase,
)
from time_sheet.src.application.modules.user.use_cases.user_get_all_use_case import (
    UserGetAllUseCase,
)
from time_sheet.src.application.modules.user.use_cases.user_get_by_id_use_case import (
    UserGetByIdUseCase,
)
from time_sheet.src.application.modules.user.use_cases.user_update_use_case import (
    UserUpdateUseCase,
)
from time_sheet.src.core.modules.user.dto.user import UserDTO


class UserService:
    def __init__(
        self,
        create_use_case: UserCreateUseCase,
        delete_use_case: UserDeleteUseCase,
        update_use_case: UserUpdateUseCase,
        get_all_use_case: UserGetAllUseCase,
        get_by_id_use_case: UserGetByIdUseCase,
    ):
        self._create_use_case = create_use_case
        self._delete_use_case = delete_use_case
        self._update_use_case = update_use_case
        self._get_all_use_case = get_all_use_case
        self._get_by_id_use_case = get_by_id_use_case

    async def create(self, request_dto: UserCreateDTO) -> UserDTO:
        return await self._create_use_case.execute(request_dto)

    async def update(self, user_id: str, request_dto: UserUpdateDTO) -> UserDTO:
        return await self._update_use_case.execute(
            request_dto=request_dto, user_id=user_id
        )

    async def delete(self, user_id: str) -> None:
        return await self._delete_use_case.execute(user_id)

    async def get_all(self) -> List[UserDTO]:
        return await self._get_all_use_case.execute()

    async def get_by_id(self, user_id: str) -> UserDTO:
        return await self._get_by_id_use_case.execute(user_id)
