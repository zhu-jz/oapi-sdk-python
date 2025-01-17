# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class PunchSpecialDateShift(object):
    _types = {
        "punch_day": int,
        "shift_id": str,
    }

    def __init__(self, d=None):
        self.punch_day: Optional[int] = None
        self.shift_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PunchSpecialDateShiftBuilder":
        return PunchSpecialDateShiftBuilder()


class PunchSpecialDateShiftBuilder(object):
    def __init__(self) -> None:
        self._punch_special_date_shift = PunchSpecialDateShift()

    def punch_day(self, punch_day: int) -> "PunchSpecialDateShiftBuilder":
        self._punch_special_date_shift.punch_day = punch_day
        return self

    def shift_id(self, shift_id: str) -> "PunchSpecialDateShiftBuilder":
        self._punch_special_date_shift.shift_id = shift_id
        return self

    def build(self) -> "PunchSpecialDateShift":
        return self._punch_special_date_shift
