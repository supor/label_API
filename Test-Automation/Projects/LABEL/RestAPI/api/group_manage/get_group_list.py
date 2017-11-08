# coding: utf-8
# 获取小组列表信息

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def get_group_list(page, per_page):

    result = common.send_GET_requests("/api/v2/teams?page=%s&per_page=%s" % (page, per_page))

    if len(result["items"]) == per_page:
        logger.write_debug(u"获取小组列表信息-接口请求正确")
    else:
        logger.write_error(u"获取小组列表信息-接口请求失败，请求返回的小组个数为为：%s, 请求的小组个数为：%s" %
                           (len(result["items"]), per_page))

