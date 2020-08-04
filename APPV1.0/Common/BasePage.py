#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/25 17:26
# @Author :春衫
# @File :BasePage.py

# 封装基本函数-执行日志、异常处理、失败截图
# 2、所有的页面公共的部分


import datetime
import time
import win32gui
import win32con
from Common.user_log import UserLog
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from Common.project_path import error_image


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = UserLog()

    # 查找某个元素
    def get_element(self, locator, doc=""):
        try:
            by = locator[0]
            value = locator[1]
            self.logger.info("定位方式:by." + by + "--->定位值:" + value)
            return self.driver.find_element(*locator)
        except:
            self.logger.info("没有找到这个元素")
            # 截图
            self.save_screenshot(doc)
            raise

    # 查找多个元素
    def get_elements(self, locator, doc=""):
        try:
            by = locator[0]
            value = locator[1]
            self.logger.info("定位方式:by." + by + "--->定位值:" + value)
            return self.driver.find_elements(*locator)
        except:
            self.logger.info("没有找到这些元素")
            # 截图
            self.save_screenshot(doc)
            raise

    # 等待元素可见
    def wait_eleVisible(self, locator, times=30, poll_frequency=0.5, doc=""):
        self.logger.info(f"等待元素{locator}可见")
        try:
            # 开始等待的时间
            start_time = time.time()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            time.sleep(5)
            # 结束等待的时间点
            end_time = time.time()
            # 求一个差值，写在日志里
            time_interval = (
                    datetime.datetime.fromtimestamp(end_time) - datetime.datetime.fromtimestamp(start_time)).seconds
            self.logger.info(f"等待时长为：{time_interval}")
        except:
            self.logger.info("等待元素可见失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # 等待元素存在
    def wait_elePresence(self, locator, times=30, poll_frequency=0.5, doc=""):
        self.logger.info(f"等待元素{locator}存在")
        try:
            # 开始等待的时间
            start_time = time.time()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待的时间点
            end_time = time.time()
            # 求一个差值，写在日志里
            time_interval = (
                    datetime.datetime.fromtimestamp(end_time) - datetime.datetime.fromtimestamp(start_time)).seconds
            self.logger.info(f"等待时长为：{time_interval}")
        except:
            self.logger.info("等待元素可见失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        self.logger.info(f"{doc}点击元素{locator}")
        # 元素操作
        try:
            ele.ckick()
        except:
            self.logger.info("元素点击操作失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=""):
        ele = self.get_element(locator, doc)
        # 输入操作
        try:
            ele.send_locators(text)
        except:
            self.logger.info("元素输入操作失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=""):
        ele = self.get_element(locator, doc)
        # 输入操作
        try:
            return ele.text
        except:
            self.logger.info("获取元素文本内容失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的属性
    def get_elment_attribute(self, locator, attr, doc=""):
        ele = self.get_element(locator, doc)
        # 输入操作
        try:
            return ele.get_attribute(attr)
        except:
            self.logger.info("获取元素的属性失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # 上滑
    def swipe_up(self, size):
        start_x = size["width"] * 0.5
        start_y = size["height"] * 0.9
        end_x = size["width"] * 0.5
        end_y = size["height"] * 0.1
        # 向上滑动:X轴不变，Y轴从大到小。
        self.driver.swipe(start_x, start_y, end_x, end_y)

    # 下滑
    def swipe_down(self, size):
        start_x = size["width"] * 0.5
        start_y = size["height"] * 0.1
        end_x = size["width"] * 0.5
        end_y = size["height"] * 0.9
        # 向下滑动:X轴不变，Y轴从小到大。
        self.driver.swipe(start_x, start_y, end_x, end_y)

    # 左滑
    def swipe_left(self, size):
        start_x = size["width"] * 0.9
        start_y = size["height"] * 0.5
        end_x = size["width"] * 0.1
        end_y = size["height"] * 0.5
        # 从右向左滑
        self.driver.swipe(start_x, start_y, end_x, end_y, 200)

    # 右滑
    def swipe_right(self, size):
        start_x = size["width"] * 0.9
        start_y = size["height"] * 0.5
        end_x = size["width"] * 0.1
        end_y = size["height"] * 0.5
        # 从左向右滑
        self.driver.swipe(end_x, end_y, start_x, start_y, 200)

    # 获取整个屏幕大小
    def get_size(self):
        return self.driver.get_window_size()

    # toast获取
    def get_toastMsg(self, text):
        # 1、xpath表达式 文本匹配
        locator = '//*[contains(@text,"{}")]'.format(text)
        # 等待的时候，要用元素存在的条件。不能用元素可见的条件
        try:
            self.wait_elePresence(locator)
            return self.get_element(locator).text
        except:
            self.logger.info("没有找到匹配的toast!!!!")
            raise

    # 截图
    def save_screenshot(self, name):
        time = datetime.datetime.now()
        # 图片名称+模块名+页面名称+操作名称+时间.png
        file_name = error_image + f"{name},{time}.png"
        self.driver.save_screenshot(file_name)
        self.logger.info(f"截取网页成功，文件路径为为：{file_name}")

    # 上传图片
    def upload_file(self, filepath):
        # 一级窗口
        dialog = win32gui.FindWindow("#32770", "打开")
        # 二级窗口
        comboxex32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        # 三级窗口
        combox = win32gui.FindWindowEx(comboxex32, 0, "ComboBox", None)
        # 四级窗口 文本输入框
        edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
        # 打开按钮 二级窗口
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开")
        # 输入文件路径
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)
        # 点击打开按钮 上传文件
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    # 点击坐标
    def touch(self, x, y, doc=""):
        try:
            self.logger.info(f"点击坐标{(x, y)}")
            TouchAction(self.driver).tap(x=x, y=y).perform()
        except:
            self.logger.info("点击坐标失败")
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入手机号
    def send_phone_number(self, number):

        for i in number:
            if i == "1":
                self.driver.keyevent(8)
            elif i == "2":
                self.driver.keyevent(9)
            elif i == "3":
                self.driver.keyevent(10)
            elif i == "4":
                self.driver.keyevent(11)
            elif i == "5":
                self.driver.keyevent(12)
            elif i == "6":
                self.driver.keyevent(13)
            elif i == "7":
                self.driver.keyevent(14)
            elif i == "8":
                self.driver.keyevent(15)
            elif i == "9":
                self.driver.keyevent(16)
            elif i == "0":
                self.driver.keyevent(7)

    # 输入密码
    def send_pwd(self):
        # 输入密码 默认qaz123
        self.driver.keyevent(45)
        self.driver.keyevent(29)
        self.driver.keyevent(54)
        self.driver.keyevent(8)
        self.driver.keyevent(9)
        self.driver.keyevent(10)

if __name__ == '__main__':
    pass
