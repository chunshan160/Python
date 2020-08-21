#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/3 16:05
#@Author :春衫
#@File :BuyGoods.py



class BuyGoods:
    #点击加入易购车
    cart = (MobileBy.ID,'//div[@class="joincart"]')
    #数量+
    add = (MobileBy.ID,'//span[contains(text(),"+")]')
    #确定
    determine = (MobileBy.ID, '//div[contains(text(),"确")]')
    #添加成功msg
    success_msg = (MobileBy.ID,'//div[contains(text(),"添加成功")]')
    #立即购买
    buy_now = (MobileBy.ID,'//div[@class="r-server"]')
    #提交订单
    submit_orders = (MobileBy.ID,'//button[contains(text(),"提交订单")]')
    #更换支付方式
    payment_method = (MobileBy.ID,'//span[contains(text(),"更换支付方式")]')
    #选择易贝券
    yibeiquan = (MobileBy.ID,'//div[contains(text(),"易贝券")]//..//parent::div[@class="detaisl"]//parent::li')
    #选择抵工资
    digongzi = (MobileBy.ID,'//div[contains(text(),"抵工资")]//..//parent::div[@class="detaisl"]//parent::li')
    #选择家人购
    jiarengou = (MobileBy.ID,'//li[@class="li last-li"]')
    #选择现金账户
    xianjinzhanghu = (MobileBy.ID,'//div[contains(text(),"现金账户")]//..//parent::div[@class="detaisl"]//parent::li')
    #确认支付
    confirm_payment = ((MobileBy.ID,'//a[contains(text(),"确认支付")]'))
    #支付密码
    pay_1 = (MobileBy.ID,'//i[contains(text(),"1")]')
    pay_2 = (MobileBy.ID, '//i[contains(text(),"2")]')
    pay_3 = (MobileBy.ID, '//i[contains(text(),"3")]')
    pay_4 = (MobileBy.ID, '//i[contains(text(),"4")]')
    pay_5 = (MobileBy.ID, '//i[contains(text(),"5")]')
    pay_6 = (MobileBy.ID, '//i[contains(text(),"6")]')
    #支付成功
    pay_success = (MobileBy.ID,'//p[contains(text(),"支付成功")]')
    #返回首页
    Back_to_Home = (MobileBy.ID,'//div[@class="button-div index"]')

    xuliehao=(MobileBy.ID,'//div[@class="qr"]//div')

    frist_order=(MobileBy.ID,'(//div[@class="order-shop"])[1]')

    click_xuliehao=(MobileBy.ID,'//input[@type="text"]')
    click_queding=(MobileBy.ID,'//button[contains(text(),"确定")]')
    click_queding2=(MobileBy.ID,'//li[contains(text(),"确定")]')

    qianyue=(MobileBy.ID,'//button[text()="确认签约"]')