#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/7 12:40
# @Author :春衫
# @File :Check.py

from selenium.webdriver.common.by import By


class Check:
    # 商品中心
    goods_center = (By.XPATH, '//span[text()="商品中心"]')
    # 商品审核
    good_check = (By.XPATH, '//li[contains(text(),"商品审核")]')
    # 搜索框卖家手机
    search_phone = (By.XPATH, '//*[contains(text(),"卖家手机")]//following-sibling::div//div//input')
    # 点击查询
    search = (By.XPATH, '//span[contains(text(),"查询")]')
    # 审核指定商品
    check_chutd = (By.XPATH,
                   '//div[@class="el-table__fixed-right"]//div[contains(text(),"出售中:审核通过，待复审")]//..//..//span[contains(text(),"审核")]')
    check_chutt = (By.XPATH,
                   '//div[@class="el-table__fixed-right"]//div[contains(text(),"出售中:审核通过，复审通过")]//..//..//span[contains(text(),"审核")]')
    check_djj = (By.XPATH,
                 '//div[@class="el-table__fixed-right"]//div[contains(text(),"待审核:审核拒绝，复审拒绝")]//..//..//span[contains(text(),"审核")]')
    check_ctd = (By.XPATH,
                 '//div[@class="el-table__fixed-right"]//div[contains(text(),"仓库中：审核通过，待复审")]//..//..//span[contains(text(),"审核")]')
    check_ctt = (By.XPATH,
                 '//div[@class="el-table__fixed-right"]//div[contains(text(),"仓库中：审核通过，复审通过")]//..//..//span[contains(text(),"审核")]')
    check_cwj = (By.XPATH,
                 '//div[@class="el-table__fixed-right"]//div[contains(text(),"仓库中：未审核，复审拒绝")]//..//..//span[contains(text(),"审核")]')
    # 审核通过
    check_pass = (By.XPATH, '//button[@class="el-button el-button--primary"]')
    determine_1 = (By.XPATH, '//span[contains(text(),"确定")]//parent::button')
    # 审核拒绝
    check_refuse = (By.XPATH, '//button[@class="el-button el-button--danger"]')
    refuse_reason = (By.XPATH, '//textarea')
    determine_2 = (By.XPATH, '//button[@class="el-button btn el-button--primary"]')
