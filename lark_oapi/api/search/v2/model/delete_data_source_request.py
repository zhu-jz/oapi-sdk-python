# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteDataSourceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.data_source_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteDataSourceRequestBuilder":
        return DeleteDataSourceRequestBuilder()


class DeleteDataSourceRequestBuilder(object):

    def __init__(self) -> None:
        delete_data_source_request = DeleteDataSourceRequest()
        delete_data_source_request.http_method = HttpMethod.DELETE
        delete_data_source_request.uri = "/open-apis/search/v2/data_sources/:data_source_id"
        delete_data_source_request.token_types = {AccessTokenType.TENANT}
        self._delete_data_source_request: DeleteDataSourceRequest = delete_data_source_request

    def data_source_id(self, data_source_id: str) -> "DeleteDataSourceRequestBuilder":
        self._delete_data_source_request.data_source_id = data_source_id
        self._delete_data_source_request.paths["data_source_id"] = str(data_source_id)
        return self

    def build(self) -> DeleteDataSourceRequest:
        return self._delete_data_source_request
