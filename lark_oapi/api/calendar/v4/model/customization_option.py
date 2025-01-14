# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CustomizationOption(object):
    _types = {
        "option_key": str,
        "others_content": str,
    }

    def __init__(self, d=None):
        self.option_key: Optional[str] = None
        self.others_content: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CustomizationOptionBuilder":
        return CustomizationOptionBuilder()


class CustomizationOptionBuilder(object):
    def __init__(self) -> None:
        self._customization_option = CustomizationOption()

    def option_key(self, option_key: str) -> "CustomizationOptionBuilder":
        self._customization_option.option_key = option_key
        return self

    def others_content(self, others_content: str) -> "CustomizationOptionBuilder":
        self._customization_option.others_content = others_content
        return self

    def build(self) -> "CustomizationOption":
        return self._customization_option
