#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 18:08
# @Author :春衫
# @File :Pay_Business.py

from appium.webdriver.common.mobileby import MobileBy

'''
支付
'''

# 更换支付方式
replace_pay = (MobileBy.ID, "com.ecloud.hobay:id/tv_replace_pay")
# 易贝
cbp_pay = (MobileBy.ID, "com.ecloud.hobay:id/view_cbp")
# 易贝券
voucher_pay = (MobileBy.ID, "com.ecloud.hobay:id/view_voucher")
# 抵工资
wages_pay = (MobileBy.ID, "com.ecloud.hobay:id/view_wages")
#家人购
family_pay=(MobileBy.CLASS_NAME,"android.view.ViewGroup")
# 现金
cash_pay = (MobileBy.ID, "com.ecloud.hobay:id/tv_cash")
# 微信
wechat_pay = (MobileBy.ID, "com.ecloud.hobay:id/tv_wechat")
# 支付宝
alibaba_pay = (MobileBy.ID, "com.ecloud.hobay:id/tv_alibaba")
# 确认支付
confirm_pay = (MobileBy.ID, "com.ecloud.hobay:id/btn_pay")
