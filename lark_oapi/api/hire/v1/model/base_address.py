# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .base_city import BaseCity
from .base_country import BaseCountry
from .base_district import BaseDistrict


class BaseAddress(object):
    _types = {
        "id": str,
        "zh_name": str,
        "en_name": str,
        "district": BaseDistrict,
        "city": BaseCity,
        "state": BaseCity,
        "country": BaseCountry,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.district: Optional[BaseDistrict] = None
        self.city: Optional[BaseCity] = None
        self.state: Optional[BaseCity] = None
        self.country: Optional[BaseCountry] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BaseAddressBuilder":
        return BaseAddressBuilder()


class BaseAddressBuilder(object):
    def __init__(self) -> None:
        self._base_address = BaseAddress()

    def id(self, id: str) -> "BaseAddressBuilder":
        self._base_address.id = id
        return self

    def zh_name(self, zh_name: str) -> "BaseAddressBuilder":
        self._base_address.zh_name = zh_name
        return self

    def en_name(self, en_name: str) -> "BaseAddressBuilder":
        self._base_address.en_name = en_name
        return self

    def district(self, district: BaseDistrict) -> "BaseAddressBuilder":
        self._base_address.district = district
        return self

    def city(self, city: BaseCity) -> "BaseAddressBuilder":
        self._base_address.city = city
        return self

    def state(self, state: BaseCity) -> "BaseAddressBuilder":
        self._base_address.state = state
        return self

    def country(self, country: BaseCountry) -> "BaseAddressBuilder":
        self._base_address.country = country
        return self

    def build(self) -> "BaseAddress":
        return self._base_address
