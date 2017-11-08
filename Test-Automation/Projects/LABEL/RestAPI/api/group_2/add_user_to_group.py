# coding: utf-8
# 增加一个用户到群组里

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def add_user_to_group(group_id, user_id):

    result = common.send_PUT_requests("/api/v2/groups/%s/users/%s" % (group_id, user_id))

    if result["user_id"] == user_id:
        logger.write_debug(u"增加user到群组-接口请求正确")
    else:
        logger.write_error(u"增加user到群组-接口请求失败")
