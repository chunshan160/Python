#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/1 16:25
# @Author :春衫
# @File :Comm_Bus.py

import time
from Common.BaseDriver import BaseDriver
from PageLocators.Android.Welcome import welcome
from PageLocators.Android import Common
from PageObjects.Android.MyIndex.MyIndex import MyIndexPage
from PageObjects.Android.MyIndex.Setting.Setting import SettingPage
from PageLocators.Android.MyIndex import MyIndex
from Common.BasePage import BasePage
from PageObjects.Android.Login.Login_Page import LoginPage


class CommBus(BasePage):

    # 处理欢迎页面
    def do_welcome(self, text=""):
        doc = text + "处理欢迎页面-"
        time.sleep(2)
        # 如果没有找到首页的元素/或者不包含MainActivity,那么就是在欢迎页面
        curAct = self.driver.current_activity
        # 权限-始终允许
        if self.ele_if_exist(Common.always_allowed):
            self.click_element(Common.always_allowed)

        if curAct.find("HomeActivity") == -1:
            # 点击同意
            self.click_element(welcome.yes, doc=doc)
            # 滑动欢迎页面至首页
            size = self.get_size(doc=doc)
            for i in range(3):
                self.swipe_left(size, doc=doc)
                time.sleep(1)
            # 点击立即体验
            self.click_element(welcome.experience_now, doc=doc)
            # 权限-始终允许
            time.sleep(2)
            if self.ele_if_exist(Common.always_allowed):
                self.click_element(Common.always_allowed, doc=doc)

    # 获取当前app的登陆状态
    def get_loginStatus(self, text=""):
        doc = text + "获取当前app的登陆状态-"
        # 获取当前app的登陆状态。已登录为True，未登陆为False
        # 等待5秒
        # 找登陆/注册按钮
        self.click_element(Common.my_index, doc=doc)
        ele = self.ele_if_exist(MyIndex.setting)
        return ele

    # 首页
    def click_index(self, text=""):
        doc = text + "点击底部导航栏-首页-"
        self.click_element(Common.index, doc=doc)

    # 易货信用
    def click_credit_good(self, text=""):
        doc = text + "点击底部导航栏-易货信用-"
        self.click_element(Common.credit_good, doc=doc)

    # 焕焕商机
    def click_business(self, text=""):
        doc = text + "点击底部导航栏-焕焕商机-"
        self.click_element(Common.business, doc=doc)

    # 首页点击发布商品
    def click_publish_good(self, text=""):
        doc = text + "点击底部导航栏-发布商品-"
        self.click_element(Common.publish_good, doc=doc)

    # 我的
    def click_myindex(self, text=""):
        doc = text + "点击底部导航栏-我的-"
        self.click_element(Common.my_index, doc=doc)

    # 处理登陆账号
    def login(self, phone, password, text=""):
        doc = text + "处理登陆账号-"
        login_status = CommBus(self.driver).get_loginStatus(text=doc)
        if login_status == True:
            print("已经登录啦")
            # 登录手机号
            login_phone = BasePage(self.driver).get_text(MyIndex.phone, doc="")
            print("手机号是：", login_phone)
            if login_phone != phone:
                MyIndexPage(self.driver).click_setting(text=doc)
                SettingPage(self.driver).exit(text=doc)
                time.sleep(2)
                LoginPage(self.driver).login(phone, password, text=doc)
        else:
            print("没有登录")
            LoginPage(self.driver).login(phone, password, text=doc)


if __name__ == '__main__':
    driver = BaseDriver().base_driver("MI 8")
    CommBus(driver).do_welcome()
