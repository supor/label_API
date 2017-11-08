# coding: utf-8
# 获取client info(todo)

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def get_client_info(grant_type, username, password, client_id, response_type):

    data = {
        "grant_type": grant_type,
        "username": username,
        "password": password,
        "client_id": client_id,
        "response_type": response_type,
        "return_url": ""
    }

    result = common.send_POST_requests("/api/v2/token", data)
    print result

    # if result["id"] == user_id:
    #     logger.write_debug(u"修改用户属性-接口请求正确")
    # else:
    #     logger.write_error(u"修改用户属性-接口请求失败")

