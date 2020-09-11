#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/5 17:34
# @Author :春衫
# @File :PubilcGoodCommon.py

from selenium.webdriver.common.by import By

'''
底部的五个选项栏
'''
# 首页
index = (By.CLASS_NAME, "my-icon")
# 易货信用
credit_good = (By.CLASS_NAME, "credit-icon")
# 焕焕商机
business = (By.CLASS_NAME, "huanhuan-icon")
# 发布商品
publish_good = (By.CLASS_NAME, "cart-icon")
# 我的
my_index = (By.CLASS_NAME, "my-icon")
