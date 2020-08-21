#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/5 17:34
# @Author :春衫
# @File :PubilcGoodCommon.py

from selenium.webdriver.common.by import By

'''
底部的五个选项栏
'''
# 首页
index = (By.ID, "com.ecloud.hobay:id/rb_home")
# 易货信用
credit_good = (By.ID, "com.ecloud.hobay:id/rb_credit_good")
# 焕焕商机
business = (By.ID, "com.ecloud.hobay:id/rb_business")
# 发布商品
publish_good = (By.ID, "com.ecloud.hobay:id/rb_helpping_me")
# 我的
my_index = (By.ID, "com.ecloud.hobay:id/rb_me")

# 权限-始终允许
always_allowed = (By.XPATH, "//*[@text='始终允许']")
