#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/26 13:24
# @Author :春衫
# @File :conftest.py

import time
import pytest
from Common.BaseDriver import BaseDriver
from PageObjects.Comm_Bus import CommBus
from PageObjects.Android.Login.Login_Page import LoginPage
from TestData.Android.Publish_Data import Login_data
from TestData.Android.BuyGoods.BuyGoods import Login
from PageObjects.Android.Index.Index import IndexPage

params = ["MI 8"]


# 重启
@pytest.fixture(params=params)
def first_start_app(request):
    doc = "登录重启前置-"
    # 准备服务器参数，与appium server进行连接。
    driver = BaseDriver().base_driver(device=request.param, noReset=False)
    phone = request.param['phone']
    password = request.param['password']
    # 1、 要不要判断欢迎页面是否存在?
    CommBus(driver).do_welcome(text=doc)
    # 2、登录
    CommBus(driver).click_myindex(text=doc)
    time.sleep(2)
    LoginPage(driver).login(phone, password, text=doc)
    yield driver
    driver.close_app()
    driver.quit()


# 发布商品-通用条件
@pytest.fixture(params=params)
def open_app(request):
    doc = "发布商品-通用条件-"
    # 准备服务器参数，与appium server进行连接。
    driver = BaseDriver().base_driver(device=request.param)
    phone = Login_data['phone']
    password = Login_data['password']
    # 1、 要不要判断欢迎页面是否存在?
    CommBus(driver).do_welcome(text=doc)
    IndexPage(driver).location_pop_ups()
    #处理登录
    CommBus(driver).login(phone, password, text=doc)
    yield driver
    driver.close_app()
    driver.quit()

# 购买商品-通用条件
@pytest.fixture(params=params)
def buy_goods(request):
    doc = "购买商品-通用条件-"
    # 准备服务器参数，与appium server进行连接。
    driver = BaseDriver().base_driver(device=request.param)
    phone = Login['phone']
    password = Login['password']
    # 1、 要不要判断欢迎页面是否存在?
    CommBus(driver).do_welcome(text=doc)
    IndexPage(driver).location_pop_ups()
    #处理登录
    CommBus(driver).login(phone, password, text=doc)
    CommBus(driver).click_index(text=doc)
    IndexPage(driver).all_city(text=doc)
    yield driver
    driver.close_app()
    # driver.quit()
