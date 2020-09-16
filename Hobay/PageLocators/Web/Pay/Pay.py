#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/17 18:08
# @Author :春衫
# @File :Pay_Business.py

from selenium.webdriver.common.by import By

'''
支付
'''

# 更换支付方式
replace_pay = (By.XPATH,'//span[contains(text(),"更换支付方式")]')
# 易贝
cbp_pay = (By.XPATH,'(//div[@class="pay-bg"]//ul//li)[1]')
# 易贝券
voucher_pay = (By.XPATH,'(//div[@class="pay-bg"]//ul//li)[2]')
# 抵工资
wages_pay = (By.XPATH,'(//div[@class="pay-bg"]//ul//li)[3]')
#家人购
family_pay=(By.XPATH,'(//div[@class="pay-bg"]//ul//li)[4]')
# 现金
cash_pay =  (By.XPATH,'(//div[@class="pay-bg"]//ul//li)[5]')
# 微信
wechat_pay = (By.XPATH,'(//div[@class="pay-bg"]//ul//li)[6]')
# 确认支付
confirm_pay = (By.XPATH,'//a[contains(text(),"确认支付")]')

#支付密码
pay_1 = (By.XPATH,'//i[contains(text(),"1")]')
pay_2 = (By.XPATH, '//i[contains(text(),"2")]')
pay_3 = (By.XPATH, '//i[contains(text(),"3")]')
pay_4 = (By.XPATH, '//i[contains(text(),"4")]')
pay_5 = (By.XPATH, '//i[contains(text(),"5")]')
pay_6 = (By.XPATH, '//i[contains(text(),"6")]')

