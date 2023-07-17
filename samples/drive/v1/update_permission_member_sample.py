# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.drive.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: UpdatePermissionMemberRequest = UpdatePermissionMemberRequest.builder() \
		.token("doccnBKgoMyY5OMbUG6FioTXuBe") \
		.member_id("ou_7dab8a3d3cdcc9da365777c7ad535d62") \
		.need_notification(False) \
		.type("doc") \
		.request_body(BaseMember.builder()
					  .member_type("openid")
					  .perm("view")
					  .build()) \
		.build()

	# 发起请求
	response: UpdatePermissionMemberResponse = client.drive.v1.permission_member.update(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.drive.v1.permission_member.update failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()