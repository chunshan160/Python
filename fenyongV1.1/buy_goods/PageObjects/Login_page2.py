# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 12:27
# @Author  : 春衫
# @Email   : 1605936478@qq.com
# @File    : login_page.py
# @Software: PyCharm


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from buy_goods.PageLocators.Login import LoginPage as loc
from buy_goods.PageLocators.Login import common


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # 正常登录操作
    def login(self, phone):
        # 输入手机号
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((common.name))).send_keys(phone)
        # 点击下一步
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((common.next))).click()
        # 点击验证码
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.click_code))).click()
        #输入验证码
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.verification_code))).send_keys(666666)
        # 点击登录
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.login_but))).click()
        # 首页弹出来的城市定位
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.location))).click()