# coding: utf-8
# 更新任务池

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def update_task_pool(task_pool_id, title, enabled, email_enabled, email_list, workload_email_enabled,
                     workload_email_list, edit_limit_seconds, check_limit_seconds, task_type_id, leaders, inspectors):

    data = {
        "task_pool_id": task_pool_id,
        "title": title,
        "enabled": enabled,
        "email_enabled": email_enabled,
        "email_list": email_list,
        "workload_email_enabled": workload_email_enabled,
        "workload_email_list": workload_email_list,
        "edit_limit_seconds": edit_limit_seconds,
        "check_limit_seconds": check_limit_seconds,
        "task_type_id": task_type_id,
        "leaders": leaders,
        "inspectors": inspectors
    }

    result = common.send_PATCH_requests("/api/v2/task-pools/%s" % task_pool_id, data)
    print result

    # if result["title"] == data["title"]:
    #     logger.write_debug(u"创建发布组-接口请求正确")
    # else:
    #     logger.write_error(u"创建发布组-接口请求失败")

