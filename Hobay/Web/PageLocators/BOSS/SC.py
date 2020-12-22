#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/6 17:40
# @Author :春衫
# @File :SuperShop.py




# 商超列表
class SC:
    #退出账号
    logout = (MobileBy.ID,'//div[@class="Logout"]')
    #确定
    queding = (MobileBy.ID,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    # 商超tap
    sc = (MobileBy.ID, '//li[text()="商超"]')
    # 商品入仓审核
    sc_review = (MobileBy.ID, '//span[text()="商品入仓审核"]')
    # 勾选商品
    goods_cwj = (MobileBy.ID,
                         '//div[contains(text(),"仓库中：未审核，复审拒绝")]/parent::td/parent::tr//td//div//label/span')
    goods_ctt = (MobileBy.ID,
                         '//div[contains(text(),"仓库中：审核通过，复审通过")]/parent::td/parent::tr//td//div//label/span')
    goods_ctd = (MobileBy.ID,
                         '//div[contains(text(),"仓库中：审核通过，待复审")]/parent::td/parent::tr//td//div//label/span')
    goods_djj = (MobileBy.ID,
                         '//div[contains(text(),"待审核:审核拒绝，复审拒绝")]/parent::td/parent::tr//td//div//label/span')
    goods_chutt = (MobileBy.ID,
                         '//div[contains(text(),"出售中:审核通过，复审通过")]/parent::td/parent::tr//td//div//label/span')
    goods_chusd = (MobileBy.ID,
                         '//div[contains(text(),"出售中:审核通过，待复审")]/parent::td/parent::tr//td//div//label/span')
    #点通过
    passed = (MobileBy.ID,'//span[text()="通过"]//parent::button')
    #点确认
    determine = (MobileBy.ID,'//span[contains(text(),"确定")]//parent::button')
