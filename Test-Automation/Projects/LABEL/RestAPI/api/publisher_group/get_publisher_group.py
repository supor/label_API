# coding: utf-8
# 获取发布组

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def get_publisher_group(publisher_group_id):

    result = common.send_GET_requests("/api/v2/publisher-groups/%s" % publisher_group_id)

    if result["id"] == publisher_group_id:
        logger.write_debug(u"获取发布组-接口请求正确")
    else:
        logger.write_error(u"获取发布组-接口请求失败")

