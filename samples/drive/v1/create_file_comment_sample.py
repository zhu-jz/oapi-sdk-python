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
	request: CreateFileCommentRequest = CreateFileCommentRequest.builder() \
		.file_token("doccnGp4UK1UskrOEJwBXd3****") \
		.file_type("doc") \
		.user_id_type("user_id") \
		.request_body(FileComment.builder()
					  .comment_id("str")
					  .user_id("str")
					  .create_time(int)
					  .update_time(int)
					  .is_solved(bool)
					  .solved_time(int)
					  .solver_user_id("str")
					  .has_more(bool)
					  .page_token("str")
					  .is_whole(bool)
					  .quote("str")
					  .reply_list(ReplyList.builder().build())
					  .build()) \
		.build()

	# 发起请求
	response: CreateFileCommentResponse = client.drive.v1.file_comment.create(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.drive.v1.file_comment.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()