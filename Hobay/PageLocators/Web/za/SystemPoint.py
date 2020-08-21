#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/3/18 14:01
#@Author :春衫
#@File :SystemPoint.py

from selenium.webdriver.common.by import By

class SystemPoint:
    #系统提示-支付成功
    pay_success=(By.XPATH,'//p[text()="支付成功"]')