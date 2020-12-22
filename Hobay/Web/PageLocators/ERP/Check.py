#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/7 12:40
# @Author :春衫
# @File :Check.py




class Check:
    # 商品中心
    goods_center = (MobileBy.ID, '//span[text()="商品中心"]')
    # 商品审核
    good_check = (MobileBy.ID, '//li[contains(text(),"商品审核")]')
    # 搜索框卖家手机
    search_phone = (MobileBy.ID, '//*[contains(text(),"卖家手机")]//following-sibling::div//div//input')
    # 点击查询
    search = (MobileBy.ID, '//span[contains(text(),"查询")]')
    # 审核指定商品
    check_chutd = (MobileBy.ID,
                   '//div[@class="el-table__fixed-right"]//div[contains(text(),"出售中:审核通过，待复审")]//..//..//span[contains(text(),"审核")]')
    check_chutt = (MobileBy.ID,
                   '//div[@class="el-table__fixed-right"]//div[contains(text(),"出售中:审核通过，复审通过")]//..//..//span[contains(text(),"审核")]')
    check_djj = (MobileBy.ID,
                 '//div[@class="el-table__fixed-right"]//div[contains(text(),"待审核:审核拒绝，复审拒绝")]//..//..//span[contains(text(),"审核")]')
    check_ctd = (MobileBy.ID,
                 '//div[@class="el-table__fixed-right"]//div[contains(text(),"仓库中：审核通过，待复审")]//..//..//span[contains(text(),"审核")]')
    check_ctt = (MobileBy.ID,
                 '//div[@class="el-table__fixed-right"]//div[contains(text(),"仓库中：审核通过，复审通过")]//..//..//span[contains(text(),"审核")]')
    check_cwj = (MobileBy.ID,
                 '//div[@class="el-table__fixed-right"]//div[contains(text(),"仓库中：未审核，复审拒绝")]//..//..//span[contains(text(),"审核")]')
    # 审核通过
    check_pass = (MobileBy.ID, '//button[@class="el-button el-button--primary"]')
    determine_1 = (MobileBy.ID, '//span[contains(text(),"确定")]//parent::button')
    # 审核拒绝
    check_refuse = (MobileBy.ID, '//button[@class="el-button el-button--danger"]')
    refuse_reason = (MobileBy.ID, '//textarea')
    determine_2 = (MobileBy.ID, '//button[@class="el-button btn el-button--primary"]')
