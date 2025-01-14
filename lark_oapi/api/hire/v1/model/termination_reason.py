# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class TerminationReason(object):
    _types = {
        "id": str,
        "name": I18n,
        "referral_name": I18n,
        "termination_type": int,
        "is_used_as_evaluation": bool,
        "active_status": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.referral_name: Optional[I18n] = None
        self.termination_type: Optional[int] = None
        self.is_used_as_evaluation: Optional[bool] = None
        self.active_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TerminationReasonBuilder":
        return TerminationReasonBuilder()


class TerminationReasonBuilder(object):
    def __init__(self) -> None:
        self._termination_reason = TerminationReason()

    def id(self, id: str) -> "TerminationReasonBuilder":
        self._termination_reason.id = id
        return self

    def name(self, name: I18n) -> "TerminationReasonBuilder":
        self._termination_reason.name = name
        return self

    def referral_name(self, referral_name: I18n) -> "TerminationReasonBuilder":
        self._termination_reason.referral_name = referral_name
        return self

    def termination_type(self, termination_type: int) -> "TerminationReasonBuilder":
        self._termination_reason.termination_type = termination_type
        return self

    def is_used_as_evaluation(self, is_used_as_evaluation: bool) -> "TerminationReasonBuilder":
        self._termination_reason.is_used_as_evaluation = is_used_as_evaluation
        return self

    def active_status(self, active_status: int) -> "TerminationReasonBuilder":
        self._termination_reason.active_status = active_status
        return self

    def build(self) -> "TerminationReason":
        return self._termination_reason
