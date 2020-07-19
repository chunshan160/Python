#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/31 14:38
# @Author :春衫
# @File :ERP.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_dev1.PageLocators.ERP.Check import Check as CK


class Check:
    def __init__(self, driver):
        self.driver = driver

    def Search_Pnone(self, phone):
        # 点击卖家手机搜索框，输入卖家手机
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((CK.search_phone))).send_keys(phone)
