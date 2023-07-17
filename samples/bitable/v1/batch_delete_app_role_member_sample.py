# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.bitable.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: BatchDeleteAppRoleMemberRequest = BatchDeleteAppRoleMemberRequest.builder() \
		.app_token("bascnnKKvcoUblgmmhZkYqabcef") \
		.role_id("rolNGhPqks") \
		.request_body(BatchDeleteAppRoleMemberRequestBody.builder()
					  .member_list([])
					  .build()) \
		.build()

	# 发起请求
	response: BatchDeleteAppRoleMemberResponse = client.bitable.v1.app_role_member.batch_delete(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.bitable.v1.app_role_member.batch_delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()