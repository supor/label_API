# coding: utf-8
# 修改用户发布组

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def update_user_publisher_group(user_id, publisher_groups):

    data = {
        "publisher_groups": publisher_groups,
    }

    result = common.send_PUT_requests("/api/v2/users/%s/publisher-groups" % user_id, data)

    for i in range(0, len(publisher_groups)):
        if result["publisher_groups"][i]["id"] == publisher_groups[i]:
            logger.write_debug(u"修改用户发布组-接口请求正确")
        else:
            logger.write_error(u"修改用户发布组-接口请求失败")

