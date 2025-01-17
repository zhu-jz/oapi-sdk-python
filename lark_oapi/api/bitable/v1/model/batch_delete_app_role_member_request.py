# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_delete_app_role_member_request_body import BatchDeleteAppRoleMemberRequestBody


class BatchDeleteAppRoleMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.app_token: Optional[str] = None
        self.role_id: Optional[str] = None
        self.request_body: Optional[BatchDeleteAppRoleMemberRequestBody] = None

    @staticmethod
    def builder() -> "BatchDeleteAppRoleMemberRequestBuilder":
        return BatchDeleteAppRoleMemberRequestBuilder()


class BatchDeleteAppRoleMemberRequestBuilder(object):

    def __init__(self) -> None:
        batch_delete_app_role_member_request = BatchDeleteAppRoleMemberRequest()
        batch_delete_app_role_member_request.http_method = HttpMethod.POST
        batch_delete_app_role_member_request.uri = "/open-apis/bitable/v1/apps/:app_token/roles/:role_id/members/batch_delete"
        batch_delete_app_role_member_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._batch_delete_app_role_member_request: BatchDeleteAppRoleMemberRequest = batch_delete_app_role_member_request

    def app_token(self, app_token: str) -> "BatchDeleteAppRoleMemberRequestBuilder":
        self._batch_delete_app_role_member_request.app_token = app_token
        self._batch_delete_app_role_member_request.paths["app_token"] = str(app_token)
        return self

    def role_id(self, role_id: str) -> "BatchDeleteAppRoleMemberRequestBuilder":
        self._batch_delete_app_role_member_request.role_id = role_id
        self._batch_delete_app_role_member_request.paths["role_id"] = str(role_id)
        return self

    def request_body(self,
                     request_body: BatchDeleteAppRoleMemberRequestBody) -> "BatchDeleteAppRoleMemberRequestBuilder":
        self._batch_delete_app_role_member_request.request_body = request_body
        self._batch_delete_app_role_member_request.body = request_body
        return self

    def build(self) -> BatchDeleteAppRoleMemberRequest:
        return self._batch_delete_app_role_member_request
