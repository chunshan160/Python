#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/16 16:01
# @Author :春衫
# @File :RegisterSuccess.py


from Common.BasePage import BasePage
from PageLocators.Web.SystemPoint.RegisterSuccess import *


# 注册成功
class RegisterSuccessPage(BasePage):

    # 注册成功
    def title_text(self, text=""):
        doc = text + "获取【title】文本-"
        return self.get_text(title, doc=doc)

    # 下载焕呗APP
    def download_app(self, text=""):
        doc = text + "点击【下载焕呗APP】按钮-"
        self.click_element(download_app, doc=doc)

    # 进入首页
    def go_to_index(self, text=""):
        doc = text + "点击【进入首页】按钮-"
        self.click_element(go_to_index, doc=doc)
