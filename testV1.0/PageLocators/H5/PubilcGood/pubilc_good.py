#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:00
#@Author :春衫
#@File :pubilc_good.py

from selenium.webdriver.common.by import By

'''
发布商品
'''

# 首页点击发布商品
publish_good=(By.XPATH,'//i[@class="cart-icon"]//..')
# 点击发布实物商品
entity_good = (By.XPATH, '//span[@class="btn material-btn"]')
# 点击发布本地生活
coupon_good = (By.XPATH, '//span[@class="btn business-btn"]')
# 点击发布商企服务
services_good = (By.XPATH, '//span[@class="btn service-btn"]')