#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/20 13:59
# @Author :春衫
# @File :Login_Business.py

from Common.TouchAction import Touch


class LoginPage:

    def __init__(self, driver, local):
        self.driver = driver
        self.local = local

    # 点击手机号输入框
    def click_phone_box(self):
        Touch(self.driver).tap(self.local["输入手机号"][0], self.local["输入手机号"][1])

    # 输入手机号
    def nine_keys_key_board(self, number):

        for i in number:
            if i == "1":
                self.driver.keyevent(8)
            elif i == "2":
                self.driver.keyevent(9)
            elif i == "3":
                self.driver.keyevent(10)
            elif i == "4":
                self.driver.keyevent(11)
            elif i == "5":
                self.driver.keyevent(12)
            elif i == "6":
                self.driver.keyevent(13)
            elif i == "7":
                self.driver.keyevent(14)
            elif i == "8":
                self.driver.keyevent(15)
            elif i == "9":
                self.driver.keyevent(16)
            elif i == "0":
                self.driver.keyevent(7)

    # 点击下一步
    def click_next(self):
        Touch(self.driver).tap(self.local["下一步"][0], self.local["下一步"][1])

    # 切换验证码登录
    def switch_code(self):
        Touch(self.driver).tap(self.local["验证码登录"][0], self.local["验证码登录"][1])

    # 点击验证码输入框
    def click_code_box(self):
        Touch(self.driver).tap(self.local["输入验证码"][0], self.local["输入验证码"][1])

    # 点击密码输入框
    def click_pwd_box(self):
        Touch(self.driver).tap(self.local["输入密码"][0], self.local["输入密码"][1])

    # 输入密码
    def send_pwd(self):
        # 输入密码 默认qaz123
        self.driver.keyevent(45)
        self.driver.keyevent(29)
        self.driver.keyevent(54)
        self.driver.keyevent(8)
        self.driver.keyevent(9)
        self.driver.keyevent(10)

    # 点击登录
    def click_login(self):
        Touch(self.driver).tap(self.local["登录"][0], self.local["登录"][1])

    #登录
    def main(self, phone,pwd=None, code="666666"):
        # 点击输入框
        self.click_phone_box()
        # 输入手机号
        self.nine_keys_key_board(phone)
        # 点击下一步
        self.click_next()
        # 不输入密码，就用通用验证码登录
        if pwd == None:
            # 切换验证码登录
            self.switch_code()
            # 点击输入框
            self.click_code_box()
            # 默认666666  传值的话会变
            self.nine_keys_key_board(code)
        # 用密码登录
        else:
            # 点击输入框
            self.click_pwd_box()
            # 输入密码 默认qaz123
            self.send_pwd()
        # 点击登录
        self.click_login()
