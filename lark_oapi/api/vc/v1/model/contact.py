# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Contact(object):
    _types = {
        "contact_type": int,
        "contact_name": str,
    }

    def __init__(self, d=None):
        self.contact_type: Optional[int] = None
        self.contact_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ContactBuilder":
        return ContactBuilder()


class ContactBuilder(object):
    def __init__(self) -> None:
        self._contact = Contact()

    def contact_type(self, contact_type: int) -> "ContactBuilder":
        self._contact.contact_type = contact_type
        return self

    def contact_name(self, contact_name: str) -> "ContactBuilder":
        self._contact.contact_name = contact_name
        return self

    def build(self) -> "Contact":
        return self._contact
