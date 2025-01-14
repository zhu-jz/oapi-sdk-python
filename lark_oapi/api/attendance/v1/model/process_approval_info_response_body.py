# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .approval_info import ApprovalInfo


class ProcessApprovalInfoResponseBody(object):
    _types = {
        "approval_info": ApprovalInfo,
    }

    def __init__(self, d=None):
        self.approval_info: Optional[ApprovalInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProcessApprovalInfoResponseBodyBuilder":
        return ProcessApprovalInfoResponseBodyBuilder()


class ProcessApprovalInfoResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._process_approval_info_response_body = ProcessApprovalInfoResponseBody()

    def approval_info(self, approval_info: ApprovalInfo) -> "ProcessApprovalInfoResponseBodyBuilder":
        self._process_approval_info_response_body.approval_info = approval_info
        return self

    def build(self) -> "ProcessApprovalInfoResponseBody":
        return self._process_approval_info_response_body
