# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class EcoExamResultReport(object):
    _types = {
        "name": str,
        "url": str,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoExamResultReportBuilder":
        return EcoExamResultReportBuilder()


class EcoExamResultReportBuilder(object):
    def __init__(self) -> None:
        self._eco_exam_result_report = EcoExamResultReport()

    def name(self, name: str) -> "EcoExamResultReportBuilder":
        self._eco_exam_result_report.name = name
        return self

    def url(self, url: str) -> "EcoExamResultReportBuilder":
        self._eco_exam_result_report.url = url
        return self

    def build(self) -> "EcoExamResultReport":
        return self._eco_exam_result_report
