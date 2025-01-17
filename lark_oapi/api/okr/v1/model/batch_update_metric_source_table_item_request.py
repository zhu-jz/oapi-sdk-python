# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_update_metric_source_table_item_request_body import BatchUpdateMetricSourceTableItemRequestBody


class BatchUpdateMetricSourceTableItemRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.metric_source_id: Optional[str] = None
        self.metric_table_id: Optional[str] = None
        self.request_body: Optional[BatchUpdateMetricSourceTableItemRequestBody] = None

    @staticmethod
    def builder() -> "BatchUpdateMetricSourceTableItemRequestBuilder":
        return BatchUpdateMetricSourceTableItemRequestBuilder()


class BatchUpdateMetricSourceTableItemRequestBuilder(object):

    def __init__(self) -> None:
        batch_update_metric_source_table_item_request = BatchUpdateMetricSourceTableItemRequest()
        batch_update_metric_source_table_item_request.http_method = HttpMethod.PATCH
        batch_update_metric_source_table_item_request.uri = "/open-apis/okr/v1/metric_sources/:metric_source_id/tables/:metric_table_id/items/batch_update"
        batch_update_metric_source_table_item_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._batch_update_metric_source_table_item_request: BatchUpdateMetricSourceTableItemRequest = batch_update_metric_source_table_item_request

    def user_id_type(self, user_id_type: str) -> "BatchUpdateMetricSourceTableItemRequestBuilder":
        self._batch_update_metric_source_table_item_request.user_id_type = user_id_type
        self._batch_update_metric_source_table_item_request.add_query("user_id_type", user_id_type)
        return self

    def metric_source_id(self, metric_source_id: str) -> "BatchUpdateMetricSourceTableItemRequestBuilder":
        self._batch_update_metric_source_table_item_request.metric_source_id = metric_source_id
        self._batch_update_metric_source_table_item_request.paths["metric_source_id"] = str(metric_source_id)
        return self

    def metric_table_id(self, metric_table_id: str) -> "BatchUpdateMetricSourceTableItemRequestBuilder":
        self._batch_update_metric_source_table_item_request.metric_table_id = metric_table_id
        self._batch_update_metric_source_table_item_request.paths["metric_table_id"] = str(metric_table_id)
        return self

    def request_body(self,
                     request_body: BatchUpdateMetricSourceTableItemRequestBody) -> "BatchUpdateMetricSourceTableItemRequestBuilder":
        self._batch_update_metric_source_table_item_request.request_body = request_body
        self._batch_update_metric_source_table_item_request.body = request_body
        return self

    def build(self) -> BatchUpdateMetricSourceTableItemRequest:
        return self._batch_update_metric_source_table_item_request
