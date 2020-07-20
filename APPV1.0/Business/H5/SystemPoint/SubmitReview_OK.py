#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/13 13:53
#@Author :春衫
#@File :SubmitReviewOK_Page.py

import time
from Handle.H5.SystemPoint.SubmitReviewOK import SubmitReviewOKHandle

# 系统提示页面-商品审核中
class SubmitReviewOKBusiness:

    def __init__(self, driver):
        self.to_audit_ok = SubmitReviewOKHandle(driver)

    # 获取提示文字信息
    def get_text(self):
        time.sleep(2)
        text = self.to_audit_ok.get_text()
        if text == "商品审核中":
            return True
        else:
            return False

    #点击完成按钮
    def good_audit_btn(self):
        self.to_audit_ok.good_audit_btn()