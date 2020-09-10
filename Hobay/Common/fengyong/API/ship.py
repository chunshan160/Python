#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 17:14
# @Author :春衫
# @File :ship.py


from Common.fengyong.tools.http_request import HttpRequest


def ship(surroundings, orderId, payType, buyer_userId, cookies):
    # 发货
    ship_url = f'http://m.{surroundings}.hobay.com.cn/orders/sendProduct'

    ship_data = {'orderId': orderId, 'payType': payType, 'buyerUserId': buyer_userId, 'type': 1,
                 'logisticsCompany': '德邦物流', 'companyNum': 'debangwuliu', 'logisticsNum': '123456789'}
    ship_headers = {'login': ''}
    ship_res = HttpRequest().http_request(ship_url, 'post', data=ship_data, headers=ship_headers,
                                          cookies=cookies)
    return ship_res
