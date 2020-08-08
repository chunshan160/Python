#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/1 16:25
# @Author :春衫
# @File :Comm_Bus.py

import time
from Common.BaseDriver import BaseDriver
from Common.BasePage import BasePage
from PageLocators.H5.Welcome import welcome
from PageLocators.H5 import Common
from PageLocators.H5.MyIndex import MyIndex


class CommBus(BasePage):

    # 处理欢迎页面
    def do_welcome(self, text=""):
        doc = text + "处理欢迎页面-"
        time.sleep(7)
        # 如果没有找到首页的元素/或者不包含MainActivity,那么就是在欢迎页面
        curAct = self.driver.current_activity

        # 权限-始终允许
        ele = self.ele_if_exist(Common.always_allowed)
        if ele:
            self.click_element(Common.always_allowed)

        if curAct.find("HomeActivity") == -1:
            # 点击同意
            self.wait_eleVisible(welcome.yes, doc=doc)
            self.click_element(welcome.yes, doc=doc)
            # 滑动欢迎页面至首页
            size = self.get_size(doc=doc)
            for i in range(3):
                self.swipe_left(size, doc=doc)
                time.sleep(1)
            # 点击立即体验
            self.click_element(welcome.experience_now, doc=doc)
            time.sleep(2)
            # 权限-始终允许
            self.click_element(Common.always_allowed, doc=doc)

    def get_loginStatus(self, text=""):
        doc = text + "获取当前app的登陆状态-"
        # 获取当前app的登陆状态。已登录为True，未登陆为False
        # 等待5秒
        time.sleep(5)
        # 找登陆/注册按钮
        self.click_element(Common.my_index, doc=doc)
        time.sleep(0.5)
        ele=self.ele_if_exist(MyIndex.setting)
        return ele

    # 我的
    def click_myindex(self, text=""):
        doc = text + "点击底部导航栏-我的-"
        time.sleep(1)
        self.wait_eleVisible(Common.my_index, doc=doc)
        self.click_element(Common.my_index, doc=doc)

    # 易货信用
    def click_credit_good(self, text=""):
        doc = text + "点击底部导航栏-易货信用-"
        time.sleep(1)
        self.wait_eleVisible(Common.credit_good, doc=doc)
        self.click_element(Common.credit_good, doc=doc)

    # 焕焕商机
    def click_business(self, text=""):
        doc = text + "点击底部导航栏-焕焕商机-"
        time.sleep(1)
        self.wait_eleVisible(Common.business, doc=doc)
        self.click_element(Common.business, doc=doc)

    # 首页点击发布商品
    def click_publish_good(self, text=""):
        doc = text + "点击底部导航栏-发布商品-"
        time.sleep(1)
        self.wait_eleVisible(Common.publish_good, doc=doc)
        self.click_element(Common.publish_good, doc=doc)


if __name__ == '__main__':
    driver = BaseDriver().base_driver("MI 8")
    CommBus(driver).do_welcome()
