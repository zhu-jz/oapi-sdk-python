# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .scope_group import ScopeGroup


class PunchMember(object):
    _types = {
        "rule_scope_type": int,
        "scope_group_list": ScopeGroup,
    }

    def __init__(self, d=None):
        self.rule_scope_type: Optional[int] = None
        self.scope_group_list: Optional[ScopeGroup] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PunchMemberBuilder":
        return PunchMemberBuilder()


class PunchMemberBuilder(object):
    def __init__(self) -> None:
        self._punch_member = PunchMember()

    def rule_scope_type(self, rule_scope_type: int) -> "PunchMemberBuilder":
        self._punch_member.rule_scope_type = rule_scope_type
        return self

    def scope_group_list(self, scope_group_list: ScopeGroup) -> "PunchMemberBuilder":
        self._punch_member.scope_group_list = scope_group_list
        return self

    def build(self) -> "PunchMember":
        return self._punch_member
