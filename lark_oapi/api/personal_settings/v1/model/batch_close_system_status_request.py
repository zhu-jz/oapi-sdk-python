# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_close_system_status_request_body import BatchCloseSystemStatusRequestBody


class BatchCloseSystemStatusRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.system_status_id: Optional[int] = None
        self.request_body: Optional[BatchCloseSystemStatusRequestBody] = None

    @staticmethod
    def builder() -> "BatchCloseSystemStatusRequestBuilder":
        return BatchCloseSystemStatusRequestBuilder()


class BatchCloseSystemStatusRequestBuilder(object):

    def __init__(self) -> None:
        batch_close_system_status_request = BatchCloseSystemStatusRequest()
        batch_close_system_status_request.http_method = HttpMethod.POST
        batch_close_system_status_request.uri = "/open-apis/personal_settings/v1/system_statuses/:system_status_id/batch_close"
        batch_close_system_status_request.token_types = {AccessTokenType.TENANT}
        self._batch_close_system_status_request: BatchCloseSystemStatusRequest = batch_close_system_status_request

    def user_id_type(self, user_id_type: str) -> "BatchCloseSystemStatusRequestBuilder":
        self._batch_close_system_status_request.user_id_type = user_id_type
        self._batch_close_system_status_request.add_query("user_id_type", user_id_type)
        return self

    def system_status_id(self, system_status_id: int) -> "BatchCloseSystemStatusRequestBuilder":
        self._batch_close_system_status_request.system_status_id = system_status_id
        self._batch_close_system_status_request.paths["system_status_id"] = str(system_status_id)
        return self

    def request_body(self, request_body: BatchCloseSystemStatusRequestBody) -> "BatchCloseSystemStatusRequestBuilder":
        self._batch_close_system_status_request.request_body = request_body
        self._batch_close_system_status_request.body = request_body
        return self

    def build(self) -> BatchCloseSystemStatusRequest:
        return self._batch_close_system_status_request
