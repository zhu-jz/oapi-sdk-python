# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .enum import Enum


class Assessment(object):
    _types = {
        "assessment_id": str,
        "assessment_status": Enum,
        "assessment_result": Enum,
        "assessment_score": float,
        "assessment_grade": Enum,
        "assessment_comment": str,
        "assessment_detail": str,
        "is_final_asssessment": bool,
    }

    def __init__(self, d=None):
        self.assessment_id: Optional[str] = None
        self.assessment_status: Optional[Enum] = None
        self.assessment_result: Optional[Enum] = None
        self.assessment_score: Optional[float] = None
        self.assessment_grade: Optional[Enum] = None
        self.assessment_comment: Optional[str] = None
        self.assessment_detail: Optional[str] = None
        self.is_final_asssessment: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AssessmentBuilder":
        return AssessmentBuilder()


class AssessmentBuilder(object):
    def __init__(self) -> None:
        self._assessment = Assessment()

    def assessment_id(self, assessment_id: str) -> "AssessmentBuilder":
        self._assessment.assessment_id = assessment_id
        return self

    def assessment_status(self, assessment_status: Enum) -> "AssessmentBuilder":
        self._assessment.assessment_status = assessment_status
        return self

    def assessment_result(self, assessment_result: Enum) -> "AssessmentBuilder":
        self._assessment.assessment_result = assessment_result
        return self

    def assessment_score(self, assessment_score: float) -> "AssessmentBuilder":
        self._assessment.assessment_score = assessment_score
        return self

    def assessment_grade(self, assessment_grade: Enum) -> "AssessmentBuilder":
        self._assessment.assessment_grade = assessment_grade
        return self

    def assessment_comment(self, assessment_comment: str) -> "AssessmentBuilder":
        self._assessment.assessment_comment = assessment_comment
        return self

    def assessment_detail(self, assessment_detail: str) -> "AssessmentBuilder":
        self._assessment.assessment_detail = assessment_detail
        return self

    def is_final_asssessment(self, is_final_asssessment: bool) -> "AssessmentBuilder":
        self._assessment.is_final_asssessment = is_final_asssessment
        return self

    def build(self) -> "Assessment":
        return self._assessment
