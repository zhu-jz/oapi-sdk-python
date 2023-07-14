# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.hire.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: UpdateOfferRequest = lark.hire.v1.UpdateOfferRequest.builder() \
		.offer_id("7016605170635213100") \
		.user_id_type("open_id") \
		.department_id_type("open_department_id") \
		.request_body(lark.hire.v1.OfferInfo.builder()
					  .schema_id("7013318077945596204")
					  .basic_info(OfferBasicInfo.builder().build())
					  .salary_info(OfferSalaryInfo.builder().build())
					  .customized_info_list([])
					  .build()) \
		.build()

	# 发起请求
	response: UpdateOfferResponse = client.hire.v1.offer.update(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.hire.v1.offer.update failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()