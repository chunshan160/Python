#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/6 17:40
# @Author :春衫
# @File :SuperShop.py

from selenium.webdriver.common.by import By


# 商超列表
class SC:
    #退出账号
    logout = (By.XPATH,'//div[@class="Logout"]')
    #确定
    queding = (By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    # 商超tap
    sc = (By.XPATH, '//li[text()="商超"]')
    # 商品入仓审核
    sc_review = (By.XPATH, '//span[text()="商品入仓审核"]')
    # 勾选商品
    goods_cwj = (By.XPATH,
                         '//div[contains(text(),"仓库中：未审核，复审拒绝")]/parent::td/parent::tr//td//div//label/span')
    goods_ctt = (By.XPATH,
                         '//div[contains(text(),"仓库中：审核通过，复审通过")]/parent::td/parent::tr//td//div//label/span')
    goods_ctd = (By.XPATH,
                         '//div[contains(text(),"仓库中：审核通过，待复审")]/parent::td/parent::tr//td//div//label/span')
    goods_djj = (By.XPATH,
                         '//div[contains(text(),"待审核:审核拒绝，复审拒绝")]/parent::td/parent::tr//td//div//label/span')
    goods_chutt = (By.XPATH,
                         '//div[contains(text(),"出售中:审核通过，复审通过")]/parent::td/parent::tr//td//div//label/span')
    goods_chusd = (By.XPATH,
                         '//div[contains(text(),"出售中:审核通过，待复审")]/parent::td/parent::tr//td//div//label/span')
    #点通过
    passed = (By.XPATH,'//span[text()="通过"]//parent::button')
    #点确认
    determine = (By.XPATH,'//span[contains(text(),"确定")]//parent::button')
