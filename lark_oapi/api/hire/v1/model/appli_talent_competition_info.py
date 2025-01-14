# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppliTalentCompetitionInfo(object):
    _types = {
        "id": str,
        "name": str,
        "desc": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.desc: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppliTalentCompetitionInfoBuilder":
        return AppliTalentCompetitionInfoBuilder()


class AppliTalentCompetitionInfoBuilder(object):
    def __init__(self) -> None:
        self._appli_talent_competition_info = AppliTalentCompetitionInfo()

    def id(self, id: str) -> "AppliTalentCompetitionInfoBuilder":
        self._appli_talent_competition_info.id = id
        return self

    def name(self, name: str) -> "AppliTalentCompetitionInfoBuilder":
        self._appli_talent_competition_info.name = name
        return self

    def desc(self, desc: str) -> "AppliTalentCompetitionInfoBuilder":
        self._appli_talent_competition_info.desc = desc
        return self

    def build(self) -> "AppliTalentCompetitionInfo":
        return self._appli_talent_competition_info
