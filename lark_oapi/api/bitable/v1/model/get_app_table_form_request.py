# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetAppTableFormRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.app_token: Optional[str] = None
        self.table_id: Optional[str] = None
        self.form_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetAppTableFormRequestBuilder":
        return GetAppTableFormRequestBuilder()


class GetAppTableFormRequestBuilder(object):

    def __init__(self) -> None:
        get_app_table_form_request = GetAppTableFormRequest()
        get_app_table_form_request.http_method = HttpMethod.GET
        get_app_table_form_request.uri = "/open-apis/bitable/v1/apps/:app_token/tables/:table_id/forms/:form_id"
        get_app_table_form_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_app_table_form_request: GetAppTableFormRequest = get_app_table_form_request

    def app_token(self, app_token: str) -> "GetAppTableFormRequestBuilder":
        self._get_app_table_form_request.app_token = app_token
        self._get_app_table_form_request.paths["app_token"] = str(app_token)
        return self

    def table_id(self, table_id: str) -> "GetAppTableFormRequestBuilder":
        self._get_app_table_form_request.table_id = table_id
        self._get_app_table_form_request.paths["table_id"] = str(table_id)
        return self

    def form_id(self, form_id: str) -> "GetAppTableFormRequestBuilder":
        self._get_app_table_form_request.form_id = form_id
        self._get_app_table_form_request.paths["form_id"] = str(form_id)
        return self

    def build(self) -> GetAppTableFormRequest:
        return self._get_app_table_form_request
