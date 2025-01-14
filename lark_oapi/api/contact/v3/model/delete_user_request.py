# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .delete_user_request_body import DeleteUserRequestBody


class DeleteUserRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.user_id: Optional[str] = None
        self.request_body: Optional[DeleteUserRequestBody] = None

    @staticmethod
    def builder() -> "DeleteUserRequestBuilder":
        return DeleteUserRequestBuilder()


class DeleteUserRequestBuilder(object):

    def __init__(self) -> None:
        delete_user_request = DeleteUserRequest()
        delete_user_request.http_method = HttpMethod.DELETE
        delete_user_request.uri = "/open-apis/contact/v3/users/:user_id"
        delete_user_request.token_types = {AccessTokenType.TENANT}
        self._delete_user_request: DeleteUserRequest = delete_user_request

    def user_id_type(self, user_id_type: str) -> "DeleteUserRequestBuilder":
        self._delete_user_request.user_id_type = user_id_type
        self._delete_user_request.add_query("user_id_type", user_id_type)
        return self

    def user_id(self, user_id: str) -> "DeleteUserRequestBuilder":
        self._delete_user_request.user_id = user_id
        self._delete_user_request.paths["user_id"] = str(user_id)
        return self

    def request_body(self, request_body: DeleteUserRequestBody) -> "DeleteUserRequestBuilder":
        self._delete_user_request.request_body = request_body
        self._delete_user_request.body = request_body
        return self

    def build(self) -> DeleteUserRequest:
        return self._delete_user_request
