# coding: utf-8
# 修改用户配置信息V2

import Projects.LABEL.RestAPI.api.common.api_common as common
import framework.taf_logging as logger


def update_user_profile(user_id, real_name, id_number, email, phone, alipay):
    data = {
        "real_name": real_name,
        "id_number": id_number,
        "email": email,
        "phone": phone,
        "alipay": alipay
    }

    result = common.send_PUT_requests("/api/v2/users/%s/profile" % user_id, data)

    if result["id"] == user_id:
        logger.write_debug(u"修改用户配置信息-用户id返回正确")
    else:
        logger.write_error(u"修改用户配置信息-用户id返回失败")

    if result["real_name"] == real_name:
        logger.write_debug(u"修改用户配置信息-用户真实姓名返回正确")
    else:
        logger.write_error(u"修改用户配置信息-用户真实姓名返回失败")

    if result["id_number"] == id_number:
        logger.write_debug(u"修改用户配置信息-用户身份证信息返回正确")
    else:
        logger.write_error(u"修改用户配置信息-用户身份证信息返回失败")

    if result["email"] == email:
        logger.write_debug(u"修改用户配置信息-用户邮件返回正确")
    else:
        logger.write_error(u"修改用户配置信息-用户邮件返回失败")

    if result["phone"] == phone:
        logger.write_debug(u"修改用户配置信息-用户手机号返回正确")
    else:
        logger.write_error(u"修改用户配置信息-用户手机号返回失败")

    if result["alipay"] == alipay:
        logger.write_debug(u"修改用户配置信息-用户支付宝账号返回正确")
    else:
        logger.write_error(u"修改用户配置信息-用户支付宝账号返回失败")


