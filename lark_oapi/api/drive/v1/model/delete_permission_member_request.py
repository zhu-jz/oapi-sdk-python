# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeletePermissionMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.type: Optional[str] = None
        self.member_type: Optional[str] = None
        self.token: Optional[str] = None
        self.member_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeletePermissionMemberRequestBuilder":
        return DeletePermissionMemberRequestBuilder()


class DeletePermissionMemberRequestBuilder(object):

    def __init__(self) -> None:
        delete_permission_member_request = DeletePermissionMemberRequest()
        delete_permission_member_request.http_method = HttpMethod.DELETE
        delete_permission_member_request.uri = "/open-apis/drive/v1/permissions/:token/members/:member_id"
        delete_permission_member_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._delete_permission_member_request: DeletePermissionMemberRequest = delete_permission_member_request

    def type(self, type: str) -> "DeletePermissionMemberRequestBuilder":
        self._delete_permission_member_request.type = type
        self._delete_permission_member_request.add_query("type", type)
        return self

    def member_type(self, member_type: str) -> "DeletePermissionMemberRequestBuilder":
        self._delete_permission_member_request.member_type = member_type
        self._delete_permission_member_request.add_query("member_type", member_type)
        return self

    def token(self, token: str) -> "DeletePermissionMemberRequestBuilder":
        self._delete_permission_member_request.token = token
        self._delete_permission_member_request.paths["token"] = str(token)
        return self

    def member_id(self, member_id: str) -> "DeletePermissionMemberRequestBuilder":
        self._delete_permission_member_request.member_id = member_id
        self._delete_permission_member_request.paths["member_id"] = str(member_id)
        return self

    def build(self) -> DeletePermissionMemberRequest:
        return self._delete_permission_member_request
