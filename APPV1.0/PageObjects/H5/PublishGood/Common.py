#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/3 13:37
# @Author :春衫
# @File :PubilcGoodCommon.py

import time
from PageLocators.H5.PubilcGood import PubilcGoodCommon
from Common.BasePage import BasePage

class PublishGoodCommon(BasePage):

    # 立即上架
    def submit(self,text=""):
        doc=text+"点击【立即上架】按钮-"
        time.sleep(0.5)
        self.click_element(PubilcGoodCommon.submit, doc=doc)

    # 放入仓库
    def storage(self,text=""):
        doc=text+"点击【放入仓库】按钮-"
        time.sleep(0.5)
        self.click_element(PubilcGoodCommon.storage, doc=doc)

    # 点击发布实物商品
    def publish_entity_good(self):
        doc=""
        time.sleep(0.5)
        self.click_element(PubilcGoodCommon.entity_good, doc=doc)

    # 点击发布本地生活
    def publish_coupon_good(self):
        doc=""
        time.sleep(0.5)
        self.click_element(PubilcGoodCommon.coupon_good, doc=doc)

    # 点击发布商企服务
    def publish_services_good(self):
        doc=""
        time.sleep(0.5)
        self.click_element(PubilcGoodCommon.services_good, doc=doc)