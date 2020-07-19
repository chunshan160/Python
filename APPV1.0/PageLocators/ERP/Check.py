#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/7 12:40
# @Author :春衫
# @File :Check.py




class Check:
    # 商品中心
    goods_center = ("id", '//span[text()="商品中心"]')
    # 商品审核
    good_check = ("id", '//li[contains(text(),"商品审核")]')
    # 搜索框卖家手机
    search_phone = ("id", '//*[contains(text(),"卖家手机")]//following-sibling::div//div//input')
    # 点击查询
    search = ("id", '//span[contains(text(),"查询")]')
    # 审核指定商品
    check_chutd = ("id",
                   '//div[@class="el-table__fixed-right"]//div[contains(text(),"出售中:审核通过，待复审")]//..//..//span[contains(text(),"审核")]')
    check_chutt = ("id",
                   '//div[@class="el-table__fixed-right"]//div[contains(text(),"出售中:审核通过，复审通过")]//..//..//span[contains(text(),"审核")]')
    check_djj = ("id",
                 '//div[@class="el-table__fixed-right"]//div[contains(text(),"待审核:审核拒绝，复审拒绝")]//..//..//span[contains(text(),"审核")]')
    check_ctd = ("id",
                 '//div[@class="el-table__fixed-right"]//div[contains(text(),"仓库中：审核通过，待复审")]//..//..//span[contains(text(),"审核")]')
    check_ctt = ("id",
                 '//div[@class="el-table__fixed-right"]//div[contains(text(),"仓库中：审核通过，复审通过")]//..//..//span[contains(text(),"审核")]')
    check_cwj = ("id",
                 '//div[@class="el-table__fixed-right"]//div[contains(text(),"仓库中：未审核，复审拒绝")]//..//..//span[contains(text(),"审核")]')
    # 审核通过
    check_pass = ("id", '//button[@class="el-button el-button--primary"]')
    determine_1 = ("id", '//span[contains(text(),"确定")]//parent::button')
    # 审核拒绝
    check_refuse = ("id", '//button[@class="el-button el-button--danger"]')
    refuse_reason = ("id", '//textarea')
    determine_2 = ("id", '//button[@class="el-button btn el-button--primary"]')
