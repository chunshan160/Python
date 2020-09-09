#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 17:17
# @Author :春衫
# @File :suer.py

from tools.http_request import HttpRequest


def suer(surroundings, orderId, payType, sellerUserId, payPassword, cookies):
    # 确认收货
    suer_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/orders/recieve'
    suer_data = {'orderId': orderId, 'payType': payType, 'sellerUserId': sellerUserId}
    suer_headers = {'login': '', 'payPassword': payPassword}
    suer_res = HttpRequest().http_request(suer_url, 'post', data=suer_data, headers=suer_headers,
                                          cookies=cookies)
    return suer_res
