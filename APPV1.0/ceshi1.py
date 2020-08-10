#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/5 21:46
# @Author :春衫
# @File :ceshi1.py


from appium.webdriver.common.mobileby import MobileBy

a=(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")')
# 匹配文本来处理表达式
def match_text(locator,text):
    new_locator=(locator[0],locator[1].format(text))
    return new_locator

b=match_text(a,"lala")
print(b)