#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/9 16:24
# @Author :春衫
# @File :SuperShop_page.py

from selenium.webdriver.common.action_chains import ActionChains
from web_test.PageLocators.H5.SuperShop import SC

class ShangChao:
    def __init__(self, driver):
        self.driver = driver

    def Join_SC(self,good_name,goods_value):
        #登陆后，滑动标签，寻找【焕焕商超】，点击
        ActionChains(self.driver).move_to_element(self.driver.find_element(*SC.home_sc_label)).click(
            self.driver.find_element(*SC.home_sc)).perform()
        #点击底部的【焕焕商超】
        self.driver.find_element(*SC.sc_all).click()
        #找商超
        #先写根据唯一图片定位商超的先
        #以后用搜索的方式
        self.driver.find_element(*SC.sc_select).click()
        #点击加入按钮
        self.driver.find_element(*SC.sc_join).click()
        #提供已有商品
        self.driver.find_element(*SC.provide_good).click()
        #搜索商品名
        self.driver.find_element(*SC.good_name).send_keys(good_name)
        #默认商品唯一，勾选第一个
        self.driver.find_element(*SC.good).click()
        self.driver.find_element(*SC.confirm).click()
        #货品价值
        self.driver.find_element(*SC.goods_value).send_keys(goods_value)
        #所在地区
        self.driver.find_element(*SC.location).click()
        #直接确定
        self.driver.find_element(*SC.determine).click()
        #立即报名
        self.driver.find_element(*SC.sign_up_now).click()