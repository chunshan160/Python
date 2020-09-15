#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/3 16:05
#@Author :春衫
#@File :BuyGoods.py

from selenium.webdriver.common.by import By

class BuyGoods:
    #点击加入易购车
    cart = (By.XPATH,'//div[@class="joincart"]')
    #数量+
    add = (By.XPATH,'//span[contains(text(),"+")]')
    #确定
    determine = (By.XPATH, '//div[contains(text(),"确")]')
    #添加成功msg
    success_msg = (By.XPATH,'//div[contains(text(),"添加成功")]')
    #立即购买
    buy_now = (By.XPATH,'//div[@class="r-server"]')
    #提交订单
    submit_orders = (By.XPATH,'//button[contains(text(),"提交订单")]')
    #更换支付方式
    payment_method = (By.XPATH,'//span[contains(text(),"更换支付方式")]')
    #选择易贝券
    cbp_coupon = (By.XPATH,'//div[contains(text(),"易贝券")]//..//parent::div[@class="detaisl"]//parent::li')
    #选择抵工资
    digongzi = (By.XPATH,'//div[contains(text(),"抵工资")]//..//parent::div[@class="detaisl"]//parent::li')
    #选择家人购
    jiarengou = (By.XPATH,'//li[@class="li last-li"]')
    #选择现金账户
    xianjinzhanghu = (By.XPATH,'//div[contains(text(),"现金账户")]//..//parent::div[@class="detaisl"]//parent::li')
    #确认支付
    confirm_payment = ((By.XPATH,'//a[contains(text(),"确认支付")]'))
    #支付密码
    pay_1 = (By.XPATH,'//i[contains(text(),"1")]')
    pay_2 = (By.XPATH, '//i[contains(text(),"2")]')
    pay_3 = (By.XPATH, '//i[contains(text(),"3")]')
    pay_4 = (By.XPATH, '//i[contains(text(),"4")]')
    pay_5 = (By.XPATH, '//i[contains(text(),"5")]')
    pay_6 = (By.XPATH, '//i[contains(text(),"6")]')
    #支付成功
    pay_success = (By.XPATH,'//p[contains(text(),"支付成功")]')
    #返回首页
    Back_to_Home = (By.XPATH,'//div[@class="button-div index"]')

    xuliehao=(By.XPATH,'//div[@class="qr"]//div')

    frist_order=(By.XPATH,'(//div[@class="order-shop"])[1]')

    click_xuliehao=(By.XPATH,'//input[@type="text"]')
    click_queding=(By.XPATH,'//button[contains(text(),"确定")]')
    click_queding2=(By.XPATH,'//li[contains(text(),"确定")]')

    qianyue=(By.XPATH,'//button[text()="确认签约"]')