#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/20 13:59
# @Author :春衫
# @File :Login_Business.py
import time

from Common.BasePage import BasePage
from PageLocators.H5.Login.Login import local

class LoginPage(BasePage):

    def __init__(self, driver,model="MI 8"):
        self.driver = driver
        self.local=local[model]

    # 点击手机号输入框
    def click_phone_box(self):
        self.touch(self.local["输入手机号"][0], self.local["输入手机号"][1])

    # 点击下一步
    def click_next(self):
        self.touch(self.local["下一步"][0], self.local["下一步"][1])

    # 切换验证码登录
    def switch_code(self):
        self.touch(self.local["验证码登录"][0], self.local["验证码登录"][1])

    # 点击验证码输入框
    def click_code_box(self):
        self.touch(self.local["输入验证码"][0], self.local["输入验证码"][1])

    # 点击密码输入框
    def click_pwd_box(self):
        self.touch(self.local["输入密码"][0], self.local["输入密码"][1])

    # 点击登录
    def click_login(self):
        self.touch(self.local["登录"][0], self.local["登录"][1])

    #登录
    def login(self, phone,pwd=None, code="666666"):
        # 点击输入框
        time.sleep(1)
        self.click_phone_box()
        # 输入手机号
        time.sleep(1)
        self.send_phone_number(phone)
        # 点击下一步
        time.sleep(1)
        self.click_next()
        # 不输入密码，就用通用验证码登录
        if pwd == None:
            # 切换验证码登录
            time.sleep(1)
            self.switch_code()
            # 点击输入框
            time.sleep(1)
            self.click_code_box()
            # 默认666666  传值的话会变
            time.sleep(1)
            self.send_phone_number(code)
        # 用密码登录
        else:
            # 点击输入框
            time.sleep(1)
            self.click_pwd_box()
            # 输入密码 默认qaz123
            time.sleep(1)
            self.send_pwd()
        # 点击登录
        time.sleep(1)
        self.click_login()
