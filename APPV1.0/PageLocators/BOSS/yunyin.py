#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/22 13:36
# @Author :春衫
# @File :yunyin.py



class YunYin:
    yunyin = (MobileBy.ID, '//li[text()="运营"]')
    fencheng=(MobileBy.ID,'//span[text()="分成设置"]//parent::li')
    yewuhaunshang=(MobileBy.ID,'//label[text()="业务焕商分成比例"]//following-sibling::div//div//input')
    xiaoshou=(MobileBy.ID,'//label[text()="销售分成比例"]//following-sibling::div//div//input')
    tco = (MobileBy.ID, '//label[text()="TCO分成比例"]//following-sibling::div//div//input')
    save=(MobileBy.ID,'//button[@class="el-button btn el-button--primary"]')