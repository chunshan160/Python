#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/22 13:36
# @Author :春衫
# @File :yunyin.py
from selenium.webdriver.common.by import By


class YunYin:
    yunyin = (By.XPATH, '//li[text()="运营"]')
    fencheng=(By.XPATH,'//span[text()="分成设置"]//parent::li')
    yewuhaunshang=(By.XPATH,'//label[text()="业务焕商分成比例"]//following-sibling::div//div//input')
    xiaoshou=(By.XPATH,'//label[text()="销售分成比例"]//following-sibling::div//div//input')
    tco = (By.XPATH, '//label[text()="TCO分成比例"]//following-sibling::div//div//input')
    save=(By.XPATH,'//button[@class="el-button btn el-button--primary"]')