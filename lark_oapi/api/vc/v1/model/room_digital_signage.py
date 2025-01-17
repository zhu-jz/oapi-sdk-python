# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .room_digital_signage_material import RoomDigitalSignageMaterial


class RoomDigitalSignage(object):
    _types = {
        "enable": bool,
        "mute": bool,
        "start_display": int,
        "stop_display": int,
        "materials": List[RoomDigitalSignageMaterial],
    }

    def __init__(self, d=None):
        self.enable: Optional[bool] = None
        self.mute: Optional[bool] = None
        self.start_display: Optional[int] = None
        self.stop_display: Optional[int] = None
        self.materials: Optional[List[RoomDigitalSignageMaterial]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RoomDigitalSignageBuilder":
        return RoomDigitalSignageBuilder()


class RoomDigitalSignageBuilder(object):
    def __init__(self) -> None:
        self._room_digital_signage = RoomDigitalSignage()

    def enable(self, enable: bool) -> "RoomDigitalSignageBuilder":
        self._room_digital_signage.enable = enable
        return self

    def mute(self, mute: bool) -> "RoomDigitalSignageBuilder":
        self._room_digital_signage.mute = mute
        return self

    def start_display(self, start_display: int) -> "RoomDigitalSignageBuilder":
        self._room_digital_signage.start_display = start_display
        return self

    def stop_display(self, stop_display: int) -> "RoomDigitalSignageBuilder":
        self._room_digital_signage.stop_display = stop_display
        return self

    def materials(self, materials: List[RoomDigitalSignageMaterial]) -> "RoomDigitalSignageBuilder":
        self._room_digital_signage.materials = materials
        return self

    def build(self) -> "RoomDigitalSignage":
        return self._room_digital_signage
