#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 17:59
# @Author :春衫
# @File :ConfirmOrder_Handle.py

from PageLocators.H5.ConfirmOrder import ConfirmOrder as CO
from Common.find_element import FindElement

class ConfirmOrderPage:

    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 选择收货地址
    def get_select_address_element(self):
        return self.fd.find_element(CO.select_address)

    # 新建地址
    def get_new_address_element(self):
        return self.fd.find_element(CO.new_address)

    # 管理地址
    def get_manage_address_element(self):
        return self.fd.find_element(CO.manage_address)

    # 默认地址
    def get_default_address_element(self):
        return self.fd.find_element(CO.default_address)

    # 优惠券
    def get_coupon_element(self):
        return self.fd.find_element(CO.coupon)

    # 买家留言
    def get_buyer_message_element(self):
        return self.fd.find_element(CO.buyer_message)

    # 提交订单
    def get_submit_order_element(self):
        return self.fd.find_element(CO.submit_order)
