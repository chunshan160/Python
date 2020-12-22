#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/7 13:01
# @Author :春衫
# @File :Check.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Web.PageLocators.ERP.Check import Check as CK
from selenium.webdriver.common.action_chains import ActionChains
import time


class Check:
    def __init__(self, driver):
        self.driver = driver

    def Check_Pass(self):
        # 滚动至元素【审核通过】可见
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.driver.find_element(*CK.check_pass)).click(
            self.driver.find_element(*CK.check_pass)).perform()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((CK.determine_1))).click()

    def Check_Refuse(self, refuse_reason):
        # 滚动至元素【审核拒绝】可见
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.driver.find_element(*CK.check_refuse)).click(
            self.driver.find_element(*CK.check_refuse)).perform()
        # 拒绝原因
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((CK.refuse_reason))).send_keys(
            refuse_reason)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((CK.determine_2))).click()
