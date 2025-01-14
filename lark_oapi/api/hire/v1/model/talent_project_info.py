# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .talent_customized_data_child import TalentCustomizedDataChild


class TalentProjectInfo(object):
    _types = {
        "id": str,
        "name": str,
        "role": str,
        "link": str,
        "desc": str,
        "start_time": str,
        "end_time": str,
        "customized_data_list": List[TalentCustomizedDataChild],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.role: Optional[str] = None
        self.link: Optional[str] = None
        self.desc: Optional[str] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.customized_data_list: Optional[List[TalentCustomizedDataChild]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentProjectInfoBuilder":
        return TalentProjectInfoBuilder()


class TalentProjectInfoBuilder(object):
    def __init__(self) -> None:
        self._talent_project_info = TalentProjectInfo()

    def id(self, id: str) -> "TalentProjectInfoBuilder":
        self._talent_project_info.id = id
        return self

    def name(self, name: str) -> "TalentProjectInfoBuilder":
        self._talent_project_info.name = name
        return self

    def role(self, role: str) -> "TalentProjectInfoBuilder":
        self._talent_project_info.role = role
        return self

    def link(self, link: str) -> "TalentProjectInfoBuilder":
        self._talent_project_info.link = link
        return self

    def desc(self, desc: str) -> "TalentProjectInfoBuilder":
        self._talent_project_info.desc = desc
        return self

    def start_time(self, start_time: str) -> "TalentProjectInfoBuilder":
        self._talent_project_info.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "TalentProjectInfoBuilder":
        self._talent_project_info.end_time = end_time
        return self

    def customized_data_list(self, customized_data_list: List[TalentCustomizedDataChild]) -> "TalentProjectInfoBuilder":
        self._talent_project_info.customized_data_list = customized_data_list
        return self

    def build(self) -> "TalentProjectInfo":
        return self._talent_project_info
