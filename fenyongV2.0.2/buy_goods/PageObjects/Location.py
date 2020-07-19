#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/7 16:30
#@Author :春衫
#@File :Location.py
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from buy_goods.PageLocators.Index import Home


class Location:

    def location(self,driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Home.location))).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Home.all_city))).click()
        time.sleep(3)