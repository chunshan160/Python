#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 17:34
# @Author :春衫
# @File :get_qrCode.py

from Common.fengyong.tools.http_request import HttpRequest


def get_qrCode(surroundings, orderId, cookies):
    # 获取买家订单序列号
    OrderDetail_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/batchOrders/queryOrderDetail'
    OrderDetail_data = {"orderId": orderId, "buyOrSell": 1}
    OrderDetail_headers = {'login': ''}
    OrderDetail_res = HttpRequest().http_request(OrderDetail_url, 'post', data=OrderDetail_data,
                                                 headers=OrderDetail_headers,
                                                 cookies=cookies)
    qrCode = OrderDetail_res.json()['data']['qrCode']
    return qrCode
