#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 15:49
# @Author :春衫
# @File :BuyGood_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_test2.PageLocators.H5.BuyGoods import BuyGoods as BG
import time

class BuyGoods:

    def __init__(self, driver):
        self.driver = driver

    # 购买商品
    def BuyGood(self):
        # 立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        time.sleep(1)
        # 数量+1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.add))).click()
        # 确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        # 提交订单
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()

    #   易贝支付
    def Pay_yibei(self):
        # 确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()

    # 支付按键
    def PayPassword(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_1))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_2))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_3))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_1))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_2))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.pay_3))).click()

    # 购买商品-易贝券支付
    def Pay_yibeiquan(self):
        # 点击更换支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
        # 选择支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.yibeiquan))).click()
        # 确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()

    # 购买商品-抵工资支付
    def Pay_digongzi(self):
        # 点击更换支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
        # 选择支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.digongzi))).click()
        # 确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()

    # 购买商品-家人购支付
    def Pay_jiarengou(self):
        # 点击更换支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
        # 选择支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.jiarengou))).click()
        # 确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()

    # 购买商品-现金账户支付
    def Pay_cash(self):
        # 点击更换支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.payment_method))).click()
        # 选择支付方式
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.xianjinzhanghu))).click()
        # 确认支付
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.confirm_payment))).click()
