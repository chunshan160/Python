#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 17:17
# @Author :春衫
# @File :test_BuyGoods.py

from selenium import webdriver
from Handle.H5.za.Login_page2 import LoginPage
from Web.TestData.Web import Common_Data as CD
from Handle.H5 import PublishGood as PG
import unittest
from TestData.H5 import Login_Data as LD
import ddt
from Web.PageLocators import Home
from Handle.H5.za.BuyGood_page import BuyGoods as BG
# from PageLocators.TestCases import BuyGoods
import time
from selenium.webdriver.common.keys import Keys


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
        cls.pp = PG.PublishGood(cls.driver)
        cls.lg.login(LD.login_data["公海用户"])

    # 购买实物商品-易贝支付
    def test_1_EntityGood(self):
        time.sleep(2)
        self.driver.find_element(*Home.search).click()
        time.sleep(2)
        self.driver.find_element(*Home.input).send_keys("普通焕商实物商品")
        time.sleep(2)
        self.driver.find_element(*Home.input).send_keys(Keys.ENTER)
        time.sleep(3)
        # 点击【商品】
        self.driver.find_element(*Home.entity_good).click()
        time.sleep(2)
        # 购买流程
        BG.BuyGood(self, "易贝")
        time.sleep(2)
        # 断言
        # SP.Pay_Success(self)

    # 购买实物商品-易贝券支付
    def test_2_EntityGood(self):
        time.sleep(2)
        self.driver.find_element(*Home.search).click()
        time.sleep(2)
        self.driver.find_element(*Home.input).send_keys("普通焕商实物商品")
        time.sleep(2)
        self.driver.find_element(*Home.input).send_keys(Keys.ENTER)
        time.sleep(3)
        # 点击【商品】
        self.driver.find_element(*Home.entity_good).click()
        time.sleep(2)
        # 购买流程
        BG.BuyGood(self, "易贝券")
        time.sleep(2)

    # 购买实物商品-抵工资支付
    def test_3_EntityGood(self):
        time.sleep(2)
        self.driver.find_element(*Home.search).click()
        time.sleep(2)
        self.driver.find_element(*Home.input).send_keys("普通焕商实物商品")
        time.sleep(2)
        self.driver.find_element(*Home.input).send_keys(Keys.ENTER)
        time.sleep(3)
        # 点击【商品】
        self.driver.find_element(*Home.entity_good).click()
        time.sleep(2)
        # 购买流程
        BG.BuyGood(self, "抵工资")
        time.sleep(2)

    # 购买实物商品-家人购
    def test_4_EntityGood(self):
        time.sleep(2)
        self.driver.find_element(*Home.search).click()
        time.sleep(2)
        self.driver.find_element(*Home.input).send_keys("普通焕商实物商品")
        time.sleep(2)
        self.driver.find_element(*Home.input).send_keys(Keys.ENTER)
        time.sleep(3)
        # 点击【商品】
        self.driver.find_element(*Home.entity_good).click()
        time.sleep(2)
        # 购买流程
        BG.BuyGood(self, "家人购")
        time.sleep(2)

    # 购买实物商品-现金账户
    def test_5_EntityGood(self):
        time.sleep(2)
        self.driver.find_element(*Home.search).click()
        time.sleep(2)
        self.driver.find_element(*Home.input).send_keys("普通焕商实物商品")
        time.sleep(2)
        self.driver.find_element(*Home.input).send_keys(Keys.ENTER)
        time.sleep(3)
        # 点击【商品】
        self.driver.find_element(*Home.entity_good).click()
        time.sleep(2)
        # 购买流程
        BG.BuyGood(self, "现金账户")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDownClass整个测试类只执行一次==========")
        cls.driver.quit()

    def tearDown(cls):
        cls.driver.get(CD.H5_home_url)
        # # 后置
        # cls.driver.refresh()
