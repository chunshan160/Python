#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/13 13:42
# @Author :春衫
# @File :SubmitReviewOK_Page.py

from selenium.webdriver.common.by import By

'''
发布商品-立即上架-系统提示
'''

# 商品审核中文本
title = (By.XPATH, '//div[@class="audit-text"]')
# 审核已提交，工作人员正在为您审核
prompt = (By.XPATH, '//div[@class="audit-tip"]')
# 完成
consummation = (By.XPATH, '//div[@class="audit-btn"]')
