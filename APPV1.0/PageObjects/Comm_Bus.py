#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/1 16:25
# @Author :春衫
# @File :Comm_Bus.py

import time
from Common.BasePage import BasePage

class CommBus(BasePage):
    # 处理欢迎页面
    def do_welcome(self) :
        time.sleep(7)
        #如果没有找到首页的元素/或者不包含MainActivity,那么就是在欢迎页面
        curAct = self.driver.current_acitivity
        if curAct.find("MainActivity")==-1:
            #滑动欢迎页面至首页
            size=self.get_size()
            for i in range(3):
                self.swipe_left(size)
                time.sleep(1)
            #点击立即体验

    def get_loginStatus(self):
        #获取当前app的登陆状态。已登录为True，未登陆为False
        try:
            #等待5秒  #找登陆/注册按钮
            return True
        except:
            return False
    #导航栏
