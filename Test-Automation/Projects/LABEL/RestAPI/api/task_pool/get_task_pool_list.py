# coding: utf-8
# 获取任务池列表

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def get_list_of_task_pool(task_type_id, user_id, enabled):

    result = common.send_GET_requests("/api/v2/task-pools?task_type_id=%s&user_id=%s&enabled=%s" %
                                      (task_type_id, user_id, enabled))
    print result

    # if result["title"] == data["title"]:
    #     logger.write_debug(u"创建发布组-接口请求正确")
    # else:
    #     logger.write_error(u"创建发布组-接口请求失败")

