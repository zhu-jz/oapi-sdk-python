# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.authen.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: CreateRefreshAccessTokenRequest = CreateRefreshAccessTokenRequest.builder() \
		.request_body(CreateRefreshAccessTokenRequestBody.builder()
					  .grant_type("refresh_token")
					  .refresh_token("ur-oQ0mMq6MCcueAv0pwx2fQQhxqv__CbLu6G8ySFwafeKww2Def2BJdOkW3.9gCFM.LBQgFri901QaqeuL")
					  .build()) \
		.build()

	# 发起请求
	response: CreateRefreshAccessTokenResponse = client.authen.v1.refresh_access_token.create(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.authen.v1.refresh_access_token.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()