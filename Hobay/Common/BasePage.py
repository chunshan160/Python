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
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from Common.project_path import error_image
from Common.user_log import UserLog
from PageLocators.Android import Common


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 查找某个元素
    def get_element(self, locator, doc=""):
        try:
            by = locator[0]
            value = locator[1]
            UserLog().info("定位方式:by." + by + "--->定位值:" + value)
            return self.driver.find_element(*locator)
        except:
            UserLog().info("没有找到这个元素")
            # 截图
            self.save_screenshot(doc)
            raise

    # 查找多个元素
    def get_elements(self, locator, doc=""):
        try:
            by = locator[0]
            value = locator[1]
            UserLog().info("定位方式:by." + by + "--->定位值:" + value)
            return self.driver.find_elements(*locator)
        except:
            UserLog().info("没有找到这些元素")
            # 截图
            self.save_screenshot(doc)
            raise

    # 等待元素可见
    def wait_eleVisible(self, locator, times=30, poll_frequency=0.5, doc=""):
        try:
            UserLog().info(f"等待元素{locator}可见")
            # 开始等待的时间
            start_time = time.time()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待的时间点
            end_time = time.time()
            # 求一个差值，写在日志里
            time_interval = (
                    datetime.datetime.fromtimestamp(end_time) - datetime.datetime.fromtimestamp(start_time)).seconds
            UserLog().info(f"等待时长为：{time_interval}")
        except:
            UserLog().info("等待元素可见失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 等待元素存在
    def wait_elePresence(self, locator, times=30, poll_frequency=0.5, doc=""):
        try:
            UserLog().info(f"等待元素{locator}存在")
            # 开始等待的时间
            start_time = time.time()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.presence_of_element_located(locator))
            # 结束等待的时间点
            end_time = time.time()
            # 求一个差值，写在日志里
            time_interval = (
                    datetime.datetime.fromtimestamp(end_time) - datetime.datetime.fromtimestamp(start_time)).seconds
            UserLog().info(f"等待时长为：{time_interval}")
        except:
            UserLog().info("等待元素存在失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 等待元素可点击
    def wait_eleclickable(self, locator, times=30, poll_frequency=0.5, doc=""):
        try:
            UserLog().info(f"等待元素{locator}可点击")
            # 开始等待的时间
            start_time = time.time()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.element_to_be_clickable(locator))
            # 结束等待的时间点
            end_time = time.time()
            # 求一个差值，写在日志里
            time_interval = (
                    datetime.datetime.fromtimestamp(end_time) - datetime.datetime.fromtimestamp(start_time)).seconds
            UserLog().info(f"等待时长为：{time_interval}")
        except:
            UserLog().info("等待元素可点击失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=""):
        self.wait_eleVisible(locator, doc=doc)
        # 找元素
        ele = self.get_element(locator, doc)
        UserLog().info(f"{doc}点击元素{locator}")
        try:
            # 元素操作
            ele.click()
        except:
            UserLog().info("元素点击操作失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_elements(self, locator, index, doc=""):
        self.wait_eleVisible(locator, doc=doc)
        # 找元素
        ele = self.get_elements(locator, doc)[index]
        UserLog().info(f"{doc}点击元素{locator}")
        try:
            # 元素操作
            ele.click()
        except:
            UserLog().info("元素点击操作失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=""):
        self.wait_eleVisible(locator, doc=doc)
        ele = self.get_element(locator, doc)
        try:
            # 输入操作
            ele.send_keys(text)
        except:
            UserLog().info("元素输入操作失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=""):
        self.wait_eleVisible(locator, doc=doc)
        ele = self.get_element(locator, doc)
        UserLog().info(f"获取到的文本内容是：{ele.text}")
        # 输入操作
        try:
            return ele.text
        except:
            UserLog().info("获取元素文本内容失败!")
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
            UserLog().info("获取元素的属性失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 上滑
    def swipe_up(self, size, doc=""):
        try:
            start_x = size["width"] * 0.5
            start_y = size["height"] * 0.9
            end_x = size["width"] * 0.5
            end_y = size["height"] * 0.1
            UserLog().info(f"上滑：从({start_x, start_y})--->({end_x, end_y})")
            # 向上滑动:X轴不变，Y轴从大到小。
            self.driver.swipe(start_x, start_y, end_x, end_y, 200)
        except:
            UserLog().info("上滑失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 下滑
    def swipe_down(self, size, doc=""):
        try:
            start_x = size["width"] * 0.5
            start_y = size["height"] * 0.1
            end_x = size["width"] * 0.5
            end_y = size["height"] * 0.9
            UserLog().info(f"上滑：从({start_x, start_y})--->({end_x, end_y})")
            # 向下滑动:X轴不变，Y轴从小到大。
            self.driver.swipe(start_x, start_y, end_x, end_y, 200)
        except:
            UserLog().info("下滑失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 左滑
    def swipe_left(self, size, doc=""):
        try:
            start_x = size["width"] * 0.9
            start_y = size["height"] * 0.5
            end_x = size["width"] * 0.1
            end_y = size["height"] * 0.5
            # 左滑:Y轴不变，X轴从大到小。
            self.driver.swipe(start_x, start_y, end_x, end_y, 200)
        except:
            UserLog().info("左滑失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 右滑
    def swipe_right(self, size, doc=""):
        try:
            start_x = size["width"] * 0.1
            start_y = size["height"] * 0.5
            end_x = size["width"] * 0.9
            end_y = size["height"] * 0.5
            # 右滑:Y轴不变，X轴从小到大。
            self.driver.swipe(end_x, end_y, start_x, start_y, 200)
        except:
            UserLog().info("右滑失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取整个屏幕大小
    def get_size(self, doc=""):
        try:
            size = self.driver.get_window_size()
            UserLog().info(f"当前手机屏幕尺寸是：{size}")
            return size
        except:
            UserLog().info("获取屏幕大小失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # toast获取
    def get_toastMsg(self, text, doc=""):
        # 1、xpath表达式 文本匹配
        locator = '//*[contains(@text,"{}")]'.format(text)
        # 等待的时候，要用元素存在的条件。不能用元素可见的条件
        try:
            self.wait_elePresence(locator)
            return self.get_element(locator).text
        except:
            UserLog().info("没有找到匹配的toast!!!!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 截图
    def save_screenshot(self, name):
        time1 = datetime.datetime.now().strftime('%Y-%m-%d')
        time2 = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        # 图片名称+模块名+页面名称+操作名称+时间.png
        file_Path = error_image + f"\\{time1}"
        if not os.path.exists(file_Path):
            os.makedirs(file_Path)
        file_name = file_Path + f"\\{time2}-{name}.png"
        self.driver.save_screenshot(file_name)
        UserLog().info(f"截取网页成功，文件路径为为：{file_name}")

    # web上传图片
    def web_upload_image(self, filepath, doc=""):
        try:
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
        except:
            UserLog().info("Web上传图片失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # app上传图片
    def app_upload_image(self, choose_locator, ok_locator, doc=""):
        try:
            # 权限-始终允许
            time.sleep(1)
            if self.ele_if_exist(Common.always_allowed):
                self.click_element(Common.always_allowed, doc=doc)
            # 选择图片
            self.click_element(choose_locator)
            # 点击确定
            self.click_element(ok_locator)
        except:
            UserLog().info("上传图片失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 点击坐标
    def touch(self, x, y, doc=""):
        try:
            UserLog().info(f"点击坐标{(x, y)}")
            TouchAction(self.driver).tap(x=x, y=y).perform()
        except:
            UserLog().info("点击坐标失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入手机号
    def send_phone_number(self, number, text=""):
        doc = text + "输入手机号-"
        try:
            list = []
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
                list.append(str(i))
            num = "".join(list)
            UserLog().info(f"输入数字是{num}")
        except:
            UserLog().info("输入数字失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入密码
    def send_pwd(self, text=""):
        doc = text + "输入密码-"
        try:
            # 输入密码 默认qaz123
            self.driver.keyevent(45)
            self.driver.keyevent(29)
            self.driver.keyevent(54)
            self.driver.keyevent(8)
            self.driver.keyevent(9)
            self.driver.keyevent(10)
        except:
            UserLog().info("输入密码失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入支付密码
    def pay_password(self, text=""):
        doc = text + "输入支付密码-"
        try:
            self.driver.keyevent(8)
            self.driver.keyevent(9)
            self.driver.keyevent(10)
            self.driver.keyevent(11)
            self.driver.keyevent(12)
            self.driver.keyevent(13)
        except:
            UserLog().info("输入支付密码失败!")
            # 截图
            self.save_screenshot(doc)
            raise

    # 判断元素是否存在
    def ele_if_exist(self, locator):
        try:
            self.driver.find_element(*locator)
            UserLog().info(f"元素{locator}存在")
            return True
        except:
            UserLog().info(f"元素{locator}不存在")
            return False

    # 匹配文本来处理表达式
    def locator_by_text(self, locator, name):
        new_locator = (locator[0], locator[1].format(name))
        return new_locator


if __name__ == '__main__':
    pass
