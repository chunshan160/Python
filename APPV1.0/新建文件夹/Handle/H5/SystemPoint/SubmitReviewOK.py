#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/13 13:53
#@Author :春衫
#@File :SubmitReviewOK_Page.py
import time

from PageObjects.H5.SystemPoint.SubmitReviewOK import SubmitReviewOKPage


# 系统提示页面-商品审核中
class SubmitReviewOKHandle:

    def __init__(self, driver):
        self.to_audit_ok = SubmitReviewOKPage(driver)

    # 获取提示文字信息
    def get_text(self):
        try:
            text = self.to_audit_ok.good_audit_text().text
            return text
        except:
            print("没有找到这个元素")

    #点击完成按钮
    def good_audit_btn(self):
        self.to_audit_ok.good_audit_btn().click()