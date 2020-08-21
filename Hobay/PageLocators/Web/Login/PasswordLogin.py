#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 17:49
#@Author :春衫
#@File :PasswordLogin.py

from selenium.webdriver.common.by import By

# 输入密码
enter_password = (By.XPATH, '//input[@placeholder="请输入密码"]')
# 显示密码
display_password = (By.XPATH, '//div[@class="slot-right-icon"]')
# 登录
login = (By.XPATH, '//button[contains(text(),"登 录")]')
# 验证码登录
code_login = (By.XPATH, '//div[text()="验证码登录"]')
# 找回密码
retrieve_password = (By.XPATH, '//div[contains(text(),"找回密码")]')