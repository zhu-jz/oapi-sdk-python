# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n_names import I18nNames
from .toolkit_callback import ToolkitCallback
from .toolkit_redirect_link import ToolkitRedirectLink


class Toolkit(object):
    _types = {
        "toolkit_id": int,
        "image_key": str,
        "toolkit_name": str,
        "i18n_name": I18nNames,
        "toolkit_type": str,
        "redirect_link": ToolkitRedirectLink,
        "callback": ToolkitCallback,
    }

    def __init__(self, d=None):
        self.toolkit_id: Optional[int] = None
        self.image_key: Optional[str] = None
        self.toolkit_name: Optional[str] = None
        self.i18n_name: Optional[I18nNames] = None
        self.toolkit_type: Optional[str] = None
        self.redirect_link: Optional[ToolkitRedirectLink] = None
        self.callback: Optional[ToolkitCallback] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ToolkitBuilder":
        return ToolkitBuilder()


class ToolkitBuilder(object):
    def __init__(self) -> None:
        self._toolkit = Toolkit()

    def toolkit_id(self, toolkit_id: int) -> "ToolkitBuilder":
        self._toolkit.toolkit_id = toolkit_id
        return self

    def image_key(self, image_key: str) -> "ToolkitBuilder":
        self._toolkit.image_key = image_key
        return self

    def toolkit_name(self, toolkit_name: str) -> "ToolkitBuilder":
        self._toolkit.toolkit_name = toolkit_name
        return self

    def i18n_name(self, i18n_name: I18nNames) -> "ToolkitBuilder":
        self._toolkit.i18n_name = i18n_name
        return self

    def toolkit_type(self, toolkit_type: str) -> "ToolkitBuilder":
        self._toolkit.toolkit_type = toolkit_type
        return self

    def redirect_link(self, redirect_link: ToolkitRedirectLink) -> "ToolkitBuilder":
        self._toolkit.redirect_link = redirect_link
        return self

    def callback(self, callback: ToolkitCallback) -> "ToolkitBuilder":
        self._toolkit.callback = callback
        return self

    def build(self) -> "Toolkit":
        return self._toolkit
