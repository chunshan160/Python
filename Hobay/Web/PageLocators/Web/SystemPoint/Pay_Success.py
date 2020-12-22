#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/20 12:29
# @Author :春衫
# @File :Pay_Success.py

from selenium.webdriver.common.by import By

'''
支付成功-系统提示页面
'''

# 加入焕商
join = (By.CLASS_NAME, "join")
# 关闭弹窗
close_pop_ups = (By.XPATH, '//img[@src="/vuespa/static/img/parnter-close.a10995b.png"]')
# 支付成功
title = (By.CLASS_NAME, "success-text")
# 支付方式
pay_method = (By.XPATH, '//span[text()="支付方式"]/following-sibling::span')
# 支付金额
pay_money = (By.XPATH, '//span[text()="支付金额"]/following-sibling::span')
# 支付服务费
pay_service = (By.XPATH, '//span[text()="支付服务费"]/following-sibling::span')
# 查看订单
look_order = (By.CLASS_NAME, "button-div check")
# 返回首页
return_home = (By.CLASS_NAME, "button-div index")
