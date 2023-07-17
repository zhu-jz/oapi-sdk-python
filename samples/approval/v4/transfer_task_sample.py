# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.approval.v4 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: TransferTaskRequest = TransferTaskRequest.builder() \
		.user_id_type("user_id") \
		.request_body(TaskTransfer.builder()
					  .approval_code("7C468A54-8745-2245-9675-08B7C63E7A85")
					  .instance_code("81D31358-93AF-92D6-7425-01A5D67C4E71")
					  .user_id("f7cb567e")
					  .comment("OK")
					  .transfer_user_id("f4ip317q")
					  .task_id("12345")
					  .build()) \
		.build()

	# 发起请求
	response: TransferTaskResponse = client.approval.v4.task.transfer(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.approval.v4.task.transfer failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()