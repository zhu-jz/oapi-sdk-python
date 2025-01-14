# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .site_name import SiteName


class SiteJobType(object):
    _types = {
        "id": str,
        "name": SiteName,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[SiteName] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SiteJobTypeBuilder":
        return SiteJobTypeBuilder()


class SiteJobTypeBuilder(object):
    def __init__(self) -> None:
        self._site_job_type = SiteJobType()

    def id(self, id: str) -> "SiteJobTypeBuilder":
        self._site_job_type.id = id
        return self

    def name(self, name: SiteName) -> "SiteJobTypeBuilder":
        self._site_job_type.name = name
        return self

    def build(self) -> "SiteJobType":
        return self._site_job_type
