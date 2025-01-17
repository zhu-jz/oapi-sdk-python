# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_delete_mailgroup_manager_request_body import BatchDeleteMailgroupManagerRequestBody


class BatchDeleteMailgroupManagerRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.mailgroup_id: Optional[str] = None
        self.request_body: Optional[BatchDeleteMailgroupManagerRequestBody] = None

    @staticmethod
    def builder() -> "BatchDeleteMailgroupManagerRequestBuilder":
        return BatchDeleteMailgroupManagerRequestBuilder()


class BatchDeleteMailgroupManagerRequestBuilder(object):

    def __init__(self) -> None:
        batch_delete_mailgroup_manager_request = BatchDeleteMailgroupManagerRequest()
        batch_delete_mailgroup_manager_request.http_method = HttpMethod.POST
        batch_delete_mailgroup_manager_request.uri = "/open-apis/mail/v1/mailgroups/:mailgroup_id/managers/batch_delete"
        batch_delete_mailgroup_manager_request.token_types = {AccessTokenType.TENANT}
        self._batch_delete_mailgroup_manager_request: BatchDeleteMailgroupManagerRequest = batch_delete_mailgroup_manager_request

    def user_id_type(self, user_id_type: str) -> "BatchDeleteMailgroupManagerRequestBuilder":
        self._batch_delete_mailgroup_manager_request.user_id_type = user_id_type
        self._batch_delete_mailgroup_manager_request.add_query("user_id_type", user_id_type)
        return self

    def mailgroup_id(self, mailgroup_id: str) -> "BatchDeleteMailgroupManagerRequestBuilder":
        self._batch_delete_mailgroup_manager_request.mailgroup_id = mailgroup_id
        self._batch_delete_mailgroup_manager_request.paths["mailgroup_id"] = str(mailgroup_id)
        return self

    def request_body(self,
                     request_body: BatchDeleteMailgroupManagerRequestBody) -> "BatchDeleteMailgroupManagerRequestBuilder":
        self._batch_delete_mailgroup_manager_request.request_body = request_body
        self._batch_delete_mailgroup_manager_request.body = request_body
        return self

    def build(self) -> BatchDeleteMailgroupManagerRequest:
        return self._batch_delete_mailgroup_manager_request
