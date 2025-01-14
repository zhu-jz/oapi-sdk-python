# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetImportTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.ticket: Optional[str] = None

    @staticmethod
    def builder() -> "GetImportTaskRequestBuilder":
        return GetImportTaskRequestBuilder()


class GetImportTaskRequestBuilder(object):

    def __init__(self) -> None:
        get_import_task_request = GetImportTaskRequest()
        get_import_task_request.http_method = HttpMethod.GET
        get_import_task_request.uri = "/open-apis/drive/v1/import_tasks/:ticket"
        get_import_task_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._get_import_task_request: GetImportTaskRequest = get_import_task_request

    def ticket(self, ticket: str) -> "GetImportTaskRequestBuilder":
        self._get_import_task_request.ticket = ticket
        self._get_import_task_request.paths["ticket"] = str(ticket)
        return self

    def build(self) -> GetImportTaskRequest:
        return self._get_import_task_request
