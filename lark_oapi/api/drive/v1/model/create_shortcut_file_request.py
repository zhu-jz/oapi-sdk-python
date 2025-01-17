# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_shortcut_file_request_body import CreateShortcutFileRequestBody


class CreateShortcutFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[CreateShortcutFileRequestBody] = None

    @staticmethod
    def builder() -> "CreateShortcutFileRequestBuilder":
        return CreateShortcutFileRequestBuilder()


class CreateShortcutFileRequestBuilder(object):

    def __init__(self) -> None:
        create_shortcut_file_request = CreateShortcutFileRequest()
        create_shortcut_file_request.http_method = HttpMethod.POST
        create_shortcut_file_request.uri = "/open-apis/drive/v1/files/create_shortcut"
        create_shortcut_file_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._create_shortcut_file_request: CreateShortcutFileRequest = create_shortcut_file_request

    def user_id_type(self, user_id_type: str) -> "CreateShortcutFileRequestBuilder":
        self._create_shortcut_file_request.user_id_type = user_id_type
        self._create_shortcut_file_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: CreateShortcutFileRequestBody) -> "CreateShortcutFileRequestBuilder":
        self._create_shortcut_file_request.request_body = request_body
        self._create_shortcut_file_request.body = request_body
        return self

    def build(self) -> CreateShortcutFileRequest:
        return self._create_shortcut_file_request
