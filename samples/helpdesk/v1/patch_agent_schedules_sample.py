# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.helpdesk.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: PatchAgentSchedulesRequest = PatchAgentSchedulesRequest.builder() \
		.agent_id("123456") \
		.request_body(PatchAgentSchedulesRequestBody.builder()
					  .agent_schedule(AgentScheduleUpdateInfo.builder().build())
					  .build()) \
		.build()

	# 发起请求
	response: PatchAgentSchedulesResponse = client.helpdesk.v1.agent_schedules.patch(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.helpdesk.v1.agent_schedules.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()