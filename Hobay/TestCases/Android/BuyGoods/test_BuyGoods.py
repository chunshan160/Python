#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 17:17
# @Author :春衫
# @File :test_BuyGoods.py


import allure
import pytest

from PageObjects.Android.Index.Index import IndexPage
from PageObjects.Android.SearchGood.SearchGood import SearchGoodPage
from PageObjects.Android.GoodDetail.GoodDetail_Page import GoodDetailPage
from PageObjects.Android.ConfirmOrder.ConfirmOrder_Page import ConfirmOrderPage
from PageObjects.Android.Pay.Pay import PayPage
from PageObjects.Android.SystemPoint.Pay_Success import PaySuccessPage
from TestData.Android.BuyGoods.BuyGoods import *
from Common.project_path import *


@allure.feature('购买商品功能')
class TestBuyGoods:

    @allure.story("购买实物商品")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("buy_goods")
    @pytest.mark.parametrize("data", buy_entity_goods)
    def test_1_buy_entity_goods(self, buy_goods, data):
        doc = "测试购买实物商品-"
        with allure.step("首页点击搜索"):
            IndexPage(buy_goods).search(text=doc)
        with allure.step("输入商品名-点击第一个商品-"):
            SearchGoodPage(buy_goods).send_search(data['goods_name'], text=doc)
        with allure.step("商品详情-下单-"):
            GoodDetailPage(buy_goods).buy_good(text=doc)
        with allure.step("确认订单"):
            ConfirmOrderPage(buy_goods).submit_order_now(text=doc)
            PayPage(buy_goods).payment_method(data['payment_method'], text=doc)
        with allure.step("关闭可能出现的 加入焕商 弹窗"):
            PaySuccessPage(buy_goods).close_windows(text=doc)
        with allure.step("断言：支付成功后系统提示:支付成功"):
            text = PaySuccessPage(buy_goods).title_text(text=doc)
            assert text == "支付成功"
        with allure.step("截图保存到项目中"):
            buy_goods.save_screenshot(f"{allure_report}/screenshot/购买商品功能-购买实物商品-{data['payment_method']}支付.png")
            allure.attach.file(f"{allure_report}/screenshot/购买商品功能-购买实物商品-{data['payment_method']}支付.png", "附件截图",
                               attachment_type=allure.attachment_type.PNG)

    @allure.story("购买本地生活商品")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("buy_goods")
    @pytest.mark.parametrize("data", buy_coupon_goods)
    def test_2_buy_coupon_goods(self, buy_goods, data):
        doc = "测试购买本地生活商品-"
        with allure.step("首页点击搜索"):
            IndexPage(buy_goods).search(text=doc)
        with allure.step("输入商品名-点击第一个商品-"):
            SearchGoodPage(buy_goods).send_search(data['goods_name'], text=doc)
        with allure.step("商品详情-下单-"):
            GoodDetailPage(buy_goods).buy_good(text=doc)
        with allure.step("确认订单"):
            ConfirmOrderPage(buy_goods).submit_order_now(text=doc)
            PayPage(buy_goods).payment_method(data['payment_method'], text=doc)
        with allure.step("关闭可能出现的 加入焕商 弹窗"):
            PaySuccessPage(buy_goods).close_windows(text=doc)
        with allure.step("断言：支付成功后系统提示:支付成功"):
            text = PaySuccessPage(buy_goods).title_text(text=doc)
            assert text == "支付成功"
        with allure.step("截图保存到项目中"):
            buy_goods.save_screenshot(f"{allure_report}/screenshot/购买商品功能-购买本地生活商品-{data['payment_method']}支付.png")
            allure.attach.file(f"{allure_report}/screenshot/购买商品功能-购买本地生活商品-{data['payment_method']}支付.png", "附件截图",
                               attachment_type=allure.attachment_type.PNG)


    @allure.story("购买商企服务商品")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("buy_goods")
    @pytest.mark.parametrize("data", buy_server_goods)
    def test_3_buy_server_goods(self, buy_goods, data):
        doc = "测试购买商企服务商品-"
        with allure.step("首页点击搜索"):
            IndexPage(buy_goods).search(text=doc)
        with allure.step("输入商品名-点击第一个商品-"):
            SearchGoodPage(buy_goods).send_search(data['goods_name'], text=doc)
        with allure.step("商品详情-下单-"):
            GoodDetailPage(buy_goods).buy_good(text=doc)
        with allure.step("确认订单"):
            ConfirmOrderPage(buy_goods).submit_order_now(text=doc)
        with allure.step(f"{data['payment_method']}支付"):
            PayPage(buy_goods).payment_method(data['payment_method'], text=doc)
        with allure.step("关闭可能出现的 加入焕商 弹窗"):
            PaySuccessPage(buy_goods).close_windows(text=doc)
        with allure.step("断言：支付成功后系统提示:支付成功"):
            text = PaySuccessPage(buy_goods).title_text(text=doc)
            assert text == "支付成功"
        with allure.step("截图保存到项目中"):
            buy_goods.save_screenshot(f"{allure_report}/screenshot/购买商品功能-购买商企服务商品-{data['payment_method']}支付.png")
            allure.attach.file(f"{allure_report}/screenshot/购买商品功能-购买商企服务商品-{data['payment_method']}支付.png", "附件截图",
                               attachment_type=allure.attachment_type.PNG)


if __name__ == '__main__':
    pytest.main(
        ["-v","-s", "--reruns", "1", "--reruns-delay", "1", "test_BuyGoods.py", "--alluredir",
         allure_report + "/result"])
    os.system(f"allure generate {allure_report}/result -o {allure_report}/html --clean")
