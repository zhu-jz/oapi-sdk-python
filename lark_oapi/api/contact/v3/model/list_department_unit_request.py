# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListDepartmentUnitRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.unit_id: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None

    @staticmethod
    def builder() -> "ListDepartmentUnitRequestBuilder":
        return ListDepartmentUnitRequestBuilder()


class ListDepartmentUnitRequestBuilder(object):

    def __init__(self) -> None:
        list_department_unit_request = ListDepartmentUnitRequest()
        list_department_unit_request.http_method = HttpMethod.GET
        list_department_unit_request.uri = "/open-apis/contact/v3/unit/list_department"
        list_department_unit_request.token_types = {AccessTokenType.TENANT}
        self._list_department_unit_request: ListDepartmentUnitRequest = list_department_unit_request

    def unit_id(self, unit_id: str) -> "ListDepartmentUnitRequestBuilder":
        self._list_department_unit_request.unit_id = unit_id
        self._list_department_unit_request.add_query("unit_id", unit_id)
        return self

    def department_id_type(self, department_id_type: str) -> "ListDepartmentUnitRequestBuilder":
        self._list_department_unit_request.department_id_type = department_id_type
        self._list_department_unit_request.add_query("department_id_type", department_id_type)
        return self

    def page_token(self, page_token: str) -> "ListDepartmentUnitRequestBuilder":
        self._list_department_unit_request.page_token = page_token
        self._list_department_unit_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListDepartmentUnitRequestBuilder":
        self._list_department_unit_request.page_size = page_size
        self._list_department_unit_request.add_query("page_size", page_size)
        return self

    def build(self) -> ListDepartmentUnitRequest:
        return self._list_department_unit_request
