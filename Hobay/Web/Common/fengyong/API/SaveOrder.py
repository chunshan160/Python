#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 16:45
# @Author :春衫
# @File :SaveOrder.py

from Web.Common.fengyong.tools.http_request import HttpRequest


def SaveOrder(surroundings,productId, productStockId, cookies, addressId=""):
    SaveOrder_headers = {"login": ""}
    # 获取商品类型
    type_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/batchCart/immediatelyBuySettlement'
    type_data = {"productStockIdAndNums": [{"num": 1, "productStockId": productStockId, "productId": productId}]}
    type_res = HttpRequest().http_request(type_url, "post", json=type_data,
                                          cookies=cookies,
                                          headers=SaveOrder_headers)
    goods_type = type_res.json()['data']['type']

    # 提交订单
    SaveOrder_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/batchOrders/immediatelySaveOrder'
    SaveOrder_data = {"message": "", "couponUserId": "", "addressId": addressId,
                      "productStockIdAndNums": [{"num": 1, "productStockId": productStockId}], "type": goods_type}
    SaveOrder_res = HttpRequest().http_request(SaveOrder_url, "post", json=SaveOrder_data,
                                               cookies=cookies,
                                               headers=SaveOrder_headers)
    return SaveOrder_res
