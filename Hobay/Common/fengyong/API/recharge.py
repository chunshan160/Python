#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/10 11:02
# @Author :春衫
# @File :recharge.py

from Common.fengyong.tools.http_request import HttpRequest


def recharge(surroundings, payAmount, cookies):
    # 提交充值订单
    recharge_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/charge/saveServiceFeeOrders'
    recharge_data = {"payAmount": payAmount}
    recharge_headers = {"login": ""}
    recharge_res = HttpRequest.http_request(recharge_url, "post", data=recharge_data, headers=recharge_headers,
                                            cookies=cookies)
    return recharge_res
