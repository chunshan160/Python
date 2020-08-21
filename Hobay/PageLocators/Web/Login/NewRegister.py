#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 17:48
#@Author :春衫
#@File :NewRegister.py

from selenium.webdriver.common.by import By

# 输入验证码
enter_code = (By.XPATH, '//input[@placeholder="请输入验证码"]')
# 获取验证码
obtain_code = (By.XPATH, '//button[contains(text(),"获取验证码")]')
# 下一步
next = (By.XPATH, '//button[text()="下 一 步"]')
# 已有账号
have_account = (By.XPATH, '//div[contains(text(),"已有账号")]')