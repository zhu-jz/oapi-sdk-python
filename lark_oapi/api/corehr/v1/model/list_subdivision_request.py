# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListSubdivisionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None
        self.country_region_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListSubdivisionRequestBuilder":
        return ListSubdivisionRequestBuilder()


class ListSubdivisionRequestBuilder(object):

    def __init__(self) -> None:
        list_subdivision_request = ListSubdivisionRequest()
        list_subdivision_request.http_method = HttpMethod.GET
        list_subdivision_request.uri = "/open-apis/corehr/v1/subdivisions"
        list_subdivision_request.token_types = {AccessTokenType.TENANT}
        self._list_subdivision_request: ListSubdivisionRequest = list_subdivision_request

    def page_token(self, page_token: str) -> "ListSubdivisionRequestBuilder":
        self._list_subdivision_request.page_token = page_token
        self._list_subdivision_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: str) -> "ListSubdivisionRequestBuilder":
        self._list_subdivision_request.page_size = page_size
        self._list_subdivision_request.add_query("page_size", page_size)
        return self

    def country_region_id(self, country_region_id: str) -> "ListSubdivisionRequestBuilder":
        self._list_subdivision_request.country_region_id = country_region_id
        self._list_subdivision_request.add_query("country_region_id", country_region_id)
        return self

    def build(self) -> ListSubdivisionRequest:
        return self._list_subdivision_request
