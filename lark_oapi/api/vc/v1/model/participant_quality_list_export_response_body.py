# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ParticipantQualityListExportResponseBody(object):
    _types = {
        "task_id": str,
    }

    def __init__(self, d=None):
        self.task_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ParticipantQualityListExportResponseBodyBuilder":
        return ParticipantQualityListExportResponseBodyBuilder()


class ParticipantQualityListExportResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._participant_quality_list_export_response_body = ParticipantQualityListExportResponseBody()

    def task_id(self, task_id: str) -> "ParticipantQualityListExportResponseBodyBuilder":
        self._participant_quality_list_export_response_body.task_id = task_id
        return self

    def build(self) -> "ParticipantQualityListExportResponseBody":
        return self._participant_quality_list_export_response_body
