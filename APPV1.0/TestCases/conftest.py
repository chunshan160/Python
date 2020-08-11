#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/26 13:24
# @Author :春衫
# @File :conftest.py

import time
import pytest
from Common.BaseDriver import BaseDriver
from Common.BasePage import BasePage
from PageObjects.Comm_Bus import CommBus
from PageObjects.H5.Login.Login_Page import LoginPage
from PageObjects.H5.MyIndex.MyIndex import MyIndexPage
from PageObjects.H5.MyIndex.Setting.Setting import SettingPage
from PageLocators.H5.MyIndex import MyIndex
from TestData.H5.Login_Data import Success_data

params = ["MI 8"]


# 登陆，重启
@pytest.fixture(params=params)
def first_start_app(request):
    doc = "登录重启前置-"
    # 准备服务器参数，与appium server进行连接。
    driver = BaseDriver().base_driver(device=request.param, noReset=False)
    # 1、 要不要判断欢迎页面是否存在?
    CommBus(driver).do_welcome(text=doc)
    # 2、登录
    CommBus(driver).click_myindex(text=doc)
    yield driver


# 发布商品-通用条件
@pytest.fixture(params=params)
def open_app(request):
    doc = "发布商品-通用条件-"
    # 准备服务器参数，与appium server进行连接。
    driver = BaseDriver().base_driver(device=request.param)
    # 1、 要不要判断欢迎页面是否存在?
    CommBus(driver).do_welcome(text=doc)
    # 2、要不要判断当前用户是否已登陆?
    login_status = CommBus(driver).get_loginStatus(text=doc)
    if login_status == True:
        print("已经登录啦")
        # 登录手机号
        login_phone = BasePage(driver).get_text(MyIndex.phone, doc="")
        print("手机号是：",login_phone)
        if login_phone != Success_data["phone"]:
            MyIndexPage(driver).click_setting(text=doc)
            SettingPage(driver).exit(text=doc)
            time.sleep(2)
            LoginPage(driver).login(Success_data["phone"], Success_data["password"], text=doc)
    else:
        print("没有登录")
        time.sleep(2)
        LoginPage(driver).login(Success_data["phone"], Success_data["password"], text=doc)
    yield driver
    driver.close_app()
    driver.quit()

