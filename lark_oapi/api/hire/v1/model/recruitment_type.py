# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class RecruitmentType(object):
    _types = {
        "id": str,
        "name": str,
        "en_name": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RecruitmentTypeBuilder":
        return RecruitmentTypeBuilder()


class RecruitmentTypeBuilder(object):
    def __init__(self) -> None:
        self._recruitment_type = RecruitmentType()

    def id(self, id: str) -> "RecruitmentTypeBuilder":
        self._recruitment_type.id = id
        return self

    def name(self, name: str) -> "RecruitmentTypeBuilder":
        self._recruitment_type.name = name
        return self

    def en_name(self, en_name: str) -> "RecruitmentTypeBuilder":
        self._recruitment_type.en_name = en_name
        return self

    def build(self) -> "RecruitmentType":
        return self._recruitment_type
