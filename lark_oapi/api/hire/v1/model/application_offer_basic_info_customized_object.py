# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .offer_schema_name import OfferSchemaName
from .application_offer_basic_info_customized_object_option_value import ApplicationOfferBasicInfoCustomizedObjectOptionValue


class ApplicationOfferBasicInfoCustomizedObject(object):
    _types = {
        "id": str,
        "name": OfferSchemaName,
        "type": str,
        "value": str,
        "option_value_list": List[ApplicationOfferBasicInfoCustomizedObjectOptionValue],
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[OfferSchemaName] = None
        self.type: Optional[str] = None
        self.value: Optional[str] = None
        self.option_value_list: Optional[List[ApplicationOfferBasicInfoCustomizedObjectOptionValue]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationOfferBasicInfoCustomizedObjectBuilder":
        return ApplicationOfferBasicInfoCustomizedObjectBuilder()


class ApplicationOfferBasicInfoCustomizedObjectBuilder(object):
    def __init__(self, application_offer_basic_info_customized_object: ApplicationOfferBasicInfoCustomizedObject = ApplicationOfferBasicInfoCustomizedObject({})) -> None:
        self._application_offer_basic_info_customized_object: ApplicationOfferBasicInfoCustomizedObject = application_offer_basic_info_customized_object
    
    def id(self, id: str) -> "ApplicationOfferBasicInfoCustomizedObjectBuilder":
        self._application_offer_basic_info_customized_object.id = id
        return self
    
    def name(self, name: OfferSchemaName) -> "ApplicationOfferBasicInfoCustomizedObjectBuilder":
        self._application_offer_basic_info_customized_object.name = name
        return self
    
    def type(self, type: str) -> "ApplicationOfferBasicInfoCustomizedObjectBuilder":
        self._application_offer_basic_info_customized_object.type = type
        return self
    
    def value(self, value: str) -> "ApplicationOfferBasicInfoCustomizedObjectBuilder":
        self._application_offer_basic_info_customized_object.value = value
        return self
    
    def option_value_list(self, option_value_list: List[ApplicationOfferBasicInfoCustomizedObjectOptionValue]) -> "ApplicationOfferBasicInfoCustomizedObjectBuilder":
        self._application_offer_basic_info_customized_object.option_value_list = option_value_list
        return self
    
    def build(self) -> "ApplicationOfferBasicInfoCustomizedObject":
        return self._application_offer_basic_info_customized_object