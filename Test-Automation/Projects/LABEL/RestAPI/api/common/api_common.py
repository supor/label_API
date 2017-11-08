# coding: utf-8

import requests
import json
# import Projects.LABEL.RestAPI.mysql.mysqlManagments as mysql
import api_config as config

import framework.taf_logging as logger


def send_POST_requests(uri, data):
    """
    Send post requests
    :param uri:
    :param data:
    :return:
    """
    # 请求头
    headers = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "postman-token": "da3cfad2-33fb-9c66-7c67-61023951af07",
        "Cookie": config.COOKIE
    }
    # 拼接请求url
    url = config.BASE_URL + uri
    logger.write_debug(u'请求url: %s' % url)
    logger.write_debug(u'请求方式: POST')
    logger.write_debug(u'请求参数: %s' % data)
    logger.write_debug(u'请求头部: %s' % headers)
    response = requests.post(url, data=json.dumps(data), headers=headers)
    result = response.json()
    logger.write_debug(u"请求接口后，返回的结果为： %s" % json.dumps(result, sort_keys=True, indent=2))
    return result


def send_GET_requests(uri, data=None):
    """
    Send GET requests
    :param data: 
    :param uri:
    :return:
    """
    # 请求头
    headers = {
        # "content-type": "application/json",
        "cache-control": "no-cache",
        "postman-token": "da3cfad2-33fb-9c66-7c67-61023951af07",
        "Cookie": config.COOKIE
    }
    # 拼接请求url
    url = config.BASE_URL + uri
    logger.write_debug(u'请求url: %s' % url)
    logger.write_debug(u'请求方式: GET')
    logger.write_debug(u'请求头部: %s' % headers)
    response = requests.get(url, headers=headers, data=data)
    result = response.json()
    logger.write_debug(u"请求接口后，返回的结果为： %s" % result)
    return result


def send_PUT_requests(uri):
    """
    Send post requests
    :param uri:
    :param data:
    :return:
    """
    # 请求头
    headers = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "postman-token": "da3cfad2-33fb-9c66-7c67-61023951af07",
        "Cookie": config.COOKIE
    }
    # 拼接请求url
    url = config.BASE_URL + uri
    logger.write_debug(u'请求url: %s' % url)
    logger.write_debug(u'请求方式: PUT')
    logger.write_debug(u'请求头部: %s' % headers)
    response = requests.put(url, headers=headers)
    result = response.json()
    logger.write_debug(u"请求接口后，返回的结果为： %s" % result)
    return result


def send_PATCH_requests(uri, data):
    """
    Send post requests
    :param uri:
    :param data:
    :return:
    """
    # 请求头
    headers = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "postman-token": "da3cfad2-33fb-9c66-7c67-61023951af07",
        "Cookie": config.COOKIE
    }
    # 拼接请求url
    url = config.BASE_URL + uri
    logger.write_debug(u'请求url: %s' % url)
    logger.write_debug(u'请求方式: patch')
    logger.write_debug(u'请求头部: %s' % headers)
    response = requests.patch(url, json.dumps(data), headers=headers)
    result = response.json()
    logger.write_debug(u"请求接口后，返回的结果为： %s" % result)
    return result


def send_DELETE_requests(uri):
    """
    Send post requests
    :param uri:
    :return:
    """
    # 请求头
    headers = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "postman-token": "da3cfad2-33fb-9c66-7c67-61023951af07",
        "Cookie": config.COOKIE
    }
    # 拼接请求url
    url = config.BASE_URL + uri
    logger.write_debug(u'请求url: %s' % url)
    logger.write_debug(u'请求方式: PUT')
    logger.write_debug(u'请求头部: %s' % headers)
    response = requests.delete(url, headers=headers)
    result = response.json()
    logger.write_debug(u"请求接口后，返回的结果为： %s" % result)
    return result
