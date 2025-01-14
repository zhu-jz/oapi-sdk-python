# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetPermissionPublicRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.type: Optional[str] = None
        self.token: Optional[str] = None

    @staticmethod
    def builder() -> "GetPermissionPublicRequestBuilder":
        return GetPermissionPublicRequestBuilder()


class GetPermissionPublicRequestBuilder(object):

    def __init__(self) -> None:
        get_permission_public_request = GetPermissionPublicRequest()
        get_permission_public_request.http_method = HttpMethod.GET
        get_permission_public_request.uri = "/open-apis/drive/v1/permissions/:token/public"
        get_permission_public_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_permission_public_request: GetPermissionPublicRequest = get_permission_public_request

    def type(self, type: str) -> "GetPermissionPublicRequestBuilder":
        self._get_permission_public_request.type = type
        self._get_permission_public_request.add_query("type", type)
        return self

    def token(self, token: str) -> "GetPermissionPublicRequestBuilder":
        self._get_permission_public_request.token = token
        self._get_permission_public_request.paths["token"] = str(token)
        return self

    def build(self) -> GetPermissionPublicRequest:
        return self._get_permission_public_request
