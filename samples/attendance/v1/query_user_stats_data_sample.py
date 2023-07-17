# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.attendance.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: QueryUserStatsDataRequest = QueryUserStatsDataRequest.builder() \
		.employee_type("employee_id") \
		.request_body(QueryUserStatsDataRequestBody.builder()
					  .locale("zh")
					  .stats_type("month")
					  .start_date(20210316)
					  .end_date(20210323)
					  .user_ids([])
					  .need_history(True)
					  .current_group_only(True)
					  .user_id("ec8ddg56")
					  .build()) \
		.build()

	# 发起请求
	response: QueryUserStatsDataResponse = client.attendance.v1.user_stats_data.query(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.attendance.v1.user_stats_data.query failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()