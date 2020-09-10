#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 16:50
# @Author :春衫
# @File :pay.py

from Common.fengyong.tools.http_request import HttpRequest


def Pay(surroundings, orderNum, payPassword, payType, cookies):

    # 查询买家各种钱包明细
    myPayWay_url = f"http://m.{surroundings}.hobay.com.cn/ribbon-api/userWallet/myPayWay"
    myPayWay_headers = {"login": ""}
    myPayWay_res = HttpRequest().http_request(myPayWay_url, "get", headers=myPayWay_headers,
                                              cookies=cookies)

    # 支付订单
    pay_headers = {"login": "", "payPassword": payPassword}
    if payType in [3, 4]:
        pay_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/batchOrders/payAllCBP'
        pay_data = {"tradeNUm": orderNum, "payType": payType, "shareWalletUserId": "", "shareWalletId": ""}
        pay_res = HttpRequest().http_request(pay_url, "post", json=pay_data, cookies=cookies,
                                             headers=pay_headers)
    elif payType in [5, 6]:
        if payType == 5:
            shareWalletUserId = myPayWay_res.json()['results']['myPayWay']['myKinship'][0]['shareWalletUserId']
            shareWalletId = myPayWay_res.json()['results']['myPayWay']['myKinship'][0]['shareWalletId']
        elif payType == 6:
            shareWalletUserId = myPayWay_res.json()['results']['myPayWay']['myWages']['shareWalletUserId']
            shareWalletId = myPayWay_res.json()['results']['myPayWay']['myWages']['shareWalletId']
        pay_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/batchOrders/payAllCBP'
        pay_data = {"tradeNUm": orderNum, "payType": payType, "shareWalletUserId": shareWalletUserId,
                    "shareWalletId": shareWalletId}
        pay_res = HttpRequest().http_request(pay_url, "post", json=pay_data, cookies=cookies,
                                             headers=pay_headers)
    elif payType == 7:
        pay_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/pay/payCash'
        pay_data = {"tradeNum": orderNum}
        pay_res = HttpRequest().http_request(pay_url, "post", data=pay_data, cookies=cookies,
                                         headers=pay_headers)
    return pay_res
