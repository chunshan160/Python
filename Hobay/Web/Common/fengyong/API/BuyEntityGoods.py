#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/28 11:48
# @Author :春衫
# @File :BuyEntityGoods.py
from Web.Common.fengyong.API.login import login
from Web.Common.fengyong.API.productStockId import get_productStockId
from Web.Common import get_address_id
from Web.Common import SaveOrder
from Web.Common.fengyong.API.pay import Pay
from Web.Common import AcceptOrder
from Web.Common.fengyong.API.ship import ship
from Web.Common.fengyong.API.suer import suer
from Web.Common import UserLog

my_logger = UserLog()

def bug_entity_goods(surroundings, buyer_phone, seller_phone, product_name, payType, payPassword):
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

    # 获取收货地址
    buyer_address_res = get_address_id(surroundings, cookies=buyer_login_res.cookies)
    my_logger.debug(f"获取收货地址的结果是：{buyer_address_res.json()}")

    # 提交订单
    buyer_addressId = buyer_address_res.json()['currentUser_receiveAddress_recordList'][0]['id']
    buyer_SaveOrder_res = SaveOrder(surroundings, productId, productStockId, buyer_login_res.cookies, buyer_addressId)
    my_logger.debug(f"提交订单结果是：{buyer_SaveOrder_res.json()}")

    # 支付订单
    buyer_orderNum = buyer_SaveOrder_res.json()['data']['orderNum']
    buyer_pay_res = Pay(surroundings, buyer_orderNum, payPassword, payType, cookies=buyer_login_res.cookies)
    my_logger.debug(f"支付订单的结果是：{buyer_pay_res.json()}")

    # 卖家确认订单
    buyer_orderId = buyer_SaveOrder_res.json()['data']['orderId']
    seller_AcceptOrder_res = AcceptOrder(surroundings, buyer_orderId, cookies=seller_login_res.cookies)
    my_logger.debug(f"确认订单的结果是：{seller_AcceptOrder_res.json()}")

    # 发货
    buyer_userId = seller_login_res.json()['userId']
    seller_ship_res = ship(surroundings, buyer_orderId, payType, buyer_userId, cookies=seller_login_res.cookies)
    my_logger.debug(f'卖家发货的结果是：{seller_ship_res.json()}')

    # 确认收货
    sellerUserId = seller_login_res.json()['userId']
    buyer_suer_res = suer(surroundings, buyer_orderId, payType, sellerUserId, payPassword,
                          cookies=buyer_login_res.cookies)
    my_logger.debug(f'确认收货的结果是：{buyer_suer_res.json()}')

    return buyer_orderNum


if __name__ == '__main__':
    # bug_entity_goods("test", 13724765586,17777777781, "一天两件商超商品", 3,"gQyzNznHAvc=")
    bug_entity_goods("test", 13724765586, 17777777781, "两天一件商超商品", 3, "gQyzNznHAvc=")
