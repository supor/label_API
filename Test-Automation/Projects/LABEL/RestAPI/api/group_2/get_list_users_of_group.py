# coding: utf-8
# 获取群组里的用户

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def get_list_users_of_group(group_id):

    result = common.send_GET_requests("/api/v2/groups/%s/users" % group_id)

    print result

    # if result["user_id"] == user_id:
    #     logger.write_debug(u"增加user到群组-接口请求正确")
    # else:
    #     logger.write_error(u"增加user到群组-接口请求失败")
