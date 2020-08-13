#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/10 17:21
# @Author :春衫
# @File :test_publish_good.py

import pytest
import allure
from PageObjects.Comm_Bus import CommBus
from TestData.H5.Publish_Data import *
from PageObjects.H5.PublishGood.PublishGoodCommon import PublishGoodCommon
from PageObjects.H5.PublishGood.EntityGood_Page import EntityGoodPage
from PageObjects.H5.PublishGood.CouponGood_Page import CouponGoodPage
from PageObjects.H5.PublishGood.ServerGood_Page import ServicesGoodPage
from Common.BasePage import BasePage
from PageLocators.H5.SystemPoint import PublishGoodOK as PGOK
from Common.project_path import *


@allure.feature('发布商品功能')
class TestPublishGood:

    # @allure.story("发布实物商品")
    # @pytest.mark.smoke
    # @pytest.mark.usefixtures("open_app")
    # @pytest.mark.parametrize("data", EntityGood_data)  # 替代ddt
    # def test_1_publish_entity_good(self, open_app, data):
    #     doc = "测试发布实物商品-"
    #     with allure.step("首页点击发布商品"):
    #         CommBus(open_app).click_publish_good(text=doc)
    #     with allure.step("选择发布实物商品"):
    #         PublishGoodCommon(open_app).publish_entity_good(text=doc)
    #     with allure.step("发布实物商品"):
    #         EntityGoodPage(open_app).entity_good_information(data["product_title"], data["product_description"],
    #                                                          data["quality_name"], data["product_type"],
    #                                                          data["second_category_name"], data["third_category_name"],
    #                                                          data["property_1"], data["property_2"],
    #                                                          data["purchase_price"], data["sell_price"],
    #                                                          data["stock"], data["fare"],text=doc)
    #     with allure.step("立即上架"):
    #         PublishGoodCommon(open_app).submit(text=doc)
    #     with allure.step("断言：立即上架后系统提示商品审核中"):
    #         text = BasePage(open_app).get_text(PGOK.good_audit_text, doc=doc)
    #         assert text == "商品审核中"
    #
    # @allure.story("发布本地生活商品")
    # @pytest.mark.smoke
    # @pytest.mark.usefixtures("open_app")
    # @pytest.mark.parametrize("data", CouponGood_data)  # 替代ddt
    # def test_2_publish_coupon_good(self, open_app, data):
    #     doc = "测试发布本地生活商品-"
    #     with allure.step("首页点击发布商品"):
    #         CommBus(open_app).click_publish_good()
    #     with allure.step("选择发布本地生活商品"):
    #         PublishGoodCommon(open_app).publish_coupon_good()
    #     with allure.step("发布本地生活商品"):
    #         CouponGoodPage(open_app).coupon_good_information(data["product_title"], data["product_description"],
    #                                                          data["second_category_name"], data["third_category_name"],
    #                                                          data["category_type"],
    #                                                          data["total_price"], data["stock"], text=doc)
    #     with allure.step("立即上架"):
    #         PublishGoodCommon(open_app).submit()
    #     with allure.step("断言：立即上架后系统提示商品审核中"):
    #         text = BasePage(open_app).get_text(PGOK.good_audit_text, doc=doc)
    #         assert text == "商品审核中"

    @allure.story("发布商企服务商品")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("open_app")
    @pytest.mark.parametrize("data", ServerGood_data)  # 替代ddt
    def test_3_publish_services_good(self, open_app, data):
        doc = "测试发布商企服务商品-"
        with allure.step("首页点击发布商品"):
            CommBus(open_app).click_publish_good()
        with allure.step("选择发布商企服务商品"):
            PublishGoodCommon(open_app).publish_services_good()
        with allure.step("发布商企服务商品"):
            ServicesGoodPage(open_app).services_good_information(data["product_title"], data["product_description"],
                                                                 data["second_category_name"],
                                                                 data["third_category_name"],
                                                                 data["total_price"], data["subsist"],
                                                                 data["stock"], text=doc)

        with allure.step("立即上架"):
            PublishGoodCommon(open_app).submit()
        with allure.step("断言：立即上架后系统提示商品审核中"):
            text = BasePage(open_app).get_text(PGOK.good_audit_text, doc=doc)
            assert text == "商品审核中"


if __name__ == '__main__':
    pytest.main(
        ["-s", "test_publish_good.py", "--alluredir", allure_report + "/result", "--reruns", "3", "--reruns-delay",
         '3'])
    os.system(f"allure generate {allure_report}/result -o {allure_report}/html --clean")
