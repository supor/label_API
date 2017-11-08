# coding: utf-8
# 获取用户配置信息(todo)

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def get_user_profile(user_id):
    result = common.send_GET_requests("/api/v2/users/%s/profile" % user_id)

    if result["id"] == user_id:
        logger.write_debug(u"获取用户配置信息-接口请求正确")
    else:
        logger.write_error(u"获取用户配置信息-接口请求失败")

