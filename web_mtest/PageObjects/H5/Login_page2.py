# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 12:27
# @Author  : 春衫
# @Email   : 1605936478@qq.com
# @File    : login_page.py
# @Software: PyCharm


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_mtest.PageLocators.H5.Login import LoginPage as loc
from web_mtest.PageLocators.H5.Login import Registered
from web_mtest.PageLocators.H5.Login import common
from web_mtest.PageLocators.H5.Login import Retrieve_Password as RP
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # 正常登录操作
    def login(self, username):
        # 输入手机号
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((common.name))).send_keys(username)
        # 点击下一步
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((common.next))).click()
        # 输入密码
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.pwd))).send_keys("qaz123")
        # 点击登录
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.login_but))).click()
        # 首页弹出来的城市定位
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.location))).click()