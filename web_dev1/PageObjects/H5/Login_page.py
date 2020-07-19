# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 12:27
# @Author  : 春衫
# @Email   : 1605936478@qq.com
# @File    : login_page.py
# @Software: PyCharm


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_dev1.PageLocators.H5.Login import LoginPage as loc
from web_dev1.PageLocators.H5.Login import Registered
from web_dev1.PageLocators.H5.Login import common
from web_dev1.PageLocators.H5.Login import Retrieve_Password as RP
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # 正常登录操作
    def login(self, username, password):
        # 输入手机号
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((common.name))).send_keys(username)
        # 点击下一步
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((common.next))).click()
        # 输入密码
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.pwd))).send_keys(password)
        # 点击登录
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.login_but))).click()
        # 首页弹出来的城市定位
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.location))).click()

    # 异常登录（手机号不正确）
    def PhoneError(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((common.name))).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((common.next))).click()

    # 异常登录（密码不正确）
    def PasswordError(self, username, password):
        # 输入手机号
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((common.name))).send_keys(username)
        # 点击下一步
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((common.next))).click()
        # 输入密码
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.pwd))).send_keys(password)
        # 点击登录
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.login_but))).click()

    # 注册
    def Registered(self, username, code, invite_people):
        # 输入手机号
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((common.name))).send_keys(username)
        # 点击下一步
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((common.next))).click()
        # 点击立即注册
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.registered))).click()
        # 输入验证码
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.verification_code))).send_keys(code)
        # 点击下一步
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((common.next))).click()
        time.sleep(1)
        # 定位
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Registered.location))).click()
        # 滚动至元素可见
        # 省
        province = self.driver.find_element(Registered.province)
        self.driver.execute_script("arguments[0].scrollIntoView();", province).click()
        # 市
        city = self.driver.find_element(Registered.city)
        self.driver.execute_script("arguments[0].scrollIntoView();", city).click()
        # 区
        area = self.driver.find_element(Registered.area)
        self.driver.execute_script("arguments[0].scrollIntoView();", area).click()
        # 邀请人
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Registered.invite_people))).send_keys(
            invite_people)
        # 勾选协议
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Registered.tick))).click()
        # 完成
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Registered.perfection))).click()

    # 忘记密码
    def RetrievePassword(self, username, code, password):
        # 输入手机号
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((common.name))).send_keys(username)
        # 点击下一步
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((common.next))).click()
        # 找回密码
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RP.retrieve_password))).click()
        # 输入验证码
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RP.verification_code))).send_keys(code)
        # 输入新密码
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RP.pwd_new))).send_keys(password)
        # 再次输入新密码
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RP.pwd_again))).send_keys(password)
        # 提交
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RP.submit))).click()
