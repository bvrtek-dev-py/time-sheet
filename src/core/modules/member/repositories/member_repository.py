# pylint: disable=R0801
from abc import ABC, abstractmethod
from typing import List

from time_sheet.src.core.modules.member.dto.member import MemberDTO


class IMemberRepository(ABC):
    @abstractmethod
    async def save(self, member: MemberDTO) -> MemberDTO:
        pass

    @abstractmethod
    async def get_all_for_project(
        self, project_id: str, status: str | None = None
    ) -> List[MemberDTO]:
        pass

    @abstractmethod
    async def get_by_id(self, member_id: str) -> MemberDTO | None:
        pass

    @abstractmethod
    async def get_by_user_id(self, user_id: str) -> List[MemberDTO]:
        pass

    @abstractmethod
    async def delete(self, member_id: str) -> None:
        pass

    @abstractmethod
    async def patch(self, member: MemberDTO) -> MemberDTO:
        pass
