# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TestResultDetail(object):
    _types = {
        "subject": str,
        "result": str,
    }

    def __init__(self, d=None):
        self.subject: Optional[str] = None
        self.result: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TestResultDetailBuilder":
        return TestResultDetailBuilder()


class TestResultDetailBuilder(object):
    def __init__(self) -> None:
        self._test_result_detail = TestResultDetail()

    def subject(self, subject: str) -> "TestResultDetailBuilder":
        self._test_result_detail.subject = subject
        return self

    def result(self, result: str) -> "TestResultDetailBuilder":
        self._test_result_detail.result = result
        return self

    def build(self) -> "TestResultDetail":
        return self._test_result_detail
