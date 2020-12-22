#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/17 15:52
#@Author :春衫
#@File :SearchGood_Business.py

from selenium.webdriver.common.by import By

#搜索框-输入
send_search=(By.XPATH,'//input[@placeholder="输入关键字"]')
#商品tap
good_tap=(By.XPATH,'//span[text()="商品"]/..')
#店铺tap
shop_tap=(By.XPATH,'//span[text()="店铺"]/..')
#综合
Comprehensive=(By.XPATH,'//div[text()="综合"]')
#全新
new=(By.XPATH,'//div[text()="全新"]')
#人气
hot=(By.XPATH,'//div[text()="人气"]')
#价格
price=(By.XPATH,'//div[text()="价格"]')
#筛选
filter=(By.XPATH,'//div[@class="tab-pro"]/div[text()="筛选"]')
#商品
good=(By.XPATH,'//li[@class="product-item"]')
#进店
go_shop=(By.CLASS_NAME,"look-btn")
#搜索-店铺-商品
shop_good=(By.XPATH,'//ul[@class="pro-list clearfix"]/li')