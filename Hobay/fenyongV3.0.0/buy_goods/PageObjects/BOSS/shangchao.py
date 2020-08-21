#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/6 18:21
# @Author :春衫
# @File :SuperShop.py

import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from buy_goods.PageLocators.BOSS.SC import SC
# from buy_goods.PageLocators.BOSS.new import Local_Life as LL
# from buy_goods.PageLocators.BOSS.new import Business_Services as BS
from buy_goods.PageLocators.BOSS.PublishGoods import Pubilc
from buy_goods.PageLocators.BOSS.PublishGoods import Local_Life as LL
from buy_goods.PageLocators.BOSS.PublishGoods import Business_Services as BS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# 商品入仓审核
class ShangChao:

    def __init__(self, driver):
        self.driver = driver

    def sc(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((SC.sc))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((SC.sc_review))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((SC.goods_cwj))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((SC.goods_ctt))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((SC.goods_ctd))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((SC.goods_djj))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((SC.goods_chutt))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((SC.goods_chusd))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((SC.passed))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((SC.determine))).click()
