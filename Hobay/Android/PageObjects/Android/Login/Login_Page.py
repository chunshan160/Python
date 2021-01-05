#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/20 13:59
# @Author :春衫
# @File :Login_Business.py

import time
from Web.Common.BasePage import BasePage
from Android.PageLocators.Android import local


class LoginPage(BasePage):

    def __init__(self, driver, model="MI 8"):
        super().__init__(driver)
        self.local = local[model]

    # 点击手机号输入框
    def click_phone_box(self, text=""):
        doc = text + "点击【手机号】输入框-"
        self.touch(self.local["输入手机号"][0], self.local["输入手机号"][1], doc=doc)

    # 点击下一步
    def click_next(self, text=""):
        doc = text + "点击【下一步】按钮-"
        self.touch(self.local["下一步"][0], self.local["下一步"][1], doc=doc)

    # 切换验证码登录
    def switch_code(self, text=""):
        doc = text + "点击切换【验证码登录】按钮-"
        self.touch(self.local["验证码登录"][0], self.local["验证码登录"][1], doc=doc)

    # 点击验证码输入框
    def click_code_box(self, text=""):
        doc = text + "点击【验证码】输入框-"
        self.touch(self.local["输入验证码"][0], self.local["输入验证码"][1], doc=doc)

    # 点击密码输入框
    def click_pwd_box(self, text=""):
        doc = text + "点击【密码】输入框-"
        self.touch(self.local["输入密码"][0], self.local["输入密码"][1], doc=doc)

    # 点击登录
    def click_login(self, text=""):
        doc = text + "点击【登录】按钮-"
        self.touch(self.local["登录"][0], self.local["登录"][1], doc=doc)

    # 登录
    def login(self, phone, pwd=None, code="666666", text=""):
        # 点击输入框
        time.sleep(1)
        self.click_phone_box(text=text)
        # 输入手机号
        time.sleep(1)
        self.send_phone_number(phone, text=text)
        # 点击下一步
        time.sleep(1)
        self.click_next(text=text)
        time.sleep(1)
        # 不输入密码，就用通用验证码登录
        if pwd == None:
            # 切换验证码登录
            time.sleep(1)
            self.switch_code(text=text)
            # 点击输入框
            time.sleep(1)
            self.click_code_box(text=text)
            # 默认666666  传值的话会变
            time.sleep(1)
            self.send_phone_number(code, text=text)
        # 用密码登录
        else:
            # 点击输入框
            time.sleep(1)
            self.click_pwd_box(text=text)
            # 输入密码 默认qaz123
            time.sleep(1)
            self.send_pwd(text=text)
        # 点击登录
        time.sleep(1)
        self.click_login(text=text)


if __name__ == '__main__':
    pass
