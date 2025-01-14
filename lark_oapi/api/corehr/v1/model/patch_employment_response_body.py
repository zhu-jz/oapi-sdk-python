# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .employment import Employment


class PatchEmploymentResponseBody(object):
    _types = {
        "employment": Employment,
    }

    def __init__(self, d=None):
        self.employment: Optional[Employment] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchEmploymentResponseBodyBuilder":
        return PatchEmploymentResponseBodyBuilder()


class PatchEmploymentResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_employment_response_body = PatchEmploymentResponseBody()

    def employment(self, employment: Employment) -> "PatchEmploymentResponseBodyBuilder":
        self._patch_employment_response_body.employment = employment
        return self

    def build(self) -> "PatchEmploymentResponseBody":
        return self._patch_employment_response_body
