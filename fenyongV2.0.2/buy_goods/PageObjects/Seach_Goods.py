#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/7 15:13
#@Author :春衫
#@File :Seach_Goods.py

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from buy_goods.PageLocators.Index import Home
from selenium.webdriver.common.keys import Keys

class Seach_Goods:
    def seach_goods(self,driver,goodsname):
        driver.find_element(*Home.search).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Home.input))).send_keys(goodsname)
        time.sleep(2)
        driver.find_element(*Home.input).send_keys(Keys.ENTER)
        time.sleep(3)
        # 点击【商品】
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Home.real_goods))).click()
        time.sleep(4)