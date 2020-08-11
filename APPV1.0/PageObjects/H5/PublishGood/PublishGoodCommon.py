#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/3 13:37
# @Author :春衫
# @File :PubilcGoodCommon.py

import time
from PageLocators.H5.PubilcGood import PubilcGoodCommon as PGCommon
from Common.BasePage import BasePage

class PublishGoodCommon(BasePage):

    '''
    点击发布商品
    '''

    # 点击发布实物商品
    def publish_entity_good(self):
        doc = ""
        self.wait_eleVisible(PGCommon.entity_good, doc=doc)
        self.click_element(PGCommon.entity_good, doc=doc)

    # 点击发布本地生活
    def publish_coupon_good(self):
        doc = ""
        self.wait_eleVisible(PGCommon.coupon_good, doc=doc)
        self.click_element(PGCommon.coupon_good, doc=doc)

    # 点击发布商企服务
    def publish_services_good(self):
        doc = ""
        self.wait_eleVisible(PGCommon.services_good, doc=doc)
        self.click_element(PGCommon.services_good, doc=doc)

    '''
    发布商品页面-公共部分
    '''

    # 选择分类
    def category(self, text=""):
        doc = text + "点击【分类】选项-"
        self.wait_eleVisible(PGCommon.category, doc=doc)
        self.click_element(PGCommon.category, doc=doc)

    # 选择二级分类
    def second_category(self, second_category_name, text=""):
        doc = text + f"点击【二级分类】-【{second_category_name}】选项-"
        new_locator = self.locator_by_text(PGCommon.second_category, second_category_name, text=doc)
        self.wait_eleVisible(new_locator, doc=doc)
        self.click_element(new_locator, doc=doc)

    # 选择三级分类
    def third_category(self, third_category_name, text=""):
        doc = text + f"选择【三级分类】-【{third_category_name}】选项-"
        new_locator = self.locator_by_text(PGCommon.third_category, third_category_name, text=doc)
        self.wait_eleVisible(new_locator, doc=doc)
        self.click_element(new_locator, doc=doc)

    # 立即上架
    def submit(self,text=""):
        doc=text+"点击【立即上架】按钮-"
        self.wait_eleVisible(PGCommon.submit, doc=doc)
        self.click_element(PGCommon.submit, doc=doc)

    # 放入仓库
    def storage(self,text=""):
        doc=text+"点击【放入仓库】按钮-"
        self.wait_eleVisible(PGCommon.storage, doc=doc)
        self.click_element(PGCommon.storage, doc=doc)

