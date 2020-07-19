#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 17:17
# @Author :春衫
# @File :test_buygoods.py

from selenium import webdriver
from web_test2.PageObjects.H5.Login_page import LoginPage
from web_test2.TestData import Common_Data as CD
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from web_test2.PageObjects.H5 import PublishGoods_page as PG
import unittest
from web_test2.TestData.H5 import Login_Data as LD, Publish_Data as PD
import ddt
from web_test2.PageObjects.H5.SystemPoint_page import SystemPoint
from web_test2.PageLocators.H5.PublishGoods import Pubilc
from selenium.webdriver.common.action_chains import ActionChains
from web_test2.PageLocators.H5.Home import Home
from web_test2.PageObjects.H5.BuyGoods_page import BuyGoods
from web_test2.PageLocators.H5.BuyGoods import BuyGoods as BG
import time


@ddt.ddt
class BuyGoods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 用setUpClass就能只打开浏览器一次，setUp则是每条用例都执行一次
        print("=======所有测试用例执行之前，setUpClass整个测试类只执行一次==========")
        mobile_emulation = {'deviceName': 'iPhone X'}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get(CD.H5_Login_url)
        cls.lg = LoginPage(cls.driver)
        cls.pp = PG.Product(cls.driver)
        cls.lg.login(LD.Success_data["username"], LD.Success_data["password"])


    def setUp(cls):
        time.sleep(3)
        # 滚动至元素【本地生活】可见，点击【更多】
        ActionChains(cls.driver).move_to_element(cls.driver.find_element(*Home.local_life_title)).perform()
        cls.driver.execute_script('window.scrollBy(0,500)')
        cls.driver.find_element(*Home.local_life_more).click()
        time.sleep(2)

    def tearDown(cls):
        cls.driver.get(CD.H5_home_url)
        # # 后置
        # cls.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDownClass整个测试类只执行一次==========")
        cls.driver.quit()

    # 购买本地生活
    def test_1_LocalLife(self):
        # 点击【本地生活】
        self.driver.find_element(*Home.local_life_goods).click()
        time.sleep(6)
        # 购买流程
        # 立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        time.sleep(1)
        # 数量+1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.add))).click()
        # 确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        # 提交订单--支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()
        # 确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()
        # 支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_1))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_2))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_3))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_4))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_5))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_6))).click()
        time.sleep(2)

    # 购买本地生活
    def test_2_LocalLife(self):
        # 点击【本地生活】
        self.driver.find_element(*Home.local_life_goods).click()
        time.sleep(6)
        # 购买流程
        # 立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        time.sleep(1)
        # 数量+1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.add))).click()
        # 确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        # 提交订单--支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()
        # 点击更换支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
        time.sleep(2)
        # 选择支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.yibeiquan))).click()
        time.sleep(1)
        # 确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()
        # 支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_1))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_2))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_3))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_4))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_5))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_6))).click()
        time.sleep(2)

    # 购买本地生活
    def test_3_LocalLife(self):
        # 点击【本地生活】
        self.driver.find_element(*Home.local_life_goods).click()
        time.sleep(6)
        # 购买流程
        # 立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        time.sleep(1)
        # 数量+1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.add))).click()
        # 确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        # 提交订单--支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()
        # 点击更换支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
        time.sleep(1)
        # 选择支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.digongzi))).click()
        time.sleep(3)
        # 确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()
        # 支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_1))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_2))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_3))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_4))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_5))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_6))).click()
        time.sleep(2)

    # 购买本地生活
    def test_4_LocalLife(self):
        # 点击【本地生活】
        self.driver.find_element(*Home.local_life_goods).click()
        time.sleep(6)
        # 购买流程
        # 立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        time.sleep(1)
        # 数量+1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.add))).click()
        # 确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        # 提交订单--支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()
        # 点击更换支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
        time.sleep(1)
        # 选择支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.jiarengou))).click()
        time.sleep(2)
        # 确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()
        # 支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_1))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_2))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_3))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_4))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_5))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_6))).click()
        time.sleep(2)

    # 购买本地生活
    def test_5_LocalLife(self):
        # 点击【本地生活】
        self.driver.find_element(*Home.local_life_goods).click()
        time.sleep(6)
        # 购买流程
        # 立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        time.sleep(1)
        # 数量+1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.add))).click()
        # 确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        # 提交订单--支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()
        # 点击更换支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
        time.sleep(1)
        # 选择支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.xianjinzhanghu))).click()
        time.sleep(1)
        # 确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()
        # 支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_1))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_2))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_3))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_4))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_5))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_6))).click()
        time.sleep(2)
