#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/13 13:42
#@Author :春衫
#@File :SubmitReviewOK_Page.py

from PageLocators.H5.SystemPoint.SubmitReviewOK import *
from Common.BasePage import BasePage


# 提交审核成功
class SubmitReviewOKPage(BasePage):

    def __init__(self, driver):
        self.driver=driver

    def good_audit_text(self):
        return self.get_element(good_audit_text).text

    def good_audit_tip(self):
        return self.get_element(good_audit_tip).text

    def good_audit_btn(self):
        self.get_element(good_audit_btn).click()