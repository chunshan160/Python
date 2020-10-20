#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/5/26 11:29
#@Author :春衫
#@File :ReturnTxt.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.Web.za import BuyGoods as BG

class ReturnTxt:

    def __init__(self, driver):
        self.driver = driver

    def xuliehao_txt(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.xuliehao)))
        a=self.driver.find_element(*BG.xuliehao).get_attribute("title")
        b=a[:-6]
        xuliehao_txt =eval(b)['qrCode']
        return xuliehao_txt