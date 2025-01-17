# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .approval_create import ApprovalCreate


class CreateApprovalRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.department_id_type: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[ApprovalCreate] = None

    @staticmethod
    def builder() -> "CreateApprovalRequestBuilder":
        return CreateApprovalRequestBuilder()


class CreateApprovalRequestBuilder(object):

    def __init__(self) -> None:
        create_approval_request = CreateApprovalRequest()
        create_approval_request.http_method = HttpMethod.POST
        create_approval_request.uri = "/open-apis/approval/v4/approvals"
        create_approval_request.token_types = {AccessTokenType.TENANT}
        self._create_approval_request: CreateApprovalRequest = create_approval_request

    def department_id_type(self, department_id_type: str) -> "CreateApprovalRequestBuilder":
        self._create_approval_request.department_id_type = department_id_type
        self._create_approval_request.add_query("department_id_type", department_id_type)
        return self

    def user_id_type(self, user_id_type: str) -> "CreateApprovalRequestBuilder":
        self._create_approval_request.user_id_type = user_id_type
        self._create_approval_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: ApprovalCreate) -> "CreateApprovalRequestBuilder":
        self._create_approval_request.request_body = request_body
        self._create_approval_request.body = request_body
        return self

    def build(self) -> CreateApprovalRequest:
        return self._create_approval_request
