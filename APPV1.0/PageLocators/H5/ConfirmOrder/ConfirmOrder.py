#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 17:59
# @Author :春衫
# @File :ConfirmOrder_Handle.py

'''
确认订单页面
'''

# 选择收货地址
select_address = ("id", "com.ecloud.hobay:id/tv_select_address")
# 新建地址
new_address = ("id", "com.ecloud.hobay:id/tv_new_address")
# 管理地址
manage_address = ("id", "com.ecloud.hobay:id/tv_manage_address")
# 默认地址
default_address = ("id", "com.ecloud.hobay:id/tv_default")
# 优惠券
coupon = ("id", "com.ecloud.hobay:id/tv_coupon_number")
# 买家留言
buyer_message = ("id", "com.ecloud.hobay:id/et_message")
# 提交订单
submit_order = ("android_uiautomator",'new UiSelector().text("提交订单")')
