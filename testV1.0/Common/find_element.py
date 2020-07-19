#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/9 13:36
#@Author :春衫
#@File :find_element.py

import time
from selenium import webdriver
from Common.user_log import UserLog

class FindElement(object):
    def __init__(self,driver):
        self.driver=driver
        self.logger = UserLog()

    def find_element(self,key):
        by=key[0]
        value=key[1]
        self.logger.info("定位方式:" + by + "--->定位值:" + value)
        return self.driver.find_element(*key)


if __name__ == '__main__':
    from selenium.webdriver.common.by import By
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://m.test.hobay.com.cn/vuespa/index.html#/toAuditOk")
    A=FindElement(driver).find_element((By.XPATH, '//div[@class="audit-text"]')).text
    print(A)