#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/8 9:48
#@Author :春衫
#@File :MyIndex.py



class MyIndex:
    myIndex=(MobileBy.ID,'//i[@class="my-icon"]')
    setup = (MobileBy.ID,'//div[@class="back-icon"]')
    saleOrderList=(MobileBy.ID,'//div[text()="销售订单"]//parent::li')
    confirm_Order=(MobileBy.ID,'//button[text()="确认订单"]')
    confirm=(MobileBy.ID,'//ul[@class="sign-out-list"]//li[2]')
    ship=(MobileBy.ID,'//button[text()="发货"]')
    logistics_company=(MobileBy.ID,'//li[@class="logistics-company"]')
    debang=(MobileBy.ID,'//li[text()="德邦物流"]')
    dingdanhao=(MobileBy.ID,'//input[@placeholder="请输入物流单号"]')
    ship_now=(MobileBy.ID,'//div[text()="立即发货"]')
    receipt=(MobileBy.ID,'//button[text()="确认收货"]')
    purchase=(MobileBy.ID,'//div[@class="purchase"]')
    myPartner=(MobileBy.ID,'//div[text()="我的伙伴"]//parent::li')

    #test
    delete1=(MobileBy.ID,'//h4[text()="177****7781"]//parent::div[@class="name"]//following-sibling::div[@class="partner-contril"]')
    #mtest
    delete2=(MobileBy.ID,'//h4[text()="177****7786"]//parent::div[@class="name"]//following-sibling::div[@class="partner-contril"]')
    # dev1
    delete3 = (MobileBy.ID, '//h4[text()="一八八八"]//parent::div[@class="name"]//following-sibling::div[@class="partner-contril"]')

    serviceRecharge=(MobileBy.ID,'//div[text()="充值福利"]')
    recharge_amount=(MobileBy.ID,'//span[text()="自定义"]')
    input_amount=(MobileBy.ID,'//input[@placeholder="请输入金额"]')
    queren=(MobileBy.ID,'//span[contains(text(),"确认")]//parent::button')
    rechare_now=(MobileBy.ID,'//a[text()="立即充值"]')
    querenzhifu=(MobileBy.ID,'//a[text()="确认支付"]')

