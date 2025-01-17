# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetShiftRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.shift_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetShiftRequestBuilder":
        return GetShiftRequestBuilder()


class GetShiftRequestBuilder(object):

    def __init__(self) -> None:
        get_shift_request = GetShiftRequest()
        get_shift_request.http_method = HttpMethod.GET
        get_shift_request.uri = "/open-apis/attendance/v1/shifts/:shift_id"
        get_shift_request.token_types = {AccessTokenType.TENANT}
        self._get_shift_request: GetShiftRequest = get_shift_request

    def shift_id(self, shift_id: str) -> "GetShiftRequestBuilder":
        self._get_shift_request.shift_id = shift_id
        self._get_shift_request.paths["shift_id"] = str(shift_id)
        return self

    def build(self) -> GetShiftRequest:
        return self._get_shift_request
