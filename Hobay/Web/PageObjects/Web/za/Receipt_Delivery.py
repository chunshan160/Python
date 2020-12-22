#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/7 15:19
#@Author :春衫
#@File :Receipt_Delivery.py

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Web.PageLocators import MyIndex
from Handle.za.H5_Login_page2 import H5_LoginPage
from Handle.H5.za.BuyGood_page import BuyGoods
from Common.fengyong.ReturnTxt import ReturnTxt
from Web.PageLocators import BuyGoods as BG


class ReceiptDelivery:

    def __init__(self,driver):
        self.driver=driver

    def entity_good(self,H5_Login_url,buyer_phone):
        # 发货
        self.driver.find_element(*MyIndex.ship).click()
        time.sleep(2)
        self.driver.find_element(*MyIndex.logistics_company).click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((MyIndex.debang))).click()
        time.sleep(2)
        self.driver.find_element(*MyIndex.dingdanhao).send_keys("lalalalala")
        time.sleep(2)
        self.driver.find_element(*MyIndex.ship_now).click()
        time.sleep(2)

        # 买家
        self.driver.get(H5_Login_url)
        lg = H5_LoginPage(self.driver)
        lg.login(buyer_phone)
        time.sleep(2)
        # 点击【采购订单】
        self.driver.find_element(*MyIndex.purchase).click()
        time.sleep(4)
        # 收货
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((MyIndex.receipt))).click()
        time.sleep(3)

        # 支付按键
        BuyGoods(self.driver).pay()
        time.sleep(2)

    def coupon_good(self,H5_Login_url,H5_home_url,buyer_phone,seller_phone):
        # 本地生活
        self.driver.get(H5_Login_url)
        lg = H5_LoginPage(self.driver)
        lg.login(buyer_phone)
        time.sleep(2)
        self.driver.get(H5_home_url)
        time.sleep(2)
        self.driver.find_element(*MyIndex.myIndex).click()
        time.sleep(2)
        # 点击【采购订单】
        self.driver.find_element(*MyIndex.purchase).click()
        time.sleep(4)
        # 点击第一个订单
        self.driver.find_element(*BG.frist_order).click()
        time.sleep(2)
        xuliehao = ReturnTxt(self.driver).xuliehao_txt()
        # print(xuliehao)

        time.sleep(2)

        # 卖家
        self.driver.get(H5_Login_url)
        lg = H5_LoginPage(self.driver)
        lg.login(seller_phone)
        time.sleep(2)
        self.driver.get(H5_home_url)
        time.sleep(2)
        self.driver.find_element(*MyIndex.myIndex).click()
        time.sleep(2)
        # 滚动至元素【销售订单】可见，点击
        ActionChains(self.driver).move_to_element(self.driver.find_element(*MyIndex.saleOrderList)).perform()
        self.driver.execute_script('window.scrollBy(0,500)')
        time.sleep(2)
        self.driver.find_element(*MyIndex.saleOrderList).click()
        time.sleep(5)
        # 点击第一个订单
        self.driver.find_element(*BG.frist_order).click()
        time.sleep(2)
        # 输入序列号
        self.driver.find_element(*BG.click_xuliehao).send_keys(xuliehao)
        # 点击确定
        self.driver.find_element(*BG.click_queding).click()
        time.sleep(1)
        self.driver.find_element(*BG.click_queding2).click()
        time.sleep(2)

    def Business_Services(self,H5_Login_url,buyer_phone):
        # 买家
        self.driver.get(H5_Login_url)
        lg = H5_LoginPage(self.driver)
        lg.login(buyer_phone)
        time.sleep(3)
        # 点击【采购订单】
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((MyIndex.purchase))).click()
        time.sleep(4)

        # 确认签约
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.qianyue))).click()

        # 支付按键
        BuyGoods(self.driver).pay()
        time.sleep(2)