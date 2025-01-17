# Code generated by Lark OpenAPI.

import io
from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from lark_oapi.core.utils import Files
from ..model.create_export_task_request import CreateExportTaskRequest
from ..model.create_export_task_response import CreateExportTaskResponse
from ..model.download_export_task_request import DownloadExportTaskRequest
from ..model.download_export_task_response import DownloadExportTaskResponse
from ..model.get_export_task_request import GetExportTaskRequest
from ..model.get_export_task_response import GetExportTaskResponse


class ExportTask(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateExportTaskRequest,
               option: Optional[RequestOption] = None) -> CreateExportTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateExportTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateExportTaskResponse)
        response.raw = resp

        return response

    def download(self, request: DownloadExportTaskRequest,
                 option: Optional[RequestOption] = None) -> DownloadExportTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 处理二进制流
        content_type = resp.headers.get(CONTENT_TYPE)
        response: DownloadExportTaskResponse = DownloadExportTaskResponse()
        if 200 <= resp.status_code < 300:
            response.code = 0
            response.file = io.BytesIO(resp.content)
            response.file_name = Files.parse_file_name(resp.headers)
        elif content_type is not None and content_type.startswith(APPLICATION_JSON):
            response = JSON.unmarshal(str(resp.content, UTF_8), DownloadExportTaskResponse)

        response.raw = resp
        return response

    def get(self, request: GetExportTaskRequest, option: Optional[RequestOption] = None) -> GetExportTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetExportTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), GetExportTaskResponse)
        response.raw = resp

        return response
