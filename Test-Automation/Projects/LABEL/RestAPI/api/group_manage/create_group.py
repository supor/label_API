# coding: utf-8
# 创建小组

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def create_group(group_name, leaders, members):

    data = {
        "name": group_name,
        "leaders": leaders,
        "members": members
    }

    result = common.send_POST_requests("/api/v2/teams", data)

    if result["name"] == data["name"]:
        logger.write_debug(u"创建小组-接口请求正确, 小组名称正确")
    else:
        logger.write_error(u"创建小组-接口请求失败，小组名称错误")

    for i in range(0, len(leaders)):
        if result["leaders"][i]["user_id"] == data["leaders"][i]:
            logger.write_debug(u"创建小组-接口请求正确, 小组长正确")
        else:
            logger.write_error(u"创建小组-接口请求失败，小组长错误")
    for j in range(0, len(members)):
        if result["members"][j]["user_id"] == data["members"][j]:
            logger.write_debug(u"创建小组-接口请求正确, 小组成员正确")
        else:
            logger.write_error(u"创建小组-接口请求失败，小组成员错误")
