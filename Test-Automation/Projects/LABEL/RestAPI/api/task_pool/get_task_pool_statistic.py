# coding: utf-8
# 获取任务池统计信息

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def get_task_pool_statistic(page, per_page, task_type_id, user_type_id, start_date, end_date):

    result = common.send_GET_requests(
        "/api/v2/task-pools/statistic?page=%s&per_page=%s&task_type_id=%s&user_type_id=%s&start_date=%s&end_date=%s"
        % (page, per_page, task_type_id, user_type_id, start_date, end_date))
    print result

    # if result["title"] == data["title"]:
    #     logger.write_debug(u"创建发布组-接口请求正确")
    # else:
    #     logger.write_error(u"创建发布组-接口请求失败")

