#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/25 17:26
# @Author :春衫
# @File :basepage.py

# 封装基本函数-执行日志、异常处理、失败截图
# 2、所有的页面公共的部分

import logging
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def _init_(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self,locator,times=30,poll_frequency=0.5,doc=""):
        logging.info(f"等待元素{locator}可见")
        try:
            #开始等待的时间
            start=datetime.datetime.now()
            WebDriverWait(self.driver,times,poll_frequency).until(EC.visibility_of_element_located(locator))
            #结束等待的时间点
            end=datetime.datetime.now()
            #求一个差值，写在日志里
            logging.info("等待时长为：{}")
        except:
            logging.exception("等待元素可见失败")
            #截图
            self.save_screenshot(doc)
            raise

    # 等待元素存在
    def wait_elePresence(self):
        pass

    # 查找元素
    def get_element(self,locator,doc=""):
        logging.info(f"查找元素{locator}")
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self,locator,doc=""):
        #找元素
        ele=self.get_element(locator,doc)
        logging.info(f"{doc}点击元素{locator}")
        #元素操作
        try:
            ele.ckick()
        except:
            logging.exception("元素点击操作失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self,locator,text,doc=""):
        ele=self.get_element(locator,doc)
        #输入操作
        try:
            ele.send_keys(text)
        except:
            logging.exception("元素输入操作失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self,locator,doc=""):
        ele = self.get_element(locator, doc)
        # 输入操作
        try:
            return ele.text
        except:
            logging.exception("获取元素文本内容失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的属性
    def get_elment_attribute(self,locator,attr,doc=""):
        ele = self.get_element(locator, doc)
        # 输入操作
        try:
            return ele.get_attribute(attr)
        except:
            logging.exception("获取元素的属性失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # alert处理
    def alert_action(self, action="accept"):
        pass

    # iframe切换
    def switch_iframe(self, iframe_reference):
        pass

    # 上传操作
    def upload_file(self):
        pass


    #截图
    def save_screenshot(self,name):
        time = datetime.datetime.now()
        #图片名称+模块名+页面名称+操作名称+时间.png
        file_name="截屏存放的路径"+f"{name},{time}.png"
        self.driver.save_screenshot(file_name)
        logging.info(f"截取网页成功，文件路径为为：{file_name}")