# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .patch_leave_accrual_record_request_body import PatchLeaveAccrualRecordRequestBody


class PatchLeaveAccrualRecordRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.leave_id: Optional[str] = None
        self.request_body: Optional[PatchLeaveAccrualRecordRequestBody] = None

    @staticmethod
    def builder() -> "PatchLeaveAccrualRecordRequestBuilder":
        return PatchLeaveAccrualRecordRequestBuilder()


class PatchLeaveAccrualRecordRequestBuilder(object):

    def __init__(self) -> None:
        patch_leave_accrual_record_request = PatchLeaveAccrualRecordRequest()
        patch_leave_accrual_record_request.http_method = HttpMethod.PATCH
        patch_leave_accrual_record_request.uri = "/open-apis/attendance/v1/leave_accrual_record/:leave_id"
        patch_leave_accrual_record_request.token_types = {AccessTokenType.TENANT}
        self._patch_leave_accrual_record_request: PatchLeaveAccrualRecordRequest = patch_leave_accrual_record_request

    def user_id_type(self, user_id_type: str) -> "PatchLeaveAccrualRecordRequestBuilder":
        self._patch_leave_accrual_record_request.user_id_type = user_id_type
        self._patch_leave_accrual_record_request.add_query("user_id_type", user_id_type)
        return self

    def leave_id(self, leave_id: str) -> "PatchLeaveAccrualRecordRequestBuilder":
        self._patch_leave_accrual_record_request.leave_id = leave_id
        self._patch_leave_accrual_record_request.paths["leave_id"] = str(leave_id)
        return self

    def request_body(self, request_body: PatchLeaveAccrualRecordRequestBody) -> "PatchLeaveAccrualRecordRequestBuilder":
        self._patch_leave_accrual_record_request.request_body = request_body
        self._patch_leave_accrual_record_request.body = request_body
        return self

    def build(self) -> PatchLeaveAccrualRecordRequest:
        return self._patch_leave_accrual_record_request
