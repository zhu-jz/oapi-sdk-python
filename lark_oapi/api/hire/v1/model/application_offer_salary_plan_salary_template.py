# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ApplicationOfferSalaryPlanSalaryTemplate(object):
    _types = {
        "template_key": str,
        "total_amount": str,
        "currency": str,
        "salary_content": str,
    }

    def __init__(self, d=None):
        self.template_key: Optional[str] = None
        self.total_amount: Optional[str] = None
        self.currency: Optional[str] = None
        self.salary_content: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationOfferSalaryPlanSalaryTemplateBuilder":
        return ApplicationOfferSalaryPlanSalaryTemplateBuilder()


class ApplicationOfferSalaryPlanSalaryTemplateBuilder(object):
    def __init__(self) -> None:
        self._application_offer_salary_plan_salary_template = ApplicationOfferSalaryPlanSalaryTemplate()

    def template_key(self, template_key: str) -> "ApplicationOfferSalaryPlanSalaryTemplateBuilder":
        self._application_offer_salary_plan_salary_template.template_key = template_key
        return self

    def total_amount(self, total_amount: str) -> "ApplicationOfferSalaryPlanSalaryTemplateBuilder":
        self._application_offer_salary_plan_salary_template.total_amount = total_amount
        return self

    def currency(self, currency: str) -> "ApplicationOfferSalaryPlanSalaryTemplateBuilder":
        self._application_offer_salary_plan_salary_template.currency = currency
        return self

    def salary_content(self, salary_content: str) -> "ApplicationOfferSalaryPlanSalaryTemplateBuilder":
        self._application_offer_salary_plan_salary_template.salary_content = salary_content
        return self

    def build(self) -> "ApplicationOfferSalaryPlanSalaryTemplate":
        return self._application_offer_salary_plan_salary_template
