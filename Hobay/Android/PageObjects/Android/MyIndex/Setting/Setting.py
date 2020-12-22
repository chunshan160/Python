#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/5 18:03
# @Author :春衫
# @File :Setting.py

import time
from Android.PageLocators.Android.MyIndex.Setting import Setting
from Common.BasePage import BasePage


class SettingPage(BasePage):

    def exit(self,text):
        doc=text+"点击【退出】按钮-"
        time.sleep(0.5)
        self.click_element(Setting.exit, doc=doc)
