#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 17:37
# @Author :春衫
# @File :consume.py

from Common.fengyong.tools.http_request import HttpRequest

def consume(surroundings,orderId,payType,buyerUserId,qrCode,payPassword,cookies):
    # 卖家确认序列号
    consume_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/orders/consume'
    consume_data = {"orderId": orderId,
                    "payType": payType,
                    "buyerUserId": buyerUserId,
                    "qrCode": qrCode}
    consume_headers = {'login': '', 'payPassword': payPassword}
    consume_res = HttpRequest().http_request(consume_url, 'post', data=consume_data, headers=consume_headers,
                                             cookies=cookies)
    return consume_res