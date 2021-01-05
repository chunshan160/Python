#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/28 11:48
# @Author :春衫
# @File :BuyCouponGoods.py

from Web.Common import AcceptOrder
from Web.Common import SaveOrder
from Web.Common import consume
from Web.Common.fengyong.API.login import login
from Web.Common.fengyong.API.pay import Pay
from Web.Common.fengyong.API.productStockId import get_productStockId
from Web.Common.fengyong.API.get_qrCode import get_qrCode
from Web.Common import UserLog

my_logger = UserLog()

def buy_coupon_goods(surroundings, buyer_phone, seller_phone, product_name, payType, payPassword):
    # 卖家登录
    seller_login_res = login(surroundings, seller_phone)
    my_logger.debug(f"登录结果是：{seller_login_res.json()}")

    # 获取商品productStockId
    product_data = get_productStockId(surroundings, product_name, cookies=seller_login_res.cookies)
    productId = product_data[0]
    productStockId = product_data[1]

    # 买家登录
    buyer_login_res = login(surroundings, buyer_phone)
    my_logger.debug(f"登录结果是：{buyer_login_res.json()}")

    # 提交订单
    # addressId = address_res.json()['currentUser_receiveAddress_recordList'][0]['id']
    SaveOrder_res = SaveOrder(surroundings,productId, productStockId, cookies=buyer_login_res.cookies)
    my_logger.debug(f"提交订单结果是：{SaveOrder_res.json()}")

    # 支付订单
    orderNum = SaveOrder_res.json()['data']['orderNum']
    pay_res = Pay(surroundings, orderNum, payPassword, payType, cookies=buyer_login_res.cookies)
    my_logger.debug(f"支付订单的结果是：{pay_res.json()}")

    # 卖家确认订单
    orderId = SaveOrder_res.json()['data']['orderId']
    AcceptOrder_res = AcceptOrder(surroundings, orderId, cookies=seller_login_res.cookies)
    my_logger.debug(f"确认订单的结果是：{AcceptOrder_res.json()}")

    # 获取买家订单序列号
    qrCode = get_qrCode(surroundings, orderId, buyer_login_res.cookies)
    my_logger.debug(f"买家订单序列号是：{qrCode}")

    # 卖家确认序列号
    buyerUserId = buyer_login_res.json()['userId']
    consume_res = consume(surroundings, orderId, payType, buyerUserId, qrCode, payPassword,
                          cookies=seller_login_res.cookies)
    my_logger.debug(f'卖家确认序列号的结果是：{consume_res.json()}')

    return orderNum


if __name__ == '__main__':
    # buy_coupon_goods("test", 13724765586,17777777781, "一天两件本地生活", 3,"gQyzNznHAvc=")
    buy_coupon_goods("test", 13724765586, 17777777781, "两天一件本地生活", 3, "gQyzNznHAvc=")
