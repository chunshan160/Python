#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 17:59
# @Author :春衫
# @File :ConfirmOrder_Handle.py

import time
from PageObjects.H5.ConfirmOrder.ConfirmOrder_Page import ConfirmOrderPage

class ConfirmOrderHandle:

    def __init__(self, driver):
        self.confirm_order_P = ConfirmOrderPage(driver)

    # 选择收货地址
    def click_select_address(self):
        time.sleep(0.5)
        self.confirm_order_P.get_select_address_element().click()

    # 新建地址
    def click_new_address(self):
        time.sleep(0.5)
        self.confirm_order_P.get_new_address_element().click()

    # 管理地址
    def click_manage_address(self):
        time.sleep(0.5)
        self.confirm_order_P.get_manage_address_element().click()

    # 默认地址
    def click_default_address(self):
        time.sleep(0.5)
        self.confirm_order_P.get_default_address_element().click()

    # 优惠券
    def click_coupon(self):
        time.sleep(0.5)
        self.confirm_order_P.get_coupon_element().click()

    # 买家留言
    def click_buyer_message(self):
        time.sleep(0.5)
        self.confirm_order_P.get_buyer_message_element().click()

    # 提交订单
    def click_submit_order(self):
        time.sleep(1)
        self.confirm_order_P.get_submit_order_element().click()
