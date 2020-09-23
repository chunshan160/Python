#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/26 13:24
# @Author :春衫
# @File :conftest.py

import time
import pytest
from selenium import webdriver
from Driver.WebDriver import BrowserEngine
# from PageObjects.Web.Comm_Bus import CommBus
from PageObjects.Web.Login.Login_Page import LoginPage
from TestData.Web.Publish_Data import Login_data
from TestData.Web.BuyGoods.BuyGoods import Login
from PageObjects.Web.Index.Index import IndexPage
from TestData.Web.Common_Data import H5_Login_url


# # 发布商品-通用条件
# @pytest.fixture(params=params)
# def open_app(request):
#     doc = "发布商品-通用条件-"
#     # 准备服务器参数，与appium server进行连接。
#     driver = AndroidDriver().android_driver(device=request.param)
#     phone = Login_data['phone']
#     password = Login_data['password']
#     # 1、 要不要判断欢迎页面是否存在?
#     CommBus(driver).do_welcome(text=doc)
#     IndexPage(driver).location_pop_ups()
#     #处理登录
#     CommBus(driver).login(phone, password, text=doc)
#     yield driver
#     driver.close_app()
#     driver.quit()
#
# # 购买商品-通用条件
# @pytest.fixture(params=params)
# def app_buy_goods(request):
#     doc = "购买商品-通用条件-"
#     # 准备服务器参数，与appium server进行连接。
#     driver = AndroidDriver().android_driver(device=request.param)
#     phone = Login['phone']
#     password = Login['password']
#     # 1、 要不要判断欢迎页面是否存在?
#     CommBus(driver).do_welcome(text=doc)
#     IndexPage(driver).location_pop_ups()
#     #处理登录
#     CommBus(driver).login(phone, password, text=doc)
#     CommBus(driver).click_index(text=doc)
#     IndexPage(driver).all_city(text=doc)
#     yield driver
#     driver.close_app()
#     driver.quit()

# 购买商品-通用条件
@pytest.fixture()
def web_buy_goods():
    doc = "购买商品-通用条件-"
    mobile_emulation = {'deviceName': 'iPhone X'}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver=BrowserEngine().get_browser(chrome_options)
    #跳转登录页面
    driver.get(H5_Login_url)
    #登录
    LoginPage(driver).login("17777777781","qaz123",text=doc)
    yield driver
    driver.refresh()