#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/26 13:24
# @Author :春衫
# @File :conftest.py

import time
import pytest
import yaml
from appium import webdriver
from Common.project_path import caps_dir
from PageObjects.Comm_Bus import CommBus


# 登陆用例使用的前置后置
@pytest.fixture
def startApp():
    # 准备服务器参数，与appium server进 行连接。noReset=True
    driver = baseDriver()
    # 1、 要不要判断欢迎页面是否存在?
    CommBus(driver).do_welcome()
    # 2、要不要判断当前用户是否已登陆?
    # 3、如果已经登录，那么先退出登录--接口挤号


# 除登录以外，通用的前置条件
@pytest.fixture
def loginApp():
    # 准备服务器参数，与appium server进行连接 。noReset = True
    driver = baseDriver()
    # 1、 要不要判断欢迎 页面是否存在?
    CommBus(driver).do_welcome()
    # 2、判断是否是已登陆状态,若没有登录，则登录


def baseDriver(server_port=4723, noReset=None, automationName=None, **kwargs):
    # 将默认的配置数据读取出来
    fs = open(caps_dir + "/Caps.yaml")
    desired_caps = yaml.load(fs, Loader=yaml.FullLoader)
    # 调整参数
    if noReset is not None:
        desired_caps["noReset"] = noReset
    if automationName is not None:
        desired_caps["noReset"] = automationName
    # 返回一个启动对象一driver
    return webdriver.Remote(f"http://127.0.0.1:{server_port}/wd/hub", desired_caps)
