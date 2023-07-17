# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.auth.v3 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: InternalAppAccessTokenRequest = InternalAppAccessTokenRequest.builder() \
		.request_body(InternalAppAccessTokenRequestBody.builder()
					  .app_id("cli_hsjeriogfkd93jf84")
					  .app_secret("jdsfslkjdg8e73hdf9237enbd")
					  .build()) \
		.build()

	# 发起请求
	response: InternalAppAccessTokenResponse = client.auth.v3.app_access_token.internal(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.auth.v3.app_access_token.internal failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()