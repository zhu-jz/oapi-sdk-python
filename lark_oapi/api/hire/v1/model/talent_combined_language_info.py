# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .talent_customized_data_object_value import TalentCustomizedDataObjectValue


class TalentCombinedLanguageInfo(object):
    _types = {
        "id": str,
        "language": int,
        "proficiency": int,
        "customized_data": List[TalentCustomizedDataObjectValue],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.language: Optional[int] = None
        self.proficiency: Optional[int] = None
        self.customized_data: Optional[List[TalentCustomizedDataObjectValue]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentCombinedLanguageInfoBuilder":
        return TalentCombinedLanguageInfoBuilder()


class TalentCombinedLanguageInfoBuilder(object):
    def __init__(self) -> None:
        self._talent_combined_language_info = TalentCombinedLanguageInfo()

    def id(self, id: str) -> "TalentCombinedLanguageInfoBuilder":
        self._talent_combined_language_info.id = id
        return self

    def language(self, language: int) -> "TalentCombinedLanguageInfoBuilder":
        self._talent_combined_language_info.language = language
        return self

    def proficiency(self, proficiency: int) -> "TalentCombinedLanguageInfoBuilder":
        self._talent_combined_language_info.proficiency = proficiency
        return self

    def customized_data(self,
                        customized_data: List[TalentCustomizedDataObjectValue]) -> "TalentCombinedLanguageInfoBuilder":
        self._talent_combined_language_info.customized_data = customized_data
        return self

    def build(self) -> "TalentCombinedLanguageInfo":
        return self._talent_combined_language_info
