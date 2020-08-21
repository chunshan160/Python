#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/8 9:48
#@Author :春衫
#@File :MyIndex.py

from selenium.webdriver.common.by import By

class MyIndex:
    myIndex=(By.XPATH,'//i[@class="my-icon"]')
    setup = (By.XPATH,'//div[@class="back-icon"]')
    saleOrderList=(By.XPATH,'//div[text()="销售订单"]//parent::li')
    confirm_Order=(By.XPATH,'//button[text()="确认订单"]')
    confirm=(By.XPATH,'//ul[@class="sign-out-list"]//li[2]')
    ship=(By.XPATH,'//button[text()="发货"]')
    logistics_company=(By.XPATH,'//li[@class="logistics-company"]')
    debang=(By.XPATH,'//li[text()="德邦物流"]')
    dingdanhao=(By.XPATH,'//input[@placeholder="请输入物流单号"]')
    ship_now=(By.XPATH,'//div[text()="立即发货"]')
    receipt=(By.XPATH,'//button[text()="确认收货"]')
    purchase=(By.XPATH,'//div[@class="purchase"]')
    myPartner=(By.XPATH,'//div[text()="我的伙伴"]//parent::li')

    #test
    delete1=(By.XPATH,'//h4[text()="177****7781"]//parent::div[@class="name"]//following-sibling::div[@class="partner-contril"]')
    #mtest
    delete2=(By.XPATH,'//h4[text()="177****7786"]//parent::div[@class="name"]//following-sibling::div[@class="partner-contril"]')
    # dev1
    delete3 = (By.XPATH, '//h4[text()="一八八八"]//parent::div[@class="name"]//following-sibling::div[@class="partner-contril"]')

    serviceRecharge=(By.XPATH,'//div[text()="充值福利"]')
    recharge_amount=(By.XPATH,'//span[text()="自定义"]')
    input_amount=(By.XPATH,'//input[@placeholder="请输入金额"]')
    queren=(By.XPATH,'//span[contains(text(),"确认")]//parent::button')
    rechare_now=(By.XPATH,'//a[text()="立即充值"]')
    querenzhifu=(By.XPATH,'//a[text()="确认支付"]')

