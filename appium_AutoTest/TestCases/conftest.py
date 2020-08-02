__author__ = '小翟'

import pytest
from Common.BaseDriver import BaseDriver
from PageObjects.welcome_page import WelcomePage
from PageObjects.index_page import IndexPage
from PageObjects.login_page import LoginPage
from TestDatas.CommonData import *
import time

params=["Honor_5C", "YeShen"]

#登录：无toast弹框，不重置
@pytest.fixture(params=params)
def login_common_driver(request):
    driver = BaseDriver().base_driver(device=request.param)
    is_welcome(driver)
    yield driver
    driver.close_app()
    driver.quit()


#登录：无toast弹出框，重置
@pytest.fixture(params=params)
def login_reset_driver(request):
    driver = BaseDriver().base_driver(device=request.param, noReset=False)
    is_welcome(driver)
    yield driver
    driver.close_app()
    driver.quit()


#登录：有toast弹出框，重置
@pytest.fixture(params=params)
def login_toast_reset_driver(request):
    driver = BaseDriver().base_driver(device=request.param, automationName="UIAutomator2", noReset=False)
    is_welcome(driver)
    yield driver
    driver.close_app()
    driver.quit()


#投资：无toast弹出框，不重置
@pytest.fixture(params=params)
def invest_common_driver(request):
    driver = BaseDriver().base_driver(device=request.param)
    is_welcome(driver)
    is_login(driver)
    yield driver
    driver.close_app()
    driver.quit()


#投资：有toast弹出框，不重置
@pytest.fixture(params=params)
def invest_toast_driver(request):
    driver = BaseDriver().base_driver(device=request.param, automationName="UIAutomator2")
    is_welcome(driver)
    is_login(driver)
    yield driver
    driver.close_app()
    driver.quit()



#判断是否是欢迎页面
def is_welcome(driver):
    #等待2s
    time.sleep(2)
    cur_activity = driver.current_activity
    if cur_activity.find("MainActivity") == -1:
        WelcomePage(driver).swipe_screen()


#判断是否是登录状态
def is_login(driver):
    try:
        IndexPage(driver).click_login()
        LoginPage(driver).input_phoneNumber(common_phoneNumber)
        LoginPage(driver).input_passwd(common_passwd)
        IndexPage(driver).click_later()
    except:
        pass

