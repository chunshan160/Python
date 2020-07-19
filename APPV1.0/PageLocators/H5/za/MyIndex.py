#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/8 9:48
#@Author :春衫
#@File :MyIndex.py



class MyIndex:
    myIndex=("id",'//i[@class="my-icon"]')
    setup = ("id",'//div[@class="back-icon"]')
    saleOrderList=("id",'//div[text()="销售订单"]//parent::li')
    confirm_Order=("id",'//button[text()="确认订单"]')
    confirm=("id",'//ul[@class="sign-out-list"]//li[2]')
    ship=("id",'//button[text()="发货"]')
    logistics_company=("id",'//li[@class="logistics-company"]')
    debang=("id",'//li[text()="德邦物流"]')
    dingdanhao=("id",'//input[@placeholder="请输入物流单号"]')
    ship_now=("id",'//div[text()="立即发货"]')
    receipt=("id",'//button[text()="确认收货"]')
    purchase=("id",'//div[@class="purchase"]')
    myPartner=("id",'//div[text()="我的伙伴"]//parent::li')

    #test
    delete1=("id",'//h4[text()="177****7781"]//parent::div[@class="name"]//following-sibling::div[@class="partner-contril"]')
    #mtest
    delete2=("id",'//h4[text()="177****7786"]//parent::div[@class="name"]//following-sibling::div[@class="partner-contril"]')
    # dev1
    delete3 = ("id", '//h4[text()="一八八八"]//parent::div[@class="name"]//following-sibling::div[@class="partner-contril"]')

    serviceRecharge=("id",'//div[text()="充值福利"]')
    recharge_amount=("id",'//span[text()="自定义"]')
    input_amount=("id",'//input[@placeholder="请输入金额"]')
    queren=("id",'//span[contains(text(),"确认")]//parent::button')
    rechare_now=("id",'//a[text()="立即充值"]')
    querenzhifu=("id",'//a[text()="确认支付"]')

