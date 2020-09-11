#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/13 13:42
#@Author :春衫
#@File :ToAuditOk_Page.py


from PageLocators.Web.za import toAuditOk
from Common.BasePage import BasePage


# 发布实物商品
class ToAuditOkPage(BasePage):

    # 点击完成按钮
    def good_audit_btn(self, text=""):
        doc = text + "点击【完成】按钮-"
        self.click_element(toAuditOk.good_audit_btn, doc=doc)