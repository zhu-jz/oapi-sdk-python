# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SearchEmployeeRequestBody(object):
    _types = {
        "fields": List[str],
        "employment_id_list": List[str],
        "employee_number_list": List[str],
        "work_email": str,
        "phone_number": str,
        "key_word": str,
        "employment_status": str,
        "employee_type_id": str,
        "department_id_list": List[str],
        "direct_manager_id_list": List[str],
        "dotted_line_manager_id_list": List[str],
        "regular_employee_start_date_start": str,
        "regular_employee_start_date_end": str,
        "effective_time_start": str,
        "effective_time_end": str,
        "work_location_id_list_include_sub": List[str],
        "preferred_english_full_name_list": List[str],
        "preferred_local_full_name_list": List[str],
        "national_id_number_list": List[str],
        "phone_number_list": List[str],
        "email_address_list": List[str],
        "department_id_list_include_sub": List[str],
    }

    def __init__(self, d=None):
        self.fields: Optional[List[str]] = None
        self.employment_id_list: Optional[List[str]] = None
        self.employee_number_list: Optional[List[str]] = None
        self.work_email: Optional[str] = None
        self.phone_number: Optional[str] = None
        self.key_word: Optional[str] = None
        self.employment_status: Optional[str] = None
        self.employee_type_id: Optional[str] = None
        self.department_id_list: Optional[List[str]] = None
        self.direct_manager_id_list: Optional[List[str]] = None
        self.dotted_line_manager_id_list: Optional[List[str]] = None
        self.regular_employee_start_date_start: Optional[str] = None
        self.regular_employee_start_date_end: Optional[str] = None
        self.effective_time_start: Optional[str] = None
        self.effective_time_end: Optional[str] = None
        self.work_location_id_list_include_sub: Optional[List[str]] = None
        self.preferred_english_full_name_list: Optional[List[str]] = None
        self.preferred_local_full_name_list: Optional[List[str]] = None
        self.national_id_number_list: Optional[List[str]] = None
        self.phone_number_list: Optional[List[str]] = None
        self.email_address_list: Optional[List[str]] = None
        self.department_id_list_include_sub: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchEmployeeRequestBodyBuilder":
        return SearchEmployeeRequestBodyBuilder()


class SearchEmployeeRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._search_employee_request_body = SearchEmployeeRequestBody()

    def fields(self, fields: List[str]) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.fields = fields
        return self

    def employment_id_list(self, employment_id_list: List[str]) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.employment_id_list = employment_id_list
        return self

    def employee_number_list(self, employee_number_list: List[str]) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.employee_number_list = employee_number_list
        return self

    def work_email(self, work_email: str) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.work_email = work_email
        return self

    def phone_number(self, phone_number: str) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.phone_number = phone_number
        return self

    def key_word(self, key_word: str) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.key_word = key_word
        return self

    def employment_status(self, employment_status: str) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.employment_status = employment_status
        return self

    def employee_type_id(self, employee_type_id: str) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.employee_type_id = employee_type_id
        return self

    def department_id_list(self, department_id_list: List[str]) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.department_id_list = department_id_list
        return self

    def direct_manager_id_list(self, direct_manager_id_list: List[str]) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.direct_manager_id_list = direct_manager_id_list
        return self

    def dotted_line_manager_id_list(self, dotted_line_manager_id_list: List[str]) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.dotted_line_manager_id_list = dotted_line_manager_id_list
        return self

    def regular_employee_start_date_start(self,
                                          regular_employee_start_date_start: str) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.regular_employee_start_date_start = regular_employee_start_date_start
        return self

    def regular_employee_start_date_end(self,
                                        regular_employee_start_date_end: str) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.regular_employee_start_date_end = regular_employee_start_date_end
        return self

    def effective_time_start(self, effective_time_start: str) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.effective_time_start = effective_time_start
        return self

    def effective_time_end(self, effective_time_end: str) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.effective_time_end = effective_time_end
        return self

    def work_location_id_list_include_sub(self, work_location_id_list_include_sub: List[
        str]) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.work_location_id_list_include_sub = work_location_id_list_include_sub
        return self

    def preferred_english_full_name_list(self, preferred_english_full_name_list: List[
        str]) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.preferred_english_full_name_list = preferred_english_full_name_list
        return self

    def preferred_local_full_name_list(self,
                                       preferred_local_full_name_list: List[str]) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.preferred_local_full_name_list = preferred_local_full_name_list
        return self

    def national_id_number_list(self, national_id_number_list: List[str]) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.national_id_number_list = national_id_number_list
        return self

    def phone_number_list(self, phone_number_list: List[str]) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.phone_number_list = phone_number_list
        return self

    def email_address_list(self, email_address_list: List[str]) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.email_address_list = email_address_list
        return self

    def department_id_list_include_sub(self,
                                       department_id_list_include_sub: List[str]) -> "SearchEmployeeRequestBodyBuilder":
        self._search_employee_request_body.department_id_list_include_sub = department_id_list_include_sub
        return self

    def build(self) -> "SearchEmployeeRequestBody":
        return self._search_employee_request_body
