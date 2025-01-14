# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .report_top_user import ReportTopUser


class GetTopUserReportResponseBody(object):
    _types = {
        "top_user_report": List[ReportTopUser],
    }

    def __init__(self, d=None):
        self.top_user_report: Optional[List[ReportTopUser]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetTopUserReportResponseBodyBuilder":
        return GetTopUserReportResponseBodyBuilder()


class GetTopUserReportResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_top_user_report_response_body = GetTopUserReportResponseBody()

    def top_user_report(self, top_user_report: List[ReportTopUser]) -> "GetTopUserReportResponseBodyBuilder":
        self._get_top_user_report_response_body.top_user_report = top_user_report
        return self

    def build(self) -> "GetTopUserReportResponseBody":
        return self._get_top_user_report_response_body
