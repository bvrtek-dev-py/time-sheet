from typing import Annotated

from fastapi import Depends

from time_sheet.src.application.modules.auth.services.token_service import TokenService
from time_sheet.src.core.modules.auth.dto.auth import CurrentUserDTO
from time_sheet.src.infrastructure.dependencies.auth.creators import get_token_service
from time_sheet.src.settings.oauth2 import oauth2_scheme


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    token_service: Annotated[TokenService, Depends(get_token_service)],
) -> CurrentUserDTO:
    return token_service.decode(token)
