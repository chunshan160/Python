#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/26 13:24
#@Author :春衫
#@File :conftest.py

import time
import pytest
import yaml
from Common.basepage import BasePage

#登陆用例使用的前置后置
@pytest.fixture
def startApp() :
    #准备服务器参数，与appium server进 行连接。noReset=True
    #1、 要不要判断欢迎页面是否存在?
    do_welcome()
    #2、要不要判断当前用户是否已登陆?
    #3、如果已经登录，那么先退出登录--接口挤号


# 处理欢迎页面
def do_welcome(driver) :
    #如果没有找到首页的元素/或者不包含MainActivity,那么就是在欢迎页面
    curAct = driver.current_acitivity
    if curAct.find("MainActivity")==-1:
        #滑动欢迎页面至首页
        size=BasePage(driver).get_size()
        for i in range(3):
            BasePage(driver).swipe_left(size)
            time.sleep(1)
        #点击立即体验

def get_loginStatus(driver):
    #获取当前app的登陆状态。已登录为True，未登陆为False
    try:
        #等待5秒  #找登陆/注册按钮
        return True
    except:
        return False

def baseDriver() :
    #将默认的配置数据读取出来
    fs=open()
    #调整参数
    #返回一个启动对象一driver


