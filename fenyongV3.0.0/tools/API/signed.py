#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/10 10:06
# @Author :春衫
# @File :signed.py

from tools.http_request import HttpRequest


def signed(surroundings, orderId, payType, sellerUserId, payPassword, cookies):
    # 签约
    buyer_signed_url = f"http://m.{surroundings}.hobay.com.cn/ribbon-api/orders/signed"
    buyer_signed_data = {"orderId": orderId, "payType": payType, "sellerUserId": sellerUserId}
    buyer_signed_headers = {"login": "", "payPassword": payPassword}
    buyer_signed_res = HttpRequest().http_request(buyer_signed_url, "post", data=buyer_signed_data,
                                                  cookies=cookies,
                                                  headers=buyer_signed_headers)
    return buyer_signed_res
