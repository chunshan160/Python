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
        doc="选择收货地址-按钮"
        self.get_element(CO.select_address,doc =doc).click()

    # 管理地址
    def manage_address(self):
        doc = "收货地址-底部-管理地址-按钮"
        self.get_element(CO.manage_address, doc=doc).click()

    # 新建地址
    def new_address(self):
        doc = "收货地址-底部-新建地址-按钮"
        self.get_element(CO.new_address,doc =doc).click()

    # 填写收货地址信息
    def input_address(self, model="MI 8", default=True):
        doc = "新建地址-流程"
        tap = CO.address[model]
        # 点击输入收货人姓名
        self.touch(tap["输入收货人姓名"][0], tap["输入收货人姓名"][1])
        # 输入收货人姓名
        self.driver.keyevent(45)
        # 点击输入手机号
        self.touch(tap["输入收货人手机号码"][0], tap["输入收货人手机号码"][1])
        # 输入手机号
        self.send_phone_number(11111111111,doc =doc)
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
        self.get_element(CO.save,doc =doc)
        time.sleep(0.5)

    # 选择收货地址
    def choose_address(self):
        doc = "选择第一个为收货地址-动作"
        self.get_element(CO.choose_first_address,doc =doc).click()



    # 默认地址
    def default_address(self):
        doc = "是否存在默认地址-检查"
        try:
            return self.get_element(CO.default_address,doc =doc).text
        except:
            return None

    # 优惠券
    def coupon(self):
        doc = "优惠券-选项"
        self.get_element(CO.coupon,doc =doc).click()

    # 买家留言
    def buyer_message(self):
        doc = "买家留言-选项"
        self.get_element(CO.buyer_message,doc =doc).click()

    # 提交订单
    def submit_order(self):
        doc = "确认订单-底部-提交订单-按钮"
        self.get_element(CO.submit_order,doc =doc).click()

    # 提交订单
    def submit_order_now(self):
        doc = "收货地址-选项"
        text = self.get_element(CO.select_address,doc =doc).text
        if text == "请选择收货地址":
            self.select_address()
            if self.default_address()==None:
                self.new_address()
                self.input_address()
            self.choose_address()
        self.submit_order()
