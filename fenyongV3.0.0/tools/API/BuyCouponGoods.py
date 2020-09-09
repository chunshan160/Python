#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/28 11:48
# @Author :春衫
# @File :BuyCouponGoods.py
import time

from tools.API.AcceptOrder import AcceptOrder
from tools.API.SaveOrder import SaveOrder
from tools.API.address_id import get_address_id
from tools.API.consume import consume
from tools.API.login import login
from tools.API.pay import Pay
from tools.API.productStockId import get_productStockId
from tools.API.get_qrCode import get_qrCode
from tools.http_request import HttpRequest


def buy_coupon_goods(surroundings, buyer_phone, seller_phone, product_name, payType, payPassword):
    # 卖家登录
    seller_login_res = login(surroundings, seller_phone)
    # print("登录结果是：", seller_login_res.json())

    # 获取商品productStockId
    productStockId = get_productStockId(surroundings, product_name, cookies=seller_login_res.cookies)

    # 买家登录
    buyer_login_res = login(surroundings, buyer_phone)
    # print("登录结果是：", buyer_login_res.json())

    # 获取收货地址
    address_res = get_address_id(surroundings, cookies=buyer_login_res.cookies)
    # print("获取收货地址的结果是：", address_res.json())

    # 提交订单
    addressId = address_res.json()['currentUser_receiveAddress_recordList'][0]['id']
    SaveOrder_res = SaveOrder(surroundings, addressId, productStockId, cookies=buyer_login_res.cookies)
    # print("提交订单结果是：", SaveOrder_res.json())

    # 支付订单
    orderNum = SaveOrder_res.json()['data']['orderNum']
    pay_res = Pay(surroundings, orderNum, payPassword, payType, cookies=buyer_login_res.cookies)
    # print("支付订单的结果是：", pay_res.json())

    # 卖家确认订单
    orderId = SaveOrder_res.json()['data']['orderId']
    AcceptOrder_res = AcceptOrder(surroundings, orderId, cookies=seller_login_res.cookies)
    # print("确认订单的结果是：", AcceptOrder_res.json())

    # 获取买家订单序列号
    qrCode = get_qrCode(surroundings, orderId, buyer_login_res.cookies)
    # print("买家订单序列号是：", qrCode)

    # 卖家确认序列号
    buyerUserId = buyer_login_res.json()['userId']
    consume_res = consume(surroundings, orderId, payType, buyerUserId, qrCode, payPassword,
                          cookies=seller_login_res.cookies)
    # print('确认收货的结果是：', consume_res.json())

    return orderNum


if __name__ == '__main__':
    # buy_coupon_goods("test", 13724765586,17777777781, "一天两件本地生活", 3,"gQyzNznHAvc=")
    buy_coupon_goods("test", 13724765586, 17777777781, "两天一件本地生活", 3, "gQyzNznHAvc=")
