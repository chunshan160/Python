#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 17:17
# @Author :春衫
# @File :test_BuyGoods.py

from selenium import webdriver
from Handle.H5.za.Login_page import LoginPage
from TestData import Common_Data as CD
from Handle.H5 import PublishGood as PG
import unittest
from TestData.H5 import Login_Data as LD
import ddt
from selenium.webdriver.common.action_chains import ActionChains
from PageLocators.H5 import Home
from Handle.H5.za.BuyGood_page import BuyGoods as BG
# from PageLocators.H5 import BuyGoods
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
        cls.pp = PG.PublishGood(cls.driver)
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
    def test_1_EntityGood(self,payment_method):
        time.sleep(5)
        # 滚动至元素【实物商品】可见，点击【更多】
        ActionChains(self.driver).move_to_element(self.driver.find_element(*Home.entity_good_title)).perform()
        self.driver.execute_script('window.scrollBy(0,500)')
        self.driver.find_element(*Home.entity_good_more).click()
        time.sleep(2)
        # 点击【实物商品】
        self.driver.find_element(*Home.entity_good).click()
        time.sleep(2)
        # 购买流程
        BG.BuyGood(self,payment_method)
        time.sleep(2)
        #断言
        # SP.Pay_Success(self)


if __name__ == '__main__':
    for i in ["易贝","易贝券","抵工资","家人购","现金账户"]:
        BuyGoods().test_1_EntityGood(i)