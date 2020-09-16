#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/13 13:42
# @Author :春衫
# @File :SubmitReviewOK_Page.py

from PageLocators.Web.SystemPoint.PublishGoodOK import *
from Common.BasePage import BasePage


# 提交审核成功
class SubmitReviewOKPage(BasePage):

    # 获取【title】文本
    def title(self, text=""):
        doc = text + "获取【title】文本-"
        return self.get_text(title, doc=doc)

    # 获取提示文本
    def prompt(self, text=""):
        doc = text + "获取【提示】文本-"
        return self.get_text(prompt, doc=doc)

    # 点击完成
    def consummation(self, text=""):
        doc = text + "点击【完成】按钮-"
        self.click_element(consummation, doc=doc)
