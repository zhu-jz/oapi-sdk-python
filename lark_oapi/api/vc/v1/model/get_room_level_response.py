# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_room_level_response_body import GetRoomLevelResponseBody


class GetRoomLevelResponse(BaseResponse):
    _types = {
        "data": GetRoomLevelResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetRoomLevelResponseBody] = None
        init(self, d, self._types)