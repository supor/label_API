# coding: utf-8
# 创建发布组

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def create_publisher_group(title):

    data = {
        "title": title
    }

    result = common.send_POST_requests("/api/v2/publisher-groups", data)

    if result["title"] == data["title"]:
        logger.write_debug(u"创建发布组-接口请求正确")
    else:
        logger.write_error(u"创建发布组-接口请求失败")

