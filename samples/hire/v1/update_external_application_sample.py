# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.hire.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: UpdateExternalApplicationRequest = UpdateExternalApplicationRequest.builder() \
		.external_application_id("6960663240925956660") \
		.request_body(ExternalApplication.builder()
					  .external_id("123")
					  .job_recruitment_type(1)
					  .job_title("高级Java")
					  .resume_source("lagou")
					  .stage("1")
					  .talent_id("6960663240925956459")
					  .termination_reason("不合适")
					  .delivery_type(1)
					  .modify_time(1618500278645)
					  .termination_type("health")
					  .build()) \
		.build()

	# 发起请求
	response: UpdateExternalApplicationResponse = client.hire.v1.external_application.update(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.hire.v1.external_application.update failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()