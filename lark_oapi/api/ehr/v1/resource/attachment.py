# Code generated by Lark OpenAPI.

import io
from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from lark_oapi.core.utils import Files
from ..model.get_attachment_request import GetAttachmentRequest
from ..model.get_attachment_response import GetAttachmentResponse


class Attachment(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def get(self, request: GetAttachmentRequest, option: Optional[RequestOption] = None) -> GetAttachmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 处理二进制流
        content_type = resp.headers.get(CONTENT_TYPE)
        response: GetAttachmentResponse = GetAttachmentResponse()
        if 200 <= resp.status_code < 300:
            response.code = 0
            response.file = io.BytesIO(resp.content)
            response.file_name = Files.parse_file_name(resp.headers)
        elif content_type is not None and content_type.startswith(APPLICATION_JSON):
            response = JSON.unmarshal(str(resp.content, UTF_8), GetAttachmentResponse)

        response.raw = resp
        return response
