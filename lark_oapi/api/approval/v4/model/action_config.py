# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ActionConfig(object):
    _types = {
        "action_type": str,
        "action_name": str,
        "is_need_reason": bool,
        "is_reason_required": bool,
        "is_need_attachment": bool,
    }

    def __init__(self, d=None):
        self.action_type: Optional[str] = None
        self.action_name: Optional[str] = None
        self.is_need_reason: Optional[bool] = None
        self.is_reason_required: Optional[bool] = None
        self.is_need_attachment: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ActionConfigBuilder":
        return ActionConfigBuilder()


class ActionConfigBuilder(object):
    def __init__(self) -> None:
        self._action_config = ActionConfig()

    def action_type(self, action_type: str) -> "ActionConfigBuilder":
        self._action_config.action_type = action_type
        return self

    def action_name(self, action_name: str) -> "ActionConfigBuilder":
        self._action_config.action_name = action_name
        return self

    def is_need_reason(self, is_need_reason: bool) -> "ActionConfigBuilder":
        self._action_config.is_need_reason = is_need_reason
        return self

    def is_reason_required(self, is_reason_required: bool) -> "ActionConfigBuilder":
        self._action_config.is_reason_required = is_reason_required
        return self

    def is_need_attachment(self, is_need_attachment: bool) -> "ActionConfigBuilder":
        self._action_config.is_need_attachment = is_need_attachment
        return self

    def build(self) -> "ActionConfig":
        return self._action_config
