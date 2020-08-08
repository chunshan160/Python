#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/13 13:42
# @Author :春衫
# @File :SubmitReviewOK_Page.py

from appium.webdriver.common.mobileby import MobileBy

'''
发布商品-立即上架-系统提示
'''

# 商品审核中文本
good_audit_text = (MobileBy.ID, "com.ecloud.hobay:id/tv_tips")
# 审核已提交，工作人员正在为您审核
good_audit_tip = (MobileBy.ID, "com.ecloud.hobay:id/tv_desc")
# 完成
good_audit_btn = (MobileBy.ID, "com.ecloud.hobay:id/btn_look_product")
