# coding: utf-8
# 任务batch-task batch 列表

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger
import json


def get_list_of_task_batch(task_type_id, page, per_page, sorts, search):

    result = common.send_GET_requests("/api/v2/task-batches?task_type_id=%s&page=%s&per_page=%s&sorts=%s&search=%s" % (task_type_id, page, per_page, sorts, search))

    print json.dumps(result, sort_keys=True, indent=2)

    # if result["name"] == data["name"]:
    #     logger.write_debug(u"创建小组-接口请求正确, 小组名称正确")
    # else:
    #     logger.write_error(u"创建小组-接口请求失败，小组名称错误")
