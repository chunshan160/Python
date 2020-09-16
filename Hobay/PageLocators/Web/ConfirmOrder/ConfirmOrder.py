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
select_address = (By.CLASS_NAME, "address")
# 新建地址
new_address = (By.XPATH, '//div[contains(text(),"新建地址")]')
#名字
name = (By.XPATH,'//input[@placeholder="请输入姓名"]')
#手机号
phone=(By.XPATH,'//input[@placeholder="请输入手机号码"]')
#地址
address=(By.XPATH,'//input[@placeholder="请选择地址"]')
#省
province=(By.XPATH,'//div[contains(text(),"山西省")]')
#市
city=(By.XPATH,'//div[contains(text(),"太原市")]')
#区
area=(By.XPATH,'//div[contains(text(),"小店区")]')
#详细地址
detailed_address=(By.XPATH,'//input[@placeholder="请输入详细地址，如街道、门牌号等"]')
# 默认地址
default_address = (By.CLASS_NAME, "van-checkbox")
# 保存
save = (By.CLASS_NAME, "save-btn")

#选择第一个地址
choose_first_address=(By.CLASS_NAME,"address-item")

# 管理地址
manage_address = (By.XPATH, '//div[contains(text(),"管理地址")]')

# 优惠券
coupon = (By.XPATH, '//div[contains(text(),"优惠券")]/following-sibling::div')
# 买家留言
buyer_message = (By.XPATH,'//input[@placeholder="选填，输入想对卖家说的话"]')
# 提交订单
submit_order = (By.XPATH,'//button[contains(text(),"提交订单")]')
