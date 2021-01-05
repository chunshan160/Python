#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 17:12
# @Author :春衫
# @File :AcceptOrder.py

from Web.Common.fengyong.tools.http_request import HttpRequest


# 确认订单
def AcceptOrder(surroundings, orderId, cookies):
    order_data = {'orderStatus': 0,
                  'buyOrSell': 2,
                  'type': 0,
                  'currentPage': 1,
                  'pageSize': 10}
    AcceptOrder_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/orders/acceptOrder?orderId={orderId}'
    AcceptOrder_headers = {"login": ""}
    AcceptOrder_res = HttpRequest().http_request(AcceptOrder_url, "get", json=order_data,
                                                 cookies=cookies, headers=AcceptOrder_headers)
    return AcceptOrder_res
