#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/3 17:17
#@Author :春衫
#@File :test_buygoods.py

from selenium import webdriver
from PageObjects.H5.Login_page import LoginPage
from TestData import Common_Data as CD
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.H5 import PublishGoods_page as PG
import unittest
from TestData.H5 import Login_Data as LD, Publish_Data as PD
import ddt
from PageObjects.H5.SystemPoint_page import SystemPoint
from PageLocators.H5.PublishGoods import Pubilc
from selenium.webdriver.common.action_chains import ActionChains


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
        cls.driver.get(CD.H5_RealGoods_url)
        # 后置
        cls.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDownClass整个测试类只执行一次==========")
        cls.driver.quit()

    # 购买实物商品
    def test_1_RealGoods_submit(cls, data):
        # 滚动至元素【实物商品】可见
        ActionChains(self.driver).move_to_element(self.driver.find_element(*CK.check_refuse)).click(
            self.driver.find_element(*CK.check_refuse)).perform()
        # 点击【实物商品】
        WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((Pubilc.real_goods))).click()
        cls.pp.Real_Goods(data["product_title"], data["product_description"], data["property_1"],
                          data["property_2"], data["purchase_price"], data["sell_price"], data["stock"],
                          data["limit_quantity"])
        # 立即上架
        cls.pp.submit(Pubilc.submit)
        # 断言 在[系统提示]中，存在[完成] 这个元素   存在，就ok，不存在就报错
        cls.assertTrue(SystemPoint(cls.driver).Perfection())