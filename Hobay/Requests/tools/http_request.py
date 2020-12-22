#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/13 11:32
# @Author :春衫
# @File :http_request.py


import requests
from Requests.tools.my_log import MyLog

my_logger = MyLog()


class HttpRequest:

    @staticmethod
    def http_request(url, data, http_method, cookie=None):
        global res
        try:
            if http_method.lower() == 'get':
                res = requests.get(url, data, cookies=cookie)
            elif http_method.lower() == 'post':
                res = requests.post(url, data, cookies=cookie)
            else:
                my_logger.info("输入的请求方式不对")
        except Exception as e:
            my_logger.error("请求报错了：{0}".format(e))
            raise e
        return res


if __name__ == '__main__':
    url='http://8.129.65.165:8080/futureloan/mvc/api//member/register'
    data={'mobilephone': "13724765587", 'pwd': '123456', 'regname': 'ceshi'}
    login_res = HttpRequest().http_request(url, data, 'post')
    print("登录结果是：", login_res.json())

    # # 登录
    # login_url = 'http://8.129.65.165:8080/futureloan/mvc/api/member/login'
    # login_data = {"mobilephone": "13724765586", "pwd": "123456"}
    # login_res = HttpRequest().http_request(login_url, login_data, 'post')
    # print("登录结果是：", login_res.json())
    #
    # # 充值
    # recharge_url = "http://8.129.65.165:8080/futureloan/mvc/api/member/recharge"
    # recharge_data = {"mobilephone": "13724765586", "amount": "1000"}
    # recharge_res = HttpRequest().http_request(recharge_url, recharge_data, 'get', login_res.cookies, )
    # print("充值结果是：", recharge_res.json())
