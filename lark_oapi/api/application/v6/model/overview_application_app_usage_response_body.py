# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .application_app_usage import ApplicationAppUsage


class OverviewApplicationAppUsageResponseBody(object):
    _types = {
        "items": List[ApplicationAppUsage],
    }

    def __init__(self, d=None):
        self.items: Optional[List[ApplicationAppUsage]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OverviewApplicationAppUsageResponseBodyBuilder":
        return OverviewApplicationAppUsageResponseBodyBuilder()


class OverviewApplicationAppUsageResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._overview_application_app_usage_response_body = OverviewApplicationAppUsageResponseBody()

    def items(self, items: List[ApplicationAppUsage]) -> "OverviewApplicationAppUsageResponseBodyBuilder":
        self._overview_application_app_usage_response_body.items = items
        return self

    def build(self) -> "OverviewApplicationAppUsageResponseBody":
        return self._overview_application_app_usage_response_body
