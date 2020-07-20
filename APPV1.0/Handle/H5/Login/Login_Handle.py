#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/20 13:59
# @Author :春衫
# @File :Login_Business.py
import time

from PageObjects.H5.Login.Login import LoginPage


class LoginHandle:

    def __init__(self, driver, local):
        self.driver = driver
        self.local = local
        self.LP = LoginPage(self.driver, self.local)

    # 点击手机号输入框
    def click_phone_box(self):
        time.sleep(1)
        self.LP.click_phone_box()

    # 输入手机号
    def nine_keys_key_board(self, number):
        time.sleep(1)
        self.LP.nine_keys_key_board(number)

    # 点击下一步
    def click_next(self):
        time.sleep(1)
        self.LP.click_next()

    # 切换验证码登录
    def switch_code(self):
        time.sleep(1)
        self.LP.switch_code()

    # 点击验证码输入框
    def click_code_box(self):
        time.sleep(1)
        self.LP.click_code_box()

    # 点击密码输入框
    def click_pwd_box(self):
        time.sleep(1)
        self.LP.click_pwd_box()

    # 输入密码
    def send_pwd(self):
        time.sleep(1)
        self.LP.send_pwd()

    # 点击登录
    def click_login(self):
        time.sleep(1)
        self.LP.click_login()
