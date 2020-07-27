#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/26 13:24
#@Author :春衫
#@File :conftest.py

import pytest
from selenium import webdriver

##声明它是一个fixture
@pytest.fixture(scope="class")
def access_web():
    global driver
    #前置操作
    print("=zaasaa==所有测试用例之前的，setup===整个测试类只执行一次===s===")
    driver = webdriver.Chrome ()
    driver.get(CD.web_login_ur1)
    lg = LoginPage(driver)
    yield (driver,lg)
    #分隔线﹔#后面接返回值
    #后置操作
    print("=aaa=所有测试用例之后的，teardwon=--整个测试类只执行一次==aa===")
    driver.quit()

@pytest.fixture
def refresh_page():
    global driver
    #前置操作
    yield
    #后置操作
    driver.refresh()

