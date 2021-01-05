#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/16 16:04
# @Author :春衫
# @File :RetrievePassword.py

from Web.Common.BasePage import BasePage


# 找回密码成功
class RetrievePassword(BasePage):

    # 找回密码成功
    def title_text(self, text=""):
        doc = text + "获取【title】文本-"
        return self.get_text(title, doc=doc)

    # 立即登录
    def login_now(self, text=""):
        doc = text + "点击【立即登录】按钮-"
        self.click_element(login_now, doc=doc)