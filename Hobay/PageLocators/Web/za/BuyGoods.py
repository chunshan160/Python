#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/3 16:05
#@Author :春衫
#@File :BuyGoods.py

from selenium.webdriver.common.by import By

xuliehao=(By.XPATH,'//div[@class="qr"]//div')

frist_order=(By.XPATH,'(//div[@class="order-shop"])[1]')

click_xuliehao=(By.XPATH,'//input[@type="text"]')
click_queding=(By.XPATH,'//button[contains(text(),"确定")]')
click_queding2=(By.XPATH,'//li[contains(text(),"确定")]')

qianyue=(By.XPATH,'//button[text()="确认签约"]')