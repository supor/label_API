# coding: utf-8
# 增加采集数据(todo)

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def gather_job(data, job_id):

    data = {
        "data": data,
        "job_id": job_id,
    }

    result = common.send_POST_requests("/api/v2/gather-jobs/%s/units" % job_id, data)

    if result["name"] == data["name"]:
        logger.write_debug(u"创建小组-接口请求正确, 小组名称正确")
    else:
        logger.write_error(u"创建小组-接口请求失败，小组名称错误")
