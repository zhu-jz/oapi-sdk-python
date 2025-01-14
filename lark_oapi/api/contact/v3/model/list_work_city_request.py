# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListWorkCityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListWorkCityRequestBuilder":
        return ListWorkCityRequestBuilder()


class ListWorkCityRequestBuilder(object):

    def __init__(self) -> None:
        list_work_city_request = ListWorkCityRequest()
        list_work_city_request.http_method = HttpMethod.GET
        list_work_city_request.uri = "/open-apis/contact/v3/work_cities"
        list_work_city_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_work_city_request: ListWorkCityRequest = list_work_city_request

    def page_size(self, page_size: int) -> "ListWorkCityRequestBuilder":
        self._list_work_city_request.page_size = page_size
        self._list_work_city_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListWorkCityRequestBuilder":
        self._list_work_city_request.page_token = page_token
        self._list_work_city_request.add_query("page_token", page_token)
        return self

    def build(self) -> ListWorkCityRequest:
        return self._list_work_city_request
