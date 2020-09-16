#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/17 16:17
#@Author :春衫
#@File :GoodDetail_Business.py

from selenium.webdriver.common.by import By

#顶部商品
top_good=(By.XPATH,'//span[text()="商品"]')
#顶部详情
top_detail=(By.XPATH,'//span[text()="详情"]')
#顶部评价
top_evaluation=(By.XPATH,'//span[text()="评价"]')
#店铺
shop=(By.XPATH,'//span[text()="店铺"]/..')
#收藏
collection=(By.XPATH,'//span[text()="收藏"]/..')
#咨询
chat=(By.XPATH,'//span[text()="咨询"]/..')
#加入购物车
add_car=(By.CLASS_NAME,"btn join")
#立即购买
buy_now=(By.CLASS_NAME,"r-server")
#-
less=(By.XPATH,'//span[contains(text(),"-")]')
#购买数量
add_amount=(By.XPATH,'//input[@type="number"]')
#+
add=(By.XPATH,'//span[contains(text(),"+")]')
#确定
confirm=(By.CLASS_NAME, "btn buy")