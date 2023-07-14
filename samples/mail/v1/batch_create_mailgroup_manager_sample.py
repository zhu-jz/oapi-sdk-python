# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.mail.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: BatchCreateMailgroupManagerRequest = lark.mail.v1.BatchCreateMailgroupManagerRequest.builder() \
		.mailgroup_id("xxxxxx 或 test_mail_group@xx.xx") \
		.user_id_type("open_id") \
		.request_body(lark.mail.v1.BatchCreateMailgroupManagerRequestBody.builder()
					  .mailgroup_manager_list([])
					  .build()) \
		.build()

	# 发起请求
	response: BatchCreateMailgroupManagerResponse = client.mail.v1.mailgroup_manager.batch_create(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.mail.v1.mailgroup_manager.batch_create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()