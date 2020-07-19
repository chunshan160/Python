#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/13 13:53
#@Author :春衫
#@File :ToAuditOk_Page.py
import time

from PageObjects.H5.ToAuditOk_Page import ToAuditOkPage


# 系统提示页面-商品审核中
class ToAuditOkHandle:

    def __init__(self, driver):
        self.to_audit_ok = ToAuditOkPage(driver)

    # 获取提示文字信息
    def get_text(self):
        try:
            text = self.to_audit_ok.good_audit_text().text
        except:
            text = None
        return text

    #点击完成按钮
    def good_audit_btn(self):
        self.to_audit_ok.good_audit_btn().click()