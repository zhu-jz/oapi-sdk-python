# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .item import Item


class CreateDataSourceItemRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.data_source_id: Optional[str] = None
        self.request_body: Optional[Item] = None

    @staticmethod
    def builder() -> "CreateDataSourceItemRequestBuilder":
        return CreateDataSourceItemRequestBuilder()


class CreateDataSourceItemRequestBuilder(object):

    def __init__(self) -> None:
        create_data_source_item_request = CreateDataSourceItemRequest()
        create_data_source_item_request.http_method = HttpMethod.POST
        create_data_source_item_request.uri = "/open-apis/search/v2/data_sources/:data_source_id/items"
        create_data_source_item_request.token_types = {AccessTokenType.TENANT}
        self._create_data_source_item_request: CreateDataSourceItemRequest = create_data_source_item_request

    def data_source_id(self, data_source_id: str) -> "CreateDataSourceItemRequestBuilder":
        self._create_data_source_item_request.data_source_id = data_source_id
        self._create_data_source_item_request.paths["data_source_id"] = str(data_source_id)
        return self

    def request_body(self, request_body: Item) -> "CreateDataSourceItemRequestBuilder":
        self._create_data_source_item_request.request_body = request_body
        self._create_data_source_item_request.body = request_body
        return self

    def build(self) -> CreateDataSourceItemRequest:
        return self._create_data_source_item_request
