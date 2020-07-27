#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/16 13:15
# @Author :春衫
# @File :123.py

# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/13 11:32
# @Author :春衫
# @File :http_request.py


import requests
from tools.my_log import MyLog

my_logger = MyLog()


class HttpRequest:

    def http_request(self, url, data, http_method, **args):
        try:
            if http_method.lower() == 'get':
                res = requests.get(url, data, **args)
            elif http_method.lower() == 'post':
                res = requests.post(url, data, **args)
            return res
        except Exception as e:
            my_logger.error("请求报错了：{0}".format(e))
            raise e


if __name__ == '__main__':
    # url='http://8.129.65.165:8080/futureloan/mvc/api//member/register'
    # data={'mobilephone': "13724765587", 'pwd': '123456', 'regname': 'ceshi'}
    # login_res = HttpRequest().http_request(url, data, 'post')
    # print("登录结果是：", login_res.json())

    # 登录
    login_url = 'http://8.129.65.165:8080/futureloan/mvc/api/member/login'
    login_data = {"mobilephone": "13724765586", "pwd": "123456"}
    login_res = HttpRequest().http_request(login_url, login_data, 'post')
    print("登录结果是：", login_res.json())
    #
    # 充值
    recharge_url = "http://8.129.65.165:8080/futureloan/mvc/api/member/recharge"
    cookies = login_res.cookies
    recharge_data = {"mobilephone": "13724765586", "amount": "1000"}
    recharge_res = HttpRequest().http_request(recharge_url, recharge_data, 'get', cookies=cookies)
    print("充值结果是：", recharge_res.json())
