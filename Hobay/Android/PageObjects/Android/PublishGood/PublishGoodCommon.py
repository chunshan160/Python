#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/3 13:37
# @Author :春衫
# @File :PubilcGoodCommon.py

from Common.user_log import UserLog
from Android.PageLocators.Android.PubilcGood import PubilcGoodCommon as PGCommon
from Common.BasePage import BasePage


class PublishGoodCommon(BasePage):
    '''
    点击发布商品
    '''

    # 点击发布实物商品
    def publish_entity_good(self, text=""):
        doc = text + "点击发布实物商品-"
        self.click_element(PGCommon.entity_good, doc=doc)

    # 点击发布本地生活
    def publish_coupon_good(self, text=""):
        doc = text + "点击发布本地生活-"
        self.click_element(PGCommon.coupon_good, doc=doc)

    # 点击发布商企服务
    def publish_services_good(self, text=""):
        doc = text + "点击发布商企服务-"
        self.click_element(PGCommon.services_good, doc=doc)

    '''
    发布商品页面-公共部分
    '''

    '''
    上传主图
    '''

    # 上传商品主图
    def upload_product_image(self, text=""):
        doc = text + "点击【上传商品主图】-"
        self.wait_eleVisible(PGCommon.product_image, doc=doc)
        self.click_element(PGCommon.product_image, doc=doc)
        self.app_upload_image(PGCommon.check_image, PGCommon.btn_ok, doc=text)

    '''
    分类
    '''

    # 选择分类
    def category(self, text=""):
        doc = text + "点击【分类】选项-"
        self.click_element(PGCommon.category, doc=doc)

    # 选择二级分类
    def second_category(self, second_category_name, text=""):
        doc = text + f"点击【二级分类】-【{second_category_name}】选项-"
        new_locator = self.locator_by_text(PGCommon.second_category, second_category_name)
        self.click_element(new_locator, doc=doc)

    # 选择三级分类
    def third_category(self, third_category_name, text=""):
        doc = text + f"选择【三级分类】-【{third_category_name}】选项-"
        new_locator = self.locator_by_text(PGCommon.third_category, third_category_name)
        self.click_element(new_locator, doc=doc)

    '''
    限购
    '''

    # 限购
    def Purchase_limit(self, text=""):
        doc = text + "点击【限购】选项-"
        self.click_element(PGCommon.Purchase_limit, doc=doc)

    # 限购按钮控件
    def Purchase_limit_button(self, button, text=""):
        doc = text + f"点击【{button}】选项-"
        UserLog().info(f"点击【{button}】选项")
        if button == "不限购":
            self.click_element(PGCommon.Purchase_limit_no, doc=doc)
        elif button == "设置限购":
            self.click_element(PGCommon.Purchase_limit_yes, doc=doc)
        elif button == "无限期":
            self.click_element(PGCommon.Purchase_limit_no_day, doc=doc)
        else:
            self.click_element(PGCommon.Purchase_limit_yes_day, doc=doc)

    # 限购数量
    def limit_quantity(self, limit_quantity, text=""):
        doc = text + f"输入限购数量-"
        self.wait_eleVisible(PGCommon.limit_quantity, doc=doc)
        UserLog().info("输入的限购数量是:" + limit_quantity)
        self.input_text(PGCommon.limit_quantity, limit_quantity, doc=doc)

    # 限购周期
    def limit_time(self, limit_time, text=""):
        doc = text + f"输入限购周期【{limit_time}】-"
        self.wait_eleVisible(PGCommon.limit_time, doc=doc)
        UserLog().info("输入的限购周期是:" + limit_time)
        self.input_text(PGCommon.limit_time, limit_time, doc=doc)

    '''
    立即上架、放入仓库
    '''

    # 立即上架
    def submit(self, text=""):
        doc = text + "点击【立即上架】按钮-"
        self.click_element(PGCommon.submit, doc=doc)

    # 放入仓库
    def storage(self, text=""):
        doc = text + "点击【放入仓库】按钮-"
        self.click_element(PGCommon.storage, doc=doc)
