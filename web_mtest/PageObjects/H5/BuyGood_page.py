#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 15:49
# @Author :春衫
# @File :BuyGood_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_mtest.PageLocators.H5.BuyGoods import BuyGoods as BG
import time

class BuyGoods:

    def __init__(self, driver):
        self.driver = driver

    # 购买商品
    def BuyGood(self,payment_method):
        # 立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        time.sleep(1)
        # 数量+1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.add))).click()
        # 确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        time.sleep(3)
        # 提交订单
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()

        if payment_method !="易贝":
            # 点击更换支付方式
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
            time.sleep(1)

            if payment_method =="易贝券":
                # 选择支付方式
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.yibeiquan))).click()


            elif payment_method =="抵工资":
                # 选择支付方式
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.digongzi))).click()


            elif payment_method == "家人购":
                # 选择支付方式
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.jiarengou))).click()


            elif payment_method == "现金账户":
                # 选择支付方式
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.xianjinzhanghu))).click()

        # 确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()
        time.sleep(1)
        # 支付按键
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_1))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_2))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_3))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_4))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_5))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_6))).click()

