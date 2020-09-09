#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 16:48
# @Author :春衫
# @File :myPayWay.py

from tools.http_request import HttpRequest


def myPayWay(surroundings, cookies):
    # 查询买家各种钱包明细
    myPayWay_url = f"http://m.{surroundings}.hobay.com.cn/ribbon-api/userWallet/myPayWay"
    myPayWay_headers = {"login": ""}
    myPayWay_res = HttpRequest().http_request(myPayWay_url, "get", headers=myPayWay_headers,
                                              cookies=cookies)
    return myPayWay_res.json()
