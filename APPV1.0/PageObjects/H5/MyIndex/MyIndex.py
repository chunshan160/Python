#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/20 15:11
#@Author :春衫
#@File :MyIndex.py

from PageLocators.H5.MyIndex import MyIndex
from Common.BasePage import BasePage


class MyIndexPage(BasePage):

    def click_setting(self):
        self.get_element(MyIndex.setting).click()