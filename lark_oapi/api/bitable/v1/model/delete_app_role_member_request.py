# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteAppRoleMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.member_id_type: Optional[str] = None
        self.app_token: Optional[str] = None
        self.role_id: Optional[str] = None
        self.member_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteAppRoleMemberRequestBuilder":
        return DeleteAppRoleMemberRequestBuilder()


class DeleteAppRoleMemberRequestBuilder(object):

    def __init__(self) -> None:
        delete_app_role_member_request = DeleteAppRoleMemberRequest()
        delete_app_role_member_request.http_method = HttpMethod.DELETE
        delete_app_role_member_request.uri = "/open-apis/bitable/v1/apps/:app_token/roles/:role_id/members/:member_id"
        delete_app_role_member_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._delete_app_role_member_request: DeleteAppRoleMemberRequest = delete_app_role_member_request

    def member_id_type(self, member_id_type: str) -> "DeleteAppRoleMemberRequestBuilder":
        self._delete_app_role_member_request.member_id_type = member_id_type
        self._delete_app_role_member_request.add_query("member_id_type", member_id_type)
        return self

    def app_token(self, app_token: str) -> "DeleteAppRoleMemberRequestBuilder":
        self._delete_app_role_member_request.app_token = app_token
        self._delete_app_role_member_request.paths["app_token"] = str(app_token)
        return self

    def role_id(self, role_id: str) -> "DeleteAppRoleMemberRequestBuilder":
        self._delete_app_role_member_request.role_id = role_id
        self._delete_app_role_member_request.paths["role_id"] = str(role_id)
        return self

    def member_id(self, member_id: str) -> "DeleteAppRoleMemberRequestBuilder":
        self._delete_app_role_member_request.member_id = member_id
        self._delete_app_role_member_request.paths["member_id"] = str(member_id)
        return self

    def build(self) -> DeleteAppRoleMemberRequest:
        return self._delete_app_role_member_request
