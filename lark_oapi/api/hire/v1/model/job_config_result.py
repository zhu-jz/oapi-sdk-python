# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .id_name_object import IdNameObject
from .job_config_interview_round import JobConfigInterviewRound
from .job_config_round_type_result import JobConfigRoundTypeResult
from .registration_info import RegistrationInfo


class JobConfigResult(object):
    _types = {
        "offer_apply_schema": IdNameObject,
        "offer_process_conf": IdNameObject,
        "recommended_evaluator_list": List[IdNameObject],
        "assessment_template": IdNameObject,
        "id": str,
        "interview_round_list": List[JobConfigInterviewRound],
        "job_requirement_list": List[IdNameObject],
        "interview_registration": RegistrationInfo,
        "onboard_registration": RegistrationInfo,
        "interview_round_type_list": List[JobConfigRoundTypeResult],
        "related_job_list": List[IdNameObject],
        "job_attribute": int,
    }

    def __init__(self, d=None):
        self.offer_apply_schema: Optional[IdNameObject] = None
        self.offer_process_conf: Optional[IdNameObject] = None
        self.recommended_evaluator_list: Optional[List[IdNameObject]] = None
        self.assessment_template: Optional[IdNameObject] = None
        self.id: Optional[str] = None
        self.interview_round_list: Optional[List[JobConfigInterviewRound]] = None
        self.job_requirement_list: Optional[List[IdNameObject]] = None
        self.interview_registration: Optional[RegistrationInfo] = None
        self.onboard_registration: Optional[RegistrationInfo] = None
        self.interview_round_type_list: Optional[List[JobConfigRoundTypeResult]] = None
        self.related_job_list: Optional[List[IdNameObject]] = None
        self.job_attribute: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobConfigResultBuilder":
        return JobConfigResultBuilder()


class JobConfigResultBuilder(object):
    def __init__(self) -> None:
        self._job_config_result = JobConfigResult()

    def offer_apply_schema(self, offer_apply_schema: IdNameObject) -> "JobConfigResultBuilder":
        self._job_config_result.offer_apply_schema = offer_apply_schema
        return self

    def offer_process_conf(self, offer_process_conf: IdNameObject) -> "JobConfigResultBuilder":
        self._job_config_result.offer_process_conf = offer_process_conf
        return self

    def recommended_evaluator_list(self, recommended_evaluator_list: List[IdNameObject]) -> "JobConfigResultBuilder":
        self._job_config_result.recommended_evaluator_list = recommended_evaluator_list
        return self

    def assessment_template(self, assessment_template: IdNameObject) -> "JobConfigResultBuilder":
        self._job_config_result.assessment_template = assessment_template
        return self

    def id(self, id: str) -> "JobConfigResultBuilder":
        self._job_config_result.id = id
        return self

    def interview_round_list(self, interview_round_list: List[JobConfigInterviewRound]) -> "JobConfigResultBuilder":
        self._job_config_result.interview_round_list = interview_round_list
        return self

    def job_requirement_list(self, job_requirement_list: List[IdNameObject]) -> "JobConfigResultBuilder":
        self._job_config_result.job_requirement_list = job_requirement_list
        return self

    def interview_registration(self, interview_registration: RegistrationInfo) -> "JobConfigResultBuilder":
        self._job_config_result.interview_registration = interview_registration
        return self

    def onboard_registration(self, onboard_registration: RegistrationInfo) -> "JobConfigResultBuilder":
        self._job_config_result.onboard_registration = onboard_registration
        return self

    def interview_round_type_list(self, interview_round_type_list: List[
        JobConfigRoundTypeResult]) -> "JobConfigResultBuilder":
        self._job_config_result.interview_round_type_list = interview_round_type_list
        return self

    def related_job_list(self, related_job_list: List[IdNameObject]) -> "JobConfigResultBuilder":
        self._job_config_result.related_job_list = related_job_list
        return self

    def job_attribute(self, job_attribute: int) -> "JobConfigResultBuilder":
        self._job_config_result.job_attribute = job_attribute
        return self

    def build(self) -> "JobConfigResult":
        return self._job_config_result
