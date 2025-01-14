# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .appli_offer_onboard_profile_city import AppliOfferOnboardProfileCity


class AppliOfferOnboardProfileAdd(object):
    _types = {
        "id": str,
        "name": str,
        "en_name": str,
        "district": AppliOfferOnboardProfileCity,
        "city": AppliOfferOnboardProfileCity,
        "state": AppliOfferOnboardProfileCity,
        "country": AppliOfferOnboardProfileCity,
        "usage_id_list": List[str],
        "active_status": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.district: Optional[AppliOfferOnboardProfileCity] = None
        self.city: Optional[AppliOfferOnboardProfileCity] = None
        self.state: Optional[AppliOfferOnboardProfileCity] = None
        self.country: Optional[AppliOfferOnboardProfileCity] = None
        self.usage_id_list: Optional[List[str]] = None
        self.active_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppliOfferOnboardProfileAddBuilder":
        return AppliOfferOnboardProfileAddBuilder()


class AppliOfferOnboardProfileAddBuilder(object):
    def __init__(self) -> None:
        self._appli_offer_onboard_profile_add = AppliOfferOnboardProfileAdd()

    def id(self, id: str) -> "AppliOfferOnboardProfileAddBuilder":
        self._appli_offer_onboard_profile_add.id = id
        return self

    def name(self, name: str) -> "AppliOfferOnboardProfileAddBuilder":
        self._appli_offer_onboard_profile_add.name = name
        return self

    def en_name(self, en_name: str) -> "AppliOfferOnboardProfileAddBuilder":
        self._appli_offer_onboard_profile_add.en_name = en_name
        return self

    def district(self, district: AppliOfferOnboardProfileCity) -> "AppliOfferOnboardProfileAddBuilder":
        self._appli_offer_onboard_profile_add.district = district
        return self

    def city(self, city: AppliOfferOnboardProfileCity) -> "AppliOfferOnboardProfileAddBuilder":
        self._appli_offer_onboard_profile_add.city = city
        return self

    def state(self, state: AppliOfferOnboardProfileCity) -> "AppliOfferOnboardProfileAddBuilder":
        self._appli_offer_onboard_profile_add.state = state
        return self

    def country(self, country: AppliOfferOnboardProfileCity) -> "AppliOfferOnboardProfileAddBuilder":
        self._appli_offer_onboard_profile_add.country = country
        return self

    def usage_id_list(self, usage_id_list: List[str]) -> "AppliOfferOnboardProfileAddBuilder":
        self._appli_offer_onboard_profile_add.usage_id_list = usage_id_list
        return self

    def active_status(self, active_status: int) -> "AppliOfferOnboardProfileAddBuilder":
        self._appli_offer_onboard_profile_add.active_status = active_status
        return self

    def build(self) -> "AppliOfferOnboardProfileAdd":
        return self._appli_offer_onboard_profile_add
