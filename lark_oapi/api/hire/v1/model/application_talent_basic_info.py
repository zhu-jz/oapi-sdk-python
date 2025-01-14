# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .city import City
from .nationality import Nationality


class ApplicationTalentBasicInfo(object):
    _types = {
        "name": str,
        "mobile": str,
        "mobile_country_code": str,
        "email": str,
        "experience_years": int,
        "age": int,
        "nationality": Nationality,
        "gender": int,
        "current_city": City,
        "hometown_city": City,
        "preferred_city_list": List[City],
        "mobile_code": str,
        "identification_type": int,
        "identification_number": str,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.mobile: Optional[str] = None
        self.mobile_country_code: Optional[str] = None
        self.email: Optional[str] = None
        self.experience_years: Optional[int] = None
        self.age: Optional[int] = None
        self.nationality: Optional[Nationality] = None
        self.gender: Optional[int] = None
        self.current_city: Optional[City] = None
        self.hometown_city: Optional[City] = None
        self.preferred_city_list: Optional[List[City]] = None
        self.mobile_code: Optional[str] = None
        self.identification_type: Optional[int] = None
        self.identification_number: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationTalentBasicInfoBuilder":
        return ApplicationTalentBasicInfoBuilder()


class ApplicationTalentBasicInfoBuilder(object):
    def __init__(self) -> None:
        self._application_talent_basic_info = ApplicationTalentBasicInfo()

    def name(self, name: str) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.name = name
        return self

    def mobile(self, mobile: str) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.mobile = mobile
        return self

    def mobile_country_code(self, mobile_country_code: str) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.mobile_country_code = mobile_country_code
        return self

    def email(self, email: str) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.email = email
        return self

    def experience_years(self, experience_years: int) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.experience_years = experience_years
        return self

    def age(self, age: int) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.age = age
        return self

    def nationality(self, nationality: Nationality) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.nationality = nationality
        return self

    def gender(self, gender: int) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.gender = gender
        return self

    def current_city(self, current_city: City) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.current_city = current_city
        return self

    def hometown_city(self, hometown_city: City) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.hometown_city = hometown_city
        return self

    def preferred_city_list(self, preferred_city_list: List[City]) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.preferred_city_list = preferred_city_list
        return self

    def mobile_code(self, mobile_code: str) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.mobile_code = mobile_code
        return self

    def identification_type(self, identification_type: int) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.identification_type = identification_type
        return self

    def identification_number(self, identification_number: str) -> "ApplicationTalentBasicInfoBuilder":
        self._application_talent_basic_info.identification_number = identification_number
        return self

    def build(self) -> "ApplicationTalentBasicInfo":
        return self._application_talent_basic_info
