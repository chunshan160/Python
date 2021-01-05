#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 15:58
# @Author :春衫
# @File :login.py

from Web.Common.fengyong.tools.http_request import HttpRequest

# 登录
def login(surroundings, phone):
    login_url = f'http://m.{surroundings}.hobay.com.cn/api/app/user/login'  # 登录
    login_data = {"loginValidateType": "CODE", "phone": phone, "validateValue": "666666"}
    login_res = HttpRequest().http_request(login_url, "post", json=login_data)
    return login_res

if __name__ == '__main__':
    surroundings='test'
    phone=17777777781
    a=login(surroundings,phone)