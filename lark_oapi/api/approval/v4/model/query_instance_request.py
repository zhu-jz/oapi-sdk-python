# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .instance_search import InstanceSearch


class QueryInstanceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[InstanceSearch] = None

    @staticmethod
    def builder() -> "QueryInstanceRequestBuilder":
        return QueryInstanceRequestBuilder()


class QueryInstanceRequestBuilder(object):

    def __init__(self) -> None:
        query_instance_request = QueryInstanceRequest()
        query_instance_request.http_method = HttpMethod.POST
        query_instance_request.uri = "/open-apis/approval/v4/instances/query"
        query_instance_request.token_types = {AccessTokenType.TENANT}
        self._query_instance_request: QueryInstanceRequest = query_instance_request

    def page_size(self, page_size: int) -> "QueryInstanceRequestBuilder":
        self._query_instance_request.page_size = page_size
        self._query_instance_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "QueryInstanceRequestBuilder":
        self._query_instance_request.page_token = page_token
        self._query_instance_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "QueryInstanceRequestBuilder":
        self._query_instance_request.user_id_type = user_id_type
        self._query_instance_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: InstanceSearch) -> "QueryInstanceRequestBuilder":
        self._query_instance_request.request_body = request_body
        self._query_instance_request.body = request_body
        return self

    def build(self) -> QueryInstanceRequest:
        return self._query_instance_request
