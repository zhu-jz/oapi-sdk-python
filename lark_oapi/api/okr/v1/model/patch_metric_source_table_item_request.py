# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .patch_metric_source_table_item_request_body import PatchMetricSourceTableItemRequestBody


class PatchMetricSourceTableItemRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.metric_source_id: Optional[str] = None
        self.metric_table_id: Optional[str] = None
        self.metric_item_id: Optional[str] = None
        self.request_body: Optional[PatchMetricSourceTableItemRequestBody] = None

    @staticmethod
    def builder() -> "PatchMetricSourceTableItemRequestBuilder":
        return PatchMetricSourceTableItemRequestBuilder()


class PatchMetricSourceTableItemRequestBuilder(object):

    def __init__(self) -> None:
        patch_metric_source_table_item_request = PatchMetricSourceTableItemRequest()
        patch_metric_source_table_item_request.http_method = HttpMethod.PATCH
        patch_metric_source_table_item_request.uri = "/open-apis/okr/v1/metric_sources/:metric_source_id/tables/:metric_table_id/items/:metric_item_id"
        patch_metric_source_table_item_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._patch_metric_source_table_item_request: PatchMetricSourceTableItemRequest = patch_metric_source_table_item_request

    def user_id_type(self, user_id_type: str) -> "PatchMetricSourceTableItemRequestBuilder":
        self._patch_metric_source_table_item_request.user_id_type = user_id_type
        self._patch_metric_source_table_item_request.add_query("user_id_type", user_id_type)
        return self

    def metric_source_id(self, metric_source_id: str) -> "PatchMetricSourceTableItemRequestBuilder":
        self._patch_metric_source_table_item_request.metric_source_id = metric_source_id
        self._patch_metric_source_table_item_request.paths["metric_source_id"] = str(metric_source_id)
        return self

    def metric_table_id(self, metric_table_id: str) -> "PatchMetricSourceTableItemRequestBuilder":
        self._patch_metric_source_table_item_request.metric_table_id = metric_table_id
        self._patch_metric_source_table_item_request.paths["metric_table_id"] = str(metric_table_id)
        return self

    def metric_item_id(self, metric_item_id: str) -> "PatchMetricSourceTableItemRequestBuilder":
        self._patch_metric_source_table_item_request.metric_item_id = metric_item_id
        self._patch_metric_source_table_item_request.paths["metric_item_id"] = str(metric_item_id)
        return self

    def request_body(self,
                     request_body: PatchMetricSourceTableItemRequestBody) -> "PatchMetricSourceTableItemRequestBuilder":
        self._patch_metric_source_table_item_request.request_body = request_body
        self._patch_metric_source_table_item_request.body = request_body
        return self

    def build(self) -> PatchMetricSourceTableItemRequest:
        return self._patch_metric_source_table_item_request
