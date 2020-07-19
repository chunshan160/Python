#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 17:17
# @Author :春衫
# @File :test_BuyGoods.py

from selenium import webdriver
from web_dev1.PageObjects.H5.Login_page import LoginPage
from web_dev1.TestData import Common_Data as CD
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from web_dev1.PageObjects.H5 import PublishGood_page as PG
import unittest
from web_dev1.TestData.H5 import Login_Data as LD, Publish_Data as PD
import ddt
from web_dev1.PageObjects.H5.SystemPoint_page import SystemPoint
from web_dev1.PageLocators.H5.PublishGood import Pubilc
from selenium.webdriver.common.action_chains import ActionChains
from web_dev1.PageLocators.H5.Index import Home
from web_dev1.PageObjects.H5.BuyGood_page import BuyGoods as BG
# from web_dev1.PageLocators.H5 import BuyGoods
import time
from web_dev1.PageObjects.H5.SystemPoint_page import SystemPoint as SP


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

    def tearDown(cls):
        cls.driver.get(CD.H5_home_url)
        # # 后置
        # cls.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDownClass整个测试类只执行一次==========")
        cls.driver.quit()

    # 购买实物商品-易贝支付
    def test_1_RealGoods(self):
        time.sleep(5)
        # 滚动至元素【实物商品】可见，点击【更多】
        ActionChains(self.driver).move_to_element(self.driver.find_element(*Home.real_goods_title)).perform()
        self.driver.execute_script('window.scrollBy(0,500)')
        self.driver.find_element(*Home.real_goods_more).click()
        time.sleep(2)
        # 点击【实物商品】
        self.driver.find_element(*Home.real_goods).click()
        time.sleep(2)
        # 购买流程
        BG.BuyGood(self)
        BG.Pay_yibei(self)
        BG.PayPassword(self)
        time.sleep(2)
        #断言
        # SP.Pay_Success(self)

    # 购买实物商品-易贝券支付
    def test_2_RealGoods(self):
        time.sleep(5)
        # 滚动至元素【实物商品】可见，点击【更多】
        ActionChains(self.driver).move_to_element(self.driver.find_element(*Home.real_goods_title)).perform()
        self.driver.execute_script('window.scrollBy(0,500)')
        self.driver.find_element(*Home.real_goods_more).click()
        time.sleep(2)
        # 点击【实物商品】
        self.driver.find_element(*Home.real_goods).click()
        time.sleep(2)
        # 购买流程
        BG.BuyGood(self)
        BG.Pay_yibeiquan(self)
        BG.PayPassword(self)
        time.sleep(2)

    # 购买实物商品-抵工资支付
    def test_3_RealGoods(self):
        time.sleep(5)
        # 滚动至元素【实物商品】可见，点击【更多】
        ActionChains(self.driver).move_to_element(self.driver.find_element(*Home.real_goods_title)).perform()
        self.driver.execute_script('window.scrollBy(0,500)')
        self.driver.find_element(*Home.real_goods_more).click()
        time.sleep(2)
        # 点击【实物商品】
        self.driver.find_element(*Home.real_goods).click()
        time.sleep(2)
        # 购买流程
        BG.BuyGood(self)
        BG.Pay_digongzi(self)
        BG.PayPassword(self)
        time.sleep(2)

    # 购买实物商品-家人购
    def test_4_RealGoods(self):
        time.sleep(5)
        # 滚动至元素【实物商品】可见，点击【更多】
        ActionChains(self.driver).move_to_element(self.driver.find_element(*Home.real_goods_title)).perform()
        self.driver.execute_script('window.scrollBy(0,500)')
        self.driver.find_element(*Home.real_goods_more).click()
        time.sleep(2)
        # 点击【实物商品】
        self.driver.find_element(*Home.real_goods).click()
        time.sleep(2)
        # 购买流程
        BG.BuyGood(self)
        BG.Pay_jiarengou(self)
        BG.PayPassword(self)
        time.sleep(2)

    # 购买实物商品-现金账户
    def test_5_RealGoods(self):
        time.sleep(5)
        # 滚动至元素【实物商品】可见，点击【更多】
        ActionChains(self.driver).move_to_element(self.driver.find_element(*Home.real_goods_title)).perform()
        self.driver.execute_script('window.scrollBy(0,500)')
        self.driver.find_element(*Home.real_goods_more).click()
        time.sleep(2)
        # 点击【实物商品】
        self.driver.find_element(*Home.real_goods).click()
        time.sleep(2)
        # 购买流程
        BG.BuyGood(self)
        BG.Pay_cash(self)
        BG.PayPassword(self)
        time.sleep(2)
