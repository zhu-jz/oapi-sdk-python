# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .talent_customized_data_object_value import TalentCustomizedDataObjectValue


class TalentCombinedAwardInfo(object):
    _types = {
        "id": str,
        "title": str,
        "award_time": str,
        "desc": str,
        "customized_data": List[TalentCustomizedDataObjectValue],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.title: Optional[str] = None
        self.award_time: Optional[str] = None
        self.desc: Optional[str] = None
        self.customized_data: Optional[List[TalentCustomizedDataObjectValue]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentCombinedAwardInfoBuilder":
        return TalentCombinedAwardInfoBuilder()


class TalentCombinedAwardInfoBuilder(object):
    def __init__(self) -> None:
        self._talent_combined_award_info = TalentCombinedAwardInfo()

    def id(self, id: str) -> "TalentCombinedAwardInfoBuilder":
        self._talent_combined_award_info.id = id
        return self

    def title(self, title: str) -> "TalentCombinedAwardInfoBuilder":
        self._talent_combined_award_info.title = title
        return self

    def award_time(self, award_time: str) -> "TalentCombinedAwardInfoBuilder":
        self._talent_combined_award_info.award_time = award_time
        return self

    def desc(self, desc: str) -> "TalentCombinedAwardInfoBuilder":
        self._talent_combined_award_info.desc = desc
        return self

    def customized_data(self,
                        customized_data: List[TalentCustomizedDataObjectValue]) -> "TalentCombinedAwardInfoBuilder":
        self._talent_combined_award_info.customized_data = customized_data
        return self

    def build(self) -> "TalentCombinedAwardInfo":
        return self._talent_combined_award_info
