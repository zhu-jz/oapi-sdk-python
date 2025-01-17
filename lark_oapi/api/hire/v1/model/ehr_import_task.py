# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class EhrImportTask(object):
    _types = {
        "fail_reason": str,
        "redirect_url": str,
        "state": int,
    }

    def __init__(self, d=None):
        self.fail_reason: Optional[str] = None
        self.redirect_url: Optional[str] = None
        self.state: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EhrImportTaskBuilder":
        return EhrImportTaskBuilder()


class EhrImportTaskBuilder(object):
    def __init__(self) -> None:
        self._ehr_import_task = EhrImportTask()

    def fail_reason(self, fail_reason: str) -> "EhrImportTaskBuilder":
        self._ehr_import_task.fail_reason = fail_reason
        return self

    def redirect_url(self, redirect_url: str) -> "EhrImportTaskBuilder":
        self._ehr_import_task.redirect_url = redirect_url
        return self

    def state(self, state: int) -> "EhrImportTaskBuilder":
        self._ehr_import_task.state = state
        return self

    def build(self) -> "EhrImportTask":
        return self._ehr_import_task
