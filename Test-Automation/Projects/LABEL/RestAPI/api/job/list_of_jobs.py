# coding: utf-8
# 项目列表

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def get_list_of_jobs(page="", per_page="", sorts="", search="", task_type_id="", priority="", task_pool_id=""):
    result = common.send_GET_requests(
        "/api/v2/jobs?page=%s&per_page=%s&sorts=%s&search=%s&task_type_id=%s&priority=%s&task_pool_id=%s"
        # "/api/v2/jobs?page=%s&per_page=%s"
        %
        (page, per_page, sorts, search, task_type_id, priority, task_pool_id))
    # (page, per_page))
    print result

    # if len(result["items"]) == per_page:
    #     logger.write_debug(u"获取小组列表信息-接口请求正确")
    # else:
    #     logger.write_error(u"获取小组列表信息-接口请求失败，请求返回的小组个数为为：%s, 请求的小组个数为：%s" %
    #                        (len(result["items"]), per_page))
