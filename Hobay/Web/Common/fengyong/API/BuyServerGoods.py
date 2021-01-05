#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/29 10:11
# @Author :春衫
# @File :BuyServerGoods.py

from Web.Common import AcceptOrder
from Web.Common import SaveOrder
from Web.Common.fengyong.API.login import login
from Web.Common.fengyong.API.pay import Pay
from Web.Common.fengyong.API.productStockId import get_productStockId
from Web.Common.fengyong.API.signed import signed
from Web.Common import UserLog

my_logger = UserLog()

def buy_server_goods(surroundings, buyer_phone, seller_phone, product_name, payType, payPassword):
    # 卖家登录
    seller_login_res = login(surroundings, seller_phone)
    my_logger.debug(f"卖家登录结果是：{seller_login_res.json()}")

    # 获取商品productStockId
    product_data=get_productStockId(surroundings, product_name, cookies=seller_login_res.cookies)
    productId=product_data [0]
    productStockId =product_data [1]

    # 买家登录
    buyer_login_res = login(surroundings, buyer_phone)
    my_logger.debug(f"登录结果是：{buyer_login_res.json()}")

    # 买家提交订单
    buyer_SaveOrder_res = SaveOrder(surroundings,productId, productStockId, cookies=buyer_login_res.cookies)
    my_logger.debug(f"提交订单结果是：{buyer_SaveOrder_res.json()}")

    # 支付订单
    orderNum = buyer_SaveOrder_res.json()['data']['orderNum']
    pay_res = Pay(surroundings, orderNum, payPassword, payType, cookies=buyer_login_res.cookies)
    my_logger.debug(f"支付订单的结果是：{pay_res.json()}")

    # 确认订单
    orderId = buyer_SaveOrder_res.json()['data']['orderId']
    seller_AcceptOrder_res = AcceptOrder(surroundings, orderId, cookies=seller_login_res.cookies)
    my_logger.debug(f"确认订单的结果是：{seller_AcceptOrder_res.json()}")

    # 签约
    sellerUserId = seller_login_res.json()['userId']
    buyer_signed_res=signed(surroundings, orderId, payType, sellerUserId, payPassword, buyer_login_res.cookies)
    my_logger.debug(f"签约的结果是：{buyer_signed_res.json()}")

    return orderNum


if __name__ == '__main__':
    # buy_server_goods("test", 13724765586, 17777777781, "一天两件商企服务", 3, "gQyzNznHAvc=")
    buy_server_goods("test", 13724765586, 17777777781, "两天一件商企服务", 3, "gQyzNznHAvc=")
