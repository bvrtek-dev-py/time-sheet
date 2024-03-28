from typing import Optional

from pydantic import BaseModel, Field

from time_sheet.src.core.modules.member.enum.member_status import MemberStatus


class MemberDTO(BaseModel):
    id: Optional[str] = Field(alias="_id")
    user_id: str
    project_id: str
    status: MemberStatus
