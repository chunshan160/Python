#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/13 13:42
#@Author :春衫
#@File :SubmitReviewOK_Page.py

from Common.BasePage import BasePage


# 提交审核成功
class SubmitReviewOKPage(BasePage):

    def title(self):
        return self.get_text(title)

    def prompt(self):
        return self.get_text(prompt)

    def consummation(self):
        self.click_element(consummation)