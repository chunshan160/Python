#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/20 12:29
# @Author :春衫
# @File :Pay_Success.py

from appium.webdriver.common.mobileby import MobileBy

'''
支付成功-系统提示页面
'''

# 加入焕商
join = (MobileBy.ID, "com.ecloud.hobay:id/tv_join")
# 关闭弹窗
close_pop_ups = (MobileBy.ID, "com.ecloud.hobay:id/iv_delete")
# 支付成功
title = (MobileBy.ID, "com.ecloud.hobay:id/title")
# 支付方式
pay_method = (MobileBy.ID, "com.ecloud.hobay:id/tv_pay_method")
# 支付金额
pay_money = (MobileBy.ID, "com.ecloud.hobay:id/tv_pay_money")
# 支付服务费
pay_service = (MobileBy.ID, "com.ecloud.hobay:id/tv_pay_service")
# 查看订单
look_order = (MobileBy.ID, "com.ecloud.hobay:id/btn_look_order")
# 返回首页
return_home = (MobileBy.ID, "com.ecloud.hobay:id/return_home")
