#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 17:59
# @Author :春衫
# @File :ConfirmOrder_Handle.py

import time
from PageLocators.H5.ConfirmOrder import ConfirmOrder as CO
from Common.BasePage import BasePage


class ConfirmOrderPage(BasePage):



    # 选择收货地址
    def select_address(self):
        self.get_element(CO.select_address).click()

    # 新建地址
    def new_address(self):
        self.get_element(CO.new_address).click()


    # 填写收货地址信息
    def input_address(self, model="MI 8", default=True):
        tap = CO.address[model]
        # 点击输入收货人姓名
        self.touch(tap["输入收货人姓名"][0], tap["输入收货人姓名"][1])
        # 输入收货人姓名
        self.driver.keyevent(45)
        # 点击输入手机号
        self.touch(tap["输入收货人手机号码"][0], tap["输入收货人手机号码"][1])
        # 输入手机号
        self.send_phone_number(11111111111)
        # 点击所在地区
        self.touch(tap["选择所在地区"][0], tap["选择所在地区"][1])
        time.sleep(0.5)
        # 省
        self.touch(tap["省"][0], tap["省"][1])
        # 市
        self.touch(tap["市"][0], tap["市"][1])
        # 区
        self.touch(tap["区"][0], tap["区"][1])
        time.sleep(0.5)
        # 点击详细地址
        self.touch(tap["输入地址"][0], tap["输入地址"][1])
        # 输入详细地址
        self.driver.keyevent(45)
        if default is True:
            # 设为默认地址
            self.touch(tap["设为默认地址"][0], tap["设为默认地址"][1])
        # 点击保存
        self.get_element(CO.save)
        time.sleep(0.5)

    # 选择收货地址
    def choose_address(self):
        self.get_element(CO.choose_first_address).click()

    # 管理地址
    def manage_address(self):
        self.get_element(CO.manage_address).click()

    # 默认地址
    def default_address(self):
        try:
            return self.get_element(CO.default_address).text
        except:
            return None

    # 优惠券
    def coupon(self):
        self.get_element(CO.coupon).click()

    # 买家留言
    def buyer_message(self):
        self.get_element(CO.buyer_message).click()

    # 提交订单
    def submit_order(self):
        self.get_element(CO.submit_order).click()

    # 提交订单
    def submit_order_now(self):
        text = self.get_element(CO.select_address).text
        if text == "请选择收货地址":
            self.select_address()
            if self.default_address()==None:
                self.new_address()
                self.input_address()
            self.choose_address()
        self.submit_order()
