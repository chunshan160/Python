#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/21 14:44
# @Author :春衫
# @File :WebDriver.py

from selenium import webdriver
from Web.Common import yamlPath
from Web.Common.read_yaml import read_yaml

config = read_yaml(yamlPath)
surroundings = list(config.keys())[0]
browser = config[surroundings]['browser']

class BrowserEngine:

    def get_browser(self,options=None):
        if browser == 'Firefox':
            driver = webdriver.Firefox()
        elif browser == 'Chrome':
            driver = webdriver.Chrome(options=options)
        elif browser == 'IE':
            driver = webdriver.Ie()
        else:
            driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)

        return driver

if __name__ == '__main__':
    mobile_emulation = {'deviceName': 'iPhone X'}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver=BrowserEngine().get_browser(chrome_options)
    driver.get("http://m.test.hobay.com.cn/")