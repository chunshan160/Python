#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/7 17:07
#@Author :春衫
#@File :Untie_Partner.py
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from buy_goods.PageLocators.MyIndex import MyIndex


class UntiePartner:
    def untie_partner(self,driver,surroundings):
        
        if surroundings == "test":
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MyIndex.delete1))).click()
        elif surroundings == "mtest":
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MyIndex.delete2))).click()
        elif surroundings == "dev1":
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MyIndex.delete3))).click()
        time.sleep(2)
        driver.find_element(*MyIndex.queren).click()
        time.sleep(5)