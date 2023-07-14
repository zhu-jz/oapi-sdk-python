# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .i18n import I18n
from .common_schema import CommonSchema


class JobRequirementSchema(object):
    _types = {
        "id": str,
        "name": I18n,
        "object_list": List[CommonSchema],
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.object_list: Optional[List[CommonSchema]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobRequirementSchemaBuilder":
        return JobRequirementSchemaBuilder()


class JobRequirementSchemaBuilder(object):
    def __init__(self, job_requirement_schema: JobRequirementSchema = JobRequirementSchema({})) -> None:
        self._job_requirement_schema: JobRequirementSchema = job_requirement_schema
    
    def id(self, id: str) -> "JobRequirementSchemaBuilder":
        self._job_requirement_schema.id = id
        return self
    
    def name(self, name: I18n) -> "JobRequirementSchemaBuilder":
        self._job_requirement_schema.name = name
        return self
    
    def object_list(self, object_list: List[CommonSchema]) -> "JobRequirementSchemaBuilder":
        self._job_requirement_schema.object_list = object_list
        return self
    
    def build(self) -> "JobRequirementSchema":
        return self._job_requirement_schema