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
    def do_welcome(self) :
        doc = "处理欢迎页面"
        time.sleep(7)
        #如果没有找到首页的元素/或者不包含MainActivity,那么就是在欢迎页面
        curAct = self.driver.current_activity
        if curAct.find("MainActivity")==-1:
            #点击同意
            self.wait_eleVisible(welcome.yes,doc =doc)
            self.get_element(welcome.yes,doc =doc).click()
            #滑动欢迎页面至首页
            size=self.get_size()
            for i in range(3):
                self.swipe_left(size)
                time.sleep(1)
            #点击立即体验
            self.get_element(welcome.experience_now,doc =doc).click()
            time.sleep(2)
            # 权限-始终允许
            self.get_element(Common.always_allowed,doc =doc).click()

    def get_loginStatus(self):
        doc = "获取当前app的登陆状态"
        #获取当前app的登陆状态。已登录为True，未登陆为False
        try:
            #等待5秒
            time.sleep(5)
            #找登陆/注册按钮
            self.get_element(Common.my_index,doc =doc).click()
            time.sleep(0.5)
            self.get_element(MyIndex.setting,doc =doc)
            return True
        except:
            return False

    #导航栏
    def click_myindex(self):
        doc = "点击底部导航栏-我的"
        time.sleep(1)
        self.wait_eleVisible(Common.my_index,doc =doc)
        self.get_element(Common.my_index,doc =doc).click()

if __name__ == '__main__':
    driver=BaseDriver().base_driver("MI 8")
    CommBus(driver).do_welcome()