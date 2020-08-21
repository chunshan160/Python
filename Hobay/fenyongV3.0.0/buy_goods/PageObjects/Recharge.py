#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/7 15:03
#@Author :春衫
#@File :Recharge_requests.py

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from buy_goods.PageLocators.MyIndex import MyIndex

class Recharge:
    def recharge(self,driver):

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MyIndex.serviceRecharge))).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MyIndex.recharge_amount))).click()
        time.sleep(2)
        driver.find_element(*MyIndex.input_amount).send_keys(100)
        time.sleep(2)
        driver.find_element(*MyIndex.queren).click()
        time.sleep(5)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MyIndex.rechare_now))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MyIndex.querenzhifu))).click()
        time.sleep(2)