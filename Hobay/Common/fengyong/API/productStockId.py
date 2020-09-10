#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 16:04
# @Author :春衫
# @File :productStockId.py

from Common.fengyong.tools.http_request import HttpRequest
from Common.user_log import UserLog

my_logger = UserLog()

# 获取商品productStockId
def get_productStockId(surroundings, product_name, cookies):
    # 卖家-商品管理
    product_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/product/queryPageProductsByType?currentPage=1&type=2&pageSize=10'
    product_headers = {"login": ""}
    product_res = HttpRequest().http_request(product_url, "get", headers=product_headers,
                                             cookies=cookies)
    my_logger.debug(f"商品管理出售中的商品是：{product_res.json()}")

    # 获取商品规格id
    product_data = product_res.json()['data']['result']
    for i in range(0, len(product_data)):
        if product_data[i]['title'] == product_name:
            productId=product_data[i]['id']
            productStockId = product_data[i]['productStockWithStockImages'][0]['id']
            return productId,productStockId
