#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/25 20:44
# @Author :春衫
# @File :learn.py

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# xpath-定位-函数和逻辑

# 函数使用:
# 1、text():元素的text内容
# 例: //p[text()="XXXX"]

# 2、contains(@属性/text(),value):包含函数。
# 例: contains(@class,"XXXX")、 contains(text(),"XXXX")

# 逻辑运算:
# and 表示条件 与。
# or 表示条件 或。
# 例: //div[@class="XXX" and contains(@style,"displayvisibility*")]
# 应用场景:
# 一个页面的几个操作，都会有弹出框出现。定位到弹出框会有几个。
# 但通过display的值来定位到当前显示的那-一个。


# xpath-轴定位语法

# 轴运算:
# ancestor:祖先结点 包括父
# parent:父结点
# preceding:当前元素节点标签之前的所有结点。(html页面先后顺序)
# preceding-sibling:当前元素节点标签之前的所有兄弟结点
# following:当前元索节点标签之后的所有结点。(html页面先后顺序)
# following-sibling:当前元素节点标签之后的所有兄弟结点。

# 使用语法:
# /轴名称::节点名称
# 例: /iv//tble//td//preceding::td
# 较多的应用场景:
# 页面显示为一个表格样式的数据列。需要通过组合来定位元素

# 等待-三种等待方式
# 1、强制等待
# sleep(秒)
# 2、隐性等待
# implicitly_wait(秒)
# 设置最长等待时间，在这个时间内加载完成，则执行下一一步。
# 整个drvier的会话周期内，设置一次即可，全局都可用。


# 3、显性等待
# 明确等到某个条件满足之后，再去执行下一步操作。
# 程序每隔xx秒看-一眼，如果条件成立了，则执行下一步，否则继续等待，直到
# 超过设置的最长时间，然后抛出TimeoutException。

# WebDriverWait类:显性等待类。
# WebDriverWait(driver,等待时长,轮循周期).until()/until_not()
# 轮循周期 默认0.5S


# expected_conditions模块: 提供了一系列期望发生的条件。
# presence_of_element_located:元素存在
# visibility_of_element_located: 元素可见
# element_to_be_clickable:元素可点击
# ps:这个类多有很判断方法。具体自行了解。


# driver = webdriver.Chrome()
# # 切换一 iframe
# # 切换iframe =进入了另外一个html
# # 等待iframe存在，可见
# driver.switch_to.frame("login_frame_qq")
# driver.switch_to.frame(driver.find_element_by_xpath('//iframe [@name="login_frame_qq"]'))
# time.sleep(0.5)
# driver.find_element_by_id("switcher_plogin")
#
# # 方式二: iframe切换
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))
#
# # 从iframe当中回到默认的页面当中。
# driver.switch_to.default_content()
#
# # 回到父级页面
# driver.switch_to.parent_frame()
#
# # 切换二 窗口切换
# # step1:获取窗口的总数以及句柄 新打开的窗口，位于最后一个。
# handles = driver.window_handles  # 窗口数=2
# print(handles)
# # 当前窗口的句柄
# print(driver.current_window_handle)
#
# # 打开新窗口
#
# # 等待新的窗口出现
# # new_window_is_opened 会自动获取最新的窗口数 和旧的进行对比
# WebDriverWait(driver, 10).until(EC.new_window_is_opened(handles))
#
# # 重新获取一次窗口
# handles = driver.window_handles  # 窗口数=3
# # 切换最新打开的窗口
# # step2:切换
# driver.switch_to.window(handles[-1])
#
# # 弹出框处理
# # 弹出框有两种:
# # 1、页面弹出框
# # 2、windows弹出框
# # 页面弹出框:
#
# # 原理:
# # 等待弹出框出现之后，再定位弹出框，再去操作弹出框里的元素。
# # 例:百度登陆的弹出框
#
# # Alert弹出框:
# # 1、使用switch_to方法先切换到windows弹出框。
# # driver.switch_to.alert
#
# # 2、Alert类提供了一系列的操作方法。
# # dismiss():否。
# # accept():是。
# # text():获取弹出框里的内容。
#
# # 弹出框可见
# WebDriverWait(driver, 10).until(EC.alert_is_present())
# # alert切换  不是html页面元素
# alert = driver.switch_to.alert
# # 打印弹出框内容
# print(alert.text)
# # 关闭弹出框
# alert.accept()
#
# # 鼠标操作
# # 由selenium的ActionChains类来完成模拟鼠标操作。
#
# # 主要操作流程:
# # 1、存储鼠标操作。
# # 2、perform()来执行鼠标操作。
#
# # 支持的操作如下:
# # double_click 双击操作
# # context_click 右键操作
# # drag_and_drop 拖拽操作。左键按住拖动某一个元素到另外一个区域，然后释放按键
# # move_to_element() 鼠标悬停。
# # perform()
#
# # 引入ActionChains类:
# from selenium.webdriver.common.action_chains import ActionChains
#
# # AC.方法名1().context_click().perform()
#
#
# # 1、先找到鼠标要操作的元素
# ele = driver.find_element_by_id("switcher_plogin")
# # 2、实例化
# ac = ActionChains(driver)
# # 3、将鼠标操作添加到ActionChains列表中 悬停
# ac.move_to_element(ele)
# # 4、调用perfrom()来执行鼠标操作
# ac.perform()
# #
# ActionChains(driver).move_to_element(ele).perform()
#
# # 下拉框操作
# # 观察下拉框页面元素。是否为select/option。
# # 1、菜单栏-点击其中的某个链接跳转。
# # 2、在下拉列表中选择一个值。
#
# # 思路:
# # 1、等待下拉列表和下拉列表中值存在
# # 2、对下拉列表中的元素进行操作
#
# # 两种方式:
# # 一、获取所有的下拉列表值，然后用循环去匹配相同的值。
# # 二、通过text的内容来找到下拉列表的某个值
#
# # Select类-下拉框操作
# # selenium提供了Select类来处理select/option
# # 引入类:
# from selenium.webdriver.support.ui import Select
#
# # 选择下拉列表值:
# # 1、通过下标选择: select_by_index(index) 从0开始;
# # 2、通过value属性: select_by_value(value值)
# # 3、通过文本内容: select_by_visible_text(文本内容)
#
# select_ele = driver.find_element_by_xpath('//select[@name=”ft"]')
# # 2、实例化Select类
# s = Select(select_ele)
#
# # 3、 选择下拉列表值
# # 方式-:下标从0开始
# s.select_by_index(4)
# # 方式二: value值
# s.select_by_value(" all")
# # 方式三: 文本内容
# s.select_by_visible_text('Adobe Acrobat PDF (. pdf)')
#
# driver.find_element_by_xpath("").get_attribute("")
#
#
# #移动
# # 1、移动到元素element对象的"底端”与当前窗口的“底部”对齐:
# # driver.execute_script("arguments[0].scrollIntoView(false);",element)
# # 2、移动到元素element对象的"顶端”与当前窗口的"顶部” 对齐: .
# # driver.execute_script("arguments[0].scrollIntoView();',element)
# # 3、移动到页面底部:
# # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# # 4、移动到页面顶部:
# # driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
#
#
# #js语句
# js ='var ele = document.getElementById("train_date");ele.readOnly = false;ele.value = "2018-12-30";'
# driver.execute_script(js)
#
#
# # 上传操作
# # 有两种情况:
# # 1、如果是input可以直接输入路径的，那么直接调send_keys输入路径
#
# # 2、非input标签的上传，则需要借助第三方工具:
# # 2.1 Autolt 我们去调用其生成的au3或exe文件。
# # 2.2 SendKeys第三方库(目前只支持到2.7版本)
# # 网址: https://pypi.python.org/pypi/SendKeys
# # 2.3 Python pywin32库，识别对话框句柄，进而操作
# #pyautoit
#
# # 工具:
# # pywin32和spy++
