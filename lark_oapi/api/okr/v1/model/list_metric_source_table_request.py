# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListMetricSourceTableRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None
        self.metric_source_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListMetricSourceTableRequestBuilder":
        return ListMetricSourceTableRequestBuilder()


class ListMetricSourceTableRequestBuilder(object):

    def __init__(self) -> None:
        list_metric_source_table_request = ListMetricSourceTableRequest()
        list_metric_source_table_request.http_method = HttpMethod.GET
        list_metric_source_table_request.uri = "/open-apis/okr/v1/metric_sources/:metric_source_id/tables"
        list_metric_source_table_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_metric_source_table_request: ListMetricSourceTableRequest = list_metric_source_table_request

    def page_token(self, page_token: str) -> "ListMetricSourceTableRequestBuilder":
        self._list_metric_source_table_request.page_token = page_token
        self._list_metric_source_table_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: str) -> "ListMetricSourceTableRequestBuilder":
        self._list_metric_source_table_request.page_size = page_size
        self._list_metric_source_table_request.add_query("page_size", page_size)
        return self

    def metric_source_id(self, metric_source_id: str) -> "ListMetricSourceTableRequestBuilder":
        self._list_metric_source_table_request.metric_source_id = metric_source_id
        self._list_metric_source_table_request.paths["metric_source_id"] = str(metric_source_id)
        return self

    def build(self) -> ListMetricSourceTableRequest:
        return self._list_metric_source_table_request
