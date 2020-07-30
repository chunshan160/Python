#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   :2019/12/27 16:55
# @Author :春衫
# @Email  :1605936478@qq.com
# @File   :systempoint_page.py


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.H5.Login import LoginPage as loc
from PageLocators.H5.Login import Retrieve_Password as RP
from PageLocators.H5.MyIndex import My
from PageLocators.H5.SystemPoint import SystemPoint as SP


# 系统提示页面，主要是为了断言用
class SystemPoint:

    def __init__(self, driver):
        self.driver = driver

    #为了判断登录成功，去看首页-我的，有没有【设置】这个元素
    def Perfection(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((My.setup)))
            return True
        except:
            return False

    # 获取错误提示信息 ----登录区域
    def Login_ErrorMag(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((loc.eror_toast)))
        return self.driver.find_element(*loc.eror_toast).text

    # 找回密码----找回成功
    def RetrievePassword_msg(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((RP.msg)))
        return self.driver.find_element(*RP.msg).text

    #支付成功
    def Pay_Success(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((SP.pay_success)))
        return self.driver.find_element(SP.pay_success).text
