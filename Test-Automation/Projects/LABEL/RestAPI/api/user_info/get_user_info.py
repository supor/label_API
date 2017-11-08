# coding: utf-8
# 获取指定类型用户的信息(todo)

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def get_user_info(role_name
                  # page, per_page, user_state, role_admin, role_manager, role_leader, role_editor,
                  #    role_checker, role_sampler, role_publisher, user_type_id, publisher_group_id
                  ):

    # data = {
    #     "page": page,
    #     "per_page": per_page,
    #     "user_state": user_state,  # 用户状态
    #     "role_admin": role_admin,  # 是否是系统管理员
    #     "role_manager": role_manager,  # 是否任务管理员，可选值[0, 1]
    #     "role_leader": role_leader,  # 是否小组长，可选值[0, 1]
    #     "role_editor": role_editor,  # 是否标注员，可选值[0, 1]
    #     "role_checker": role_checker,  # 是否检查员，可选值[0, 1]
    #     "role_sampler": role_sampler,  # 是否抽查员, 可选值[0, 1]
    #     "role_publisher": role_publisher,  # 是否发布者, 可选值[0, 1]
    #     "user_type_id": user_type_id,  # 用户类型, 可选值[0, 1]
    #     "publisher_group_id": publisher_group_id  # 是否冻结用户, 可选值[0, 1]
    # }

    result = common.send_GET_requests("/api/v2/users/s/%ss" % role_name)
    print result

    # if result["id"] == user_id:
    #     logger.write_debug(u"修改用户属性-接口请求正确")
    # else:
    #     logger.write_error(u"修改用户属性-接口请求失败")

