#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/15 12:37
#@Author :春衫
#@File :TouchAction.py

from appium.webdriver.common.touch_action import TouchAction

class Touch:

    def __init__(self,driver):
        self.driver=driver

    def Touch(self,x,y):
        TouchAction(self.driver).tap(x=x, y=y).perform()
