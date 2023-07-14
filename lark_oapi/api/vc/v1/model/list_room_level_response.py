# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_room_level_response_body import ListRoomLevelResponseBody


class ListRoomLevelResponse(BaseResponse):
    _types = {
        "data": ListRoomLevelResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListRoomLevelResponseBody] = None
        init(self, d, self._types)