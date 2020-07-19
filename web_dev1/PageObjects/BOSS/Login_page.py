#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2019/12/31 17:18
#@Author :春衫
#@File :Login_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_dev1.PageLocators.BOSS.Login import LoginPage as LP

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # 正常登录操作
    def login(self, username, password):
        # 输入手机号
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LP.name))).send_keys(username)
        # 输入密码
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LP.pwd))).send_keys(password)
        # 点击登录
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LP.login_but))).click()