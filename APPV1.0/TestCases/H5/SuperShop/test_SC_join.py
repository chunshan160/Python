#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/15 16:12
#@Author :春衫
#@File :test_SC_join.py

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Handle.H5.za.Login_page2 import LoginPage
from TestData import Common_Data as CD
from Handle.H5 import PublishGood as PG
import unittest
from TestData.H5 import Login_Data as LD
import ddt
from TestData.H5 import Publish_Data as PD
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.H5 import Pubilc
import time
from Handle.H5 import SystemPoint

@ddt.ddt
class ShangChao(unittest.TestCase):

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
        cls.driver.get(CD.H5_publishGood_url)
        # 后置
        cls.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDownClass整个测试类只执行一次==========")
        cls.driver.quit()

    # 发布实物商品，立即上架
    @ddt.data(*PD.EntityGood_data)
    def test_1_EntityGood_submit(cls, data):
        # 点击发布实物商品
        WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((Pubilc.entity_good))).click()
        cls.pp.EntityGood(data["product_title"], data["product_description"], data["property_1"],
                          data["property_2"], data["purchase_price"], data["sell_price"], data["stock"],
                          data["limit_quantity"])
        # 立即上架
        cls.pp.submit(Pubilc.submit)
        time.sleep(1)
        # 断言 在[系统提示]中，存在[完成] 这个元素   存在，就ok，不存在就报错
        cls.assertTrue(SystemPoint(cls.driver).Perfection())