# coding: utf-8
# 创建群组

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def create_group_2(name):

    data = {
        "name": name
    }

    result = common.send_POST_requests("/api/v2/groups", data)

    if result["name"] == data["name"]:
        logger.write_debug(u"创建群组-接口请求正确")
    else:
        logger.write_error(u"创建群组-接口请求失败")
