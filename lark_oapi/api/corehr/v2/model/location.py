# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .address import Address
from .custom_field_data import CustomFieldData
from .enum import Enum
from .hiberarchy_common import HiberarchyCommon


class Location(object):
    _types = {
        "location_id": str,
        "hiberarchy_common": HiberarchyCommon,
        "location_usage_list": List[Enum],
        "address": List[Address],
        "working_hours_type_id": str,
        "effective_time": str,
        "expiration_time": str,
        "custom_fields": List[CustomFieldData],
        "locale": Enum,
        "time_zone_id": str,
        "display_language_id": str,
    }

    def __init__(self, d=None):
        self.location_id: Optional[str] = None
        self.hiberarchy_common: Optional[HiberarchyCommon] = None
        self.location_usage_list: Optional[List[Enum]] = None
        self.address: Optional[List[Address]] = None
        self.working_hours_type_id: Optional[str] = None
        self.effective_time: Optional[str] = None
        self.expiration_time: Optional[str] = None
        self.custom_fields: Optional[List[CustomFieldData]] = None
        self.locale: Optional[Enum] = None
        self.time_zone_id: Optional[str] = None
        self.display_language_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LocationBuilder":
        return LocationBuilder()


class LocationBuilder(object):
    def __init__(self) -> None:
        self._location = Location()

    def location_id(self, location_id: str) -> "LocationBuilder":
        self._location.location_id = location_id
        return self

    def hiberarchy_common(self, hiberarchy_common: HiberarchyCommon) -> "LocationBuilder":
        self._location.hiberarchy_common = hiberarchy_common
        return self

    def location_usage_list(self, location_usage_list: List[Enum]) -> "LocationBuilder":
        self._location.location_usage_list = location_usage_list
        return self

    def address(self, address: List[Address]) -> "LocationBuilder":
        self._location.address = address
        return self

    def working_hours_type_id(self, working_hours_type_id: str) -> "LocationBuilder":
        self._location.working_hours_type_id = working_hours_type_id
        return self

    def effective_time(self, effective_time: str) -> "LocationBuilder":
        self._location.effective_time = effective_time
        return self

    def expiration_time(self, expiration_time: str) -> "LocationBuilder":
        self._location.expiration_time = expiration_time
        return self

    def custom_fields(self, custom_fields: List[CustomFieldData]) -> "LocationBuilder":
        self._location.custom_fields = custom_fields
        return self

    def locale(self, locale: Enum) -> "LocationBuilder":
        self._location.locale = locale
        return self

    def time_zone_id(self, time_zone_id: str) -> "LocationBuilder":
        self._location.time_zone_id = time_zone_id
        return self

    def display_language_id(self, display_language_id: str) -> "LocationBuilder":
        self._location.display_language_id = display_language_id
        return self

    def build(self) -> "Location":
        return self._location
