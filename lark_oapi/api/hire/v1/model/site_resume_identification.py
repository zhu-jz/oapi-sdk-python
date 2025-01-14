# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SiteResumeIdentification(object):
    _types = {
        "identification_type": str,
        "code": str,
    }

    def __init__(self, d=None):
        self.identification_type: Optional[str] = None
        self.code: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SiteResumeIdentificationBuilder":
        return SiteResumeIdentificationBuilder()


class SiteResumeIdentificationBuilder(object):
    def __init__(self) -> None:
        self._site_resume_identification = SiteResumeIdentification()

    def identification_type(self, identification_type: str) -> "SiteResumeIdentificationBuilder":
        self._site_resume_identification.identification_type = identification_type
        return self

    def code(self, code: str) -> "SiteResumeIdentificationBuilder":
        self._site_resume_identification.code = code
        return self

    def build(self) -> "SiteResumeIdentification":
        return self._site_resume_identification
