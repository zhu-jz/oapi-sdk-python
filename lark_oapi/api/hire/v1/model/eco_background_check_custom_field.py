# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .eco_background_check_custom_field_data import EcoBackgroundCheckCustomFieldData


class EcoBackgroundCheckCustomField(object):
    _types = {
        "account_id": str,
        "custom_field_list": List[EcoBackgroundCheckCustomFieldData],
    }

    def __init__(self, d=None):
        self.account_id: Optional[str] = None
        self.custom_field_list: Optional[List[EcoBackgroundCheckCustomFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoBackgroundCheckCustomFieldBuilder":
        return EcoBackgroundCheckCustomFieldBuilder()


class EcoBackgroundCheckCustomFieldBuilder(object):
    def __init__(self) -> None:
        self._eco_background_check_custom_field = EcoBackgroundCheckCustomField()

    def account_id(self, account_id: str) -> "EcoBackgroundCheckCustomFieldBuilder":
        self._eco_background_check_custom_field.account_id = account_id
        return self

    def custom_field_list(self, custom_field_list: List[
        EcoBackgroundCheckCustomFieldData]) -> "EcoBackgroundCheckCustomFieldBuilder":
        self._eco_background_check_custom_field.custom_field_list = custom_field_list
        return self

    def build(self) -> "EcoBackgroundCheckCustomField":
        return self._eco_background_check_custom_field
