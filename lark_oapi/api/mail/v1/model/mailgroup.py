# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class Mailgroup(object):
    _types = {
        "mailgroup_id": str,
        "email": str,
        "name": str,
        "description": str,
        "direct_members_count": str,
        "include_external_member": bool,
        "include_all_company_member": bool,
        "who_can_send_mail": str,
    }

    def __init__(self, d):
        self.mailgroup_id: Optional[str] = None
        self.email: Optional[str] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.direct_members_count: Optional[str] = None
        self.include_external_member: Optional[bool] = None
        self.include_all_company_member: Optional[bool] = None
        self.who_can_send_mail: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MailgroupBuilder":
        return MailgroupBuilder()


class MailgroupBuilder(object):
    def __init__(self, mailgroup: Mailgroup = Mailgroup({})) -> None:
        self._mailgroup: Mailgroup = mailgroup
    
    def mailgroup_id(self, mailgroup_id: str) -> "MailgroupBuilder":
        self._mailgroup.mailgroup_id = mailgroup_id
        return self
    
    def email(self, email: str) -> "MailgroupBuilder":
        self._mailgroup.email = email
        return self
    
    def name(self, name: str) -> "MailgroupBuilder":
        self._mailgroup.name = name
        return self
    
    def description(self, description: str) -> "MailgroupBuilder":
        self._mailgroup.description = description
        return self
    
    def direct_members_count(self, direct_members_count: str) -> "MailgroupBuilder":
        self._mailgroup.direct_members_count = direct_members_count
        return self
    
    def include_external_member(self, include_external_member: bool) -> "MailgroupBuilder":
        self._mailgroup.include_external_member = include_external_member
        return self
    
    def include_all_company_member(self, include_all_company_member: bool) -> "MailgroupBuilder":
        self._mailgroup.include_all_company_member = include_all_company_member
        return self
    
    def who_can_send_mail(self, who_can_send_mail: str) -> "MailgroupBuilder":
        self._mailgroup.who_can_send_mail = who_can_send_mail
        return self
    
    def build(self) -> "Mailgroup":
        return self._mailgroup