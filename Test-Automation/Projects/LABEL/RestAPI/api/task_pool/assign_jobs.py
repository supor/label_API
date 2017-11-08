# coding: utf-8
# 分配项目到任务池

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def assign_jobs_to_task_pool(task_pool_id, job_ids, debug):

    data = {
        "task_pool_id": task_pool_id,
        "job_ids": job_ids,
        "debug": debug
    }

    result = common.send_PATCH_requests("/api/v2/task-pools/%s/assignments" % task_pool_id, data)
    print result

    # if result["title"] == data["title"]:
    #     logger.write_debug(u"创建发布组-接口请求正确")
    # else:
    #     logger.write_error(u"创建发布组-接口请求失败")

