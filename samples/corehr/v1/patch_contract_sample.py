# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: PatchContractRequest = PatchContractRequest.builder() \
		.contract_id("1616161616") \
		.client_token("12454646") \
		.request_body(Contract.builder()
					  .effective_time("2050-01-01 00:00:00")
					  .expiration_time("9999-12-31 23:59:59")
					  .employment_id("6893013238632416776")
					  .contract_type(Enum.builder().build())
					  .first_party_company_id("6892686614112241165")
					  .person_id("151515151")
					  .custom_fields([])
					  .duration_type(Enum.builder().build())
					  .contract_end_date("2006-01-02")
					  .contract_number("6919737965274990093")
					  .signing_type(Enum.builder().build())
					  .build()) \
		.build()

	# 发起请求
	response: PatchContractResponse = client.corehr.v1.contract.patch(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.corehr.v1.contract.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()