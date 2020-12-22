#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/20 15:11
#@Author :春衫
#@File :MyIndex.py

from Web.PageLocators.Web.MyIndex import MyIndex
from Common.BasePage import BasePage


class MyIndexPage(BasePage):

    def click_setting(self,text):
        doc=text+"点击【设置】按钮-"
        self.click_element(MyIndex.setting, doc=doc)