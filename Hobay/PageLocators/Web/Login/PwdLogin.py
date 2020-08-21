#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 17:48
#@Author :春衫
#@File :PwdLogin.py

from selenium.webdriver.common.by import By

# 输入手机号
name = (By.XPATH, '//input[@type="number"]')
# 下一步
next = (By.XPATH, '//button[text()="下 一 步"]')
# 错误提示
error_toast = (By.XPATH, '//div[@class="van-toast__text"]')
# 立即注册
register = (By.XPATH, '//span[contains(text(),"立即注册")]//parent::button')
# 取消
cancel = (By.XPATH, '//span[contains(text(),"取消")]//parent::button')