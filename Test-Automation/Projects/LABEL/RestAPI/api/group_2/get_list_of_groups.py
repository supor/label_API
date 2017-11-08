# coding: utf-8
# 获取群组信息列表

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def get_list_of_groups(page, per_page):

    result = common.send_GET_requests("/api/v2/groups?page=%s&per_page=%s" % (page, per_page))

    print result

    # if result["user_id"] == user_id:
    #     logger.write_debug(u"增加user到群组-接口请求正确")
    # else:
    #     logger.write_error(u"增加user到群组-接口请求失败")
