from time_sheet.src.application.modules.user.dto.user import UserGetDTO
from time_sheet.src.core.modules.user.dto.user import UserDTO


class UserDTOToGetMapper:
    def map(self, dto: UserDTO) -> UserGetDTO:
        return UserGetDTO(**dto.model_dump())
