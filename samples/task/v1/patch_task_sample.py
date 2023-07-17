# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.task.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: PatchTaskRequest = PatchTaskRequest.builder() \
		.task_id("83912691-2e43-47fc-94a4-d512e03984fa") \
		.user_id_type("user_id") \
		.request_body(PatchTaskRequestBody.builder()
					  .task(Task.builder().build())
					  .update_fields([])
					  .build()) \
		.build()

	# 发起请求
	response: PatchTaskResponse = client.task.v1.task.patch(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.task.v1.task.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()