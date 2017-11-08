# coding: utf-8
# 更新发布组

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def update_publisher_group(publisher_group_id, title):
    data = {
        "publisher_group_id": publisher_group_id,
        "title": title
    }

    result = common.send_PUT_requests("/api/v2/publisher-groups/%s" % publisher_group_id, data)

    if result["id"] == publisher_group_id:
        logger.write_debug(u"修改发布组-接口请求成功，返回的发布组id正确")
    else:
        logger.write_error(u"修改发布组-接口请求失败，返回的发布组id失败，返回的发布组id为：%s, 请求修改的发布组id为：%s"
                           % (result["id"], publisher_group_id))

    if result["title"] == title:
        logger.write_debug(u"修改发布组-接口请求成功，返回的发布组名称正确")
    else:
        logger.write_error(u"修改发布组-接口请求失败，返回的发布组名称失败，返回的发布组名称为：%s, 请求修改的发布组名称为：%s"
                           % (result["title"], title))

