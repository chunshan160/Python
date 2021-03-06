#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/1 0:57
# @Author :春衫
# @File :delete_partner.py

from Web.Common.fengyong.tools.http_request import HttpRequest
from Web.Common import UserLog

my_logger = UserLog()

def delete_partner(surroundings,seller_phone, userId):
    # 卖家登录
    login_url = f'http://m.{surroundings}.hobay.com.cn/api/app/user/login'  # 登录
    seller_login_data = {"loginValidateType": "CODE", "phone": seller_phone, "validateValue": "666666"}
    seller_login_res = HttpRequest().http_request(login_url, "post", json=seller_login_data)
    my_logger.debug(f"登录结果是：{seller_login_res.json()}")

    url = f'http://m.{surroundings}.hobay.com.cn/api/user/partnership/delPartnership?userId={userId}'
    headers = {"login": ""}
    res = HttpRequest.http_request(url, "get", headers=headers, cookies=seller_login_res.cookies)
    my_logger.debug(f"删除伙伴的结果是：{res.status_code}")