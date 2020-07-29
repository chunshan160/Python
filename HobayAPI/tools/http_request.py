#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/13 11:32
# @Author :春衫
# @File :http_request.py

import requests


class HttpRequest:

    @staticmethod
    def http_request(url, http_method, **kwargs):
        global res
        try:
            if http_method.lower() == 'get':
                res = requests.get(url, **kwargs)
            elif http_method.lower() == 'post':
                res = requests.post(url, **kwargs)
            else:
                print("输入的请求方式不对")
        except Exception as e:
            print("请求报错了：{0}".format(e))
            raise e
        return res


if __name__ == '__main__':
    url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    json = {"loginValidateType": "CODE", "phone": "13724765586", "validateValue": "666666"}
    res = HttpRequest().http_request(url, "post", json=json)
    print("登录结果是", res.json())

    url2 = 'http://m.test.hobay.com.cn/ribbon-api/charge/saveServiceFeeOrders'  # 充值订单
    data2 = {"payAmount": 10}
    headers2 = {"login": ""}
    res2 = HttpRequest().http_request(url2, "post", data=data2, headers=headers2, cookies=res.cookies)
    print("输入的金额", res2.json())

    # url3="http://m.test.hobay.com.cn/ribbon-api/user/getUser"
    # headers3 = {"login": ""}
    # res3 = HttpRequest().http_request(url3, "post", headers=headers3, cookies=res.cookies)
    # print("获取", res3.json())

    url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    json = {"loginValidateType": "CODE", "phone": "13724765586", "validateValue": "666666"}
    res = HttpRequest().http_request(url, "post", json=json)
    print("登录结果是", res.json())

    url4 = 'http://m.test.hobay.com.cn/ribbon-api/pay/payCash'  # 输入支付密码
    tradeNum = res2.json()['results']['ordersNum']
    data4 = {"tradeNum": tradeNum}
    headers4 = {"login": "", "payPassword": "xqdt77d9tjE="}
    res4 = HttpRequest().http_request(url4, "post", data=data4, headers=headers4, cookies=res.cookies)
    print("充值的金额为", res4.json())
