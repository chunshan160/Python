#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 17:59
# @Author :春衫
# @File :ConfirmOrder_Handle.py

from selenium.webdriver.common.by import By
'''
确认订单页面
'''

# 选择收货地址
select_address = (By.ID, "com.ecloud.hobay:id/tv_select_address")
# 新建地址
new_address = (By.ID, "com.ecloud.hobay:id/tv_new_address")
#填写信息
address = {"MI 8": {"输入收货人姓名": (868, 261), "输入收货人手机号码": (837, 402), "选择所在地区": (887, 527),
                   "省": (106, 909), "市": (110, 1163), "区": (110, 1269), "输入地址": (675, 640), "设为默认地址": (76, 769), }}
# 保存
save = (By.ID, "android:id/content")
#选择第一个地址
choose_first_address=(By.CLASS_NAME,"android.widget.RelativeLayout")

# 管理地址
manage_address = (By.ID, "com.ecloud.hobay:id/tv_manage_address")
# 默认地址
default_address = (By.ID, "com.ecloud.hobay:id/tv_default")
# 优惠券
coupon = (By.ID, "com.ecloud.hobay:id/tv_coupon_number")
# 买家留言
buyer_message = (By.ID, "com.ecloud.hobay:id/et_message")
# 提交订单
submit_order = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("提交订单")')
