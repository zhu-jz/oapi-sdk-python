# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .talent_customized_data_child import TalentCustomizedDataChild


class TalentAwardInfo(object):
    _types = {
        "id": str,
        "title": str,
        "award_time": str,
        "desc": str,
        "customized_data_list": List[TalentCustomizedDataChild],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.title: Optional[str] = None
        self.award_time: Optional[str] = None
        self.desc: Optional[str] = None
        self.customized_data_list: Optional[List[TalentCustomizedDataChild]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentAwardInfoBuilder":
        return TalentAwardInfoBuilder()


class TalentAwardInfoBuilder(object):
    def __init__(self) -> None:
        self._talent_award_info = TalentAwardInfo()

    def id(self, id: str) -> "TalentAwardInfoBuilder":
        self._talent_award_info.id = id
        return self

    def title(self, title: str) -> "TalentAwardInfoBuilder":
        self._talent_award_info.title = title
        return self

    def award_time(self, award_time: str) -> "TalentAwardInfoBuilder":
        self._talent_award_info.award_time = award_time
        return self

    def desc(self, desc: str) -> "TalentAwardInfoBuilder":
        self._talent_award_info.desc = desc
        return self

    def customized_data_list(self, customized_data_list: List[TalentCustomizedDataChild]) -> "TalentAwardInfoBuilder":
        self._talent_award_info.customized_data_list = customized_data_list
        return self

    def build(self) -> "TalentAwardInfo":
        return self._talent_award_info
