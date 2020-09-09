#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 16:45
# @Author :春衫
# @File :SaveOrder.py

from tools.http_request import HttpRequest


def SaveOrder(surroundings, addressId, productStockId, cookies):
    # 提交订单
    SaveOrder_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/batchOrders/immediatelySaveOrder'
    if
    SaveOrder_data = {"message": "", "couponUserId": "", "addressId": addressId,
                      "productStockIdAndNums": [{"num": 1, "productStockId": productStockId}], "type": 1}

    SaveOrder_data = {"message": "", "couponUserId": "", "addressId": addressId,
                      "productStockIdAndNums": [{"num": 1, "productStockId": productStockId}], "type": 2}

    SaveOrder_data = {"message": "", "couponUserId": "", "addressId": addressId,
                      "productStockIdAndNums": [{"num": 1, "productStockId": productStockId}], "type": 3}

    SaveOrder_headers = {"login": ""}
    SaveOrder_res = HttpRequest().http_request(SaveOrder_url, "post", json=SaveOrder_data,
                                               cookies=cookies,
                                               headers=SaveOrder_headers)
    return SaveOrder_res
