#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2019/12/25 12:54
#@Author :春衫
#@File :ceshi.py



class BuyGoods:

    def __init__(self, driver):
        self.driver = driver

    # 购买商品
    def BuyGood(self):
        # 立即购买
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.buy_now))).click()
        # 数量+1
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.add))).click()
        # 确定
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.determine))).click()
        # 提交订单
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((BG.submit_orders))).click()



