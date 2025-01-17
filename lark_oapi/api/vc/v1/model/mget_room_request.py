# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .mget_room_request_body import MgetRoomRequestBody


class MgetRoomRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[MgetRoomRequestBody] = None

    @staticmethod
    def builder() -> "MgetRoomRequestBuilder":
        return MgetRoomRequestBuilder()


class MgetRoomRequestBuilder(object):

    def __init__(self) -> None:
        mget_room_request = MgetRoomRequest()
        mget_room_request.http_method = HttpMethod.POST
        mget_room_request.uri = "/open-apis/vc/v1/rooms/mget"
        mget_room_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._mget_room_request: MgetRoomRequest = mget_room_request

    def user_id_type(self, user_id_type: str) -> "MgetRoomRequestBuilder":
        self._mget_room_request.user_id_type = user_id_type
        self._mget_room_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: MgetRoomRequestBody) -> "MgetRoomRequestBuilder":
        self._mget_room_request.request_body = request_body
        self._mget_room_request.body = request_body
        return self

    def build(self) -> MgetRoomRequest:
        return self._mget_room_request
