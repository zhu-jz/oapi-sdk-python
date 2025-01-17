# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListMotoRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.level: Optional[int] = None

    @staticmethod
    def builder() -> "ListMotoRequestBuilder":
        return ListMotoRequestBuilder()


class ListMotoRequestBuilder(object):

    def __init__(self) -> None:
        list_moto_request = ListMotoRequest()
        list_moto_request.http_method = HttpMethod.GET
        list_moto_request.uri = "/open-apis/gray_test_open_sg/v1/motos"
        list_moto_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_moto_request: ListMotoRequest = list_moto_request

    def page_size(self, page_size: int) -> "ListMotoRequestBuilder":
        self._list_moto_request.page_size = page_size
        self._list_moto_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListMotoRequestBuilder":
        self._list_moto_request.page_token = page_token
        self._list_moto_request.add_query("page_token", page_token)
        return self

    def level(self, level: int) -> "ListMotoRequestBuilder":
        self._list_moto_request.level = level
        self._list_moto_request.add_query("level", level)
        return self

    def build(self) -> ListMotoRequest:
        return self._list_moto_request
