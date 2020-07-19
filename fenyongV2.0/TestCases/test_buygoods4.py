#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 17:17
# @Author :春衫
# @File :test_BuyGoods.py

from selenium import webdriver
from buy_goods.PageObjects.Login_page2 import LoginPage
from buy_goods.PageLocators.Index import Home
from buy_goods.PageLocators.MyIndex import MyIndex
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from buy_goods.PageObjects.BuyGood_page import BuyGoods
from shangji.Superior_template import SuperiorTemplate
from tools.URL import url
import unittest
from ddt import ddt, data
from DoExcel.do_excel import DoExcel
from Do_mysql.sql import SQL
from muban.template import GeShiHua
from muban.title import Title
from Calculation.calculation import A
from test_data.test_data import IP
# 别删这个decimal 也别注释掉
from decimal import *
from tools.project_path import *
from tools.my_log import MyLog
from buy_goods.PageLocators.BuyGoods import BuyGoods as BG
from tools.ReturnTxt import ReturnTxt
import warnings
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from new_muban.moban2 import MoBan
from new_muban.bind_user_relationship import bind_user_relationship_id
from new_muban.second_payagent_ratio_data import second_payagent_ratio_data

my_logger = MyLog()
test_data = DoExcel().get_data(test_case_path)


@ddt
class TestBuyGoods(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # 用setUpClass就能只打开浏览器一次，setUp则是每条用例都执行一次
        warnings.simplefilter("ignore", ResourceWarning)
        my_logger.info("----------开始执行测试用例----------")
        mobile_emulation = {'deviceName': 'iPhone X'}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        cls.driver = webdriver.Chrome(options=chrome_options)

    @data(*test_data)
    # 购买实物商品
    def test_1_buy_goods(self, item):

        global disanfang_province_id, disanfang_city_id, disanfang_area_id, disanfang_personal_id, reserve_fund, expected_userid, fanhui, expected_changes, expected_moban, sql_data, TestResult, Error
        my_logger.info("----------开始执行用例{0}，环境是{1}----------".format(item['case_id'], item['surroundings']))

        ip = IP[item['surroundings']]
        H5_Login_url = url(item['surroundings'])[0]
        H5_home_url = url(item['surroundings'])[1]

        self.driver.get(H5_Login_url)
        self.lg = LoginPage(self.driver)

        buyer_phone = eval(item['data'])['buyer_phone']
        seller_phone = eval(item['data'])['seller_phone']
        self.lg.login(buyer_phone)
        time.sleep(3)

        buyer_identity = item['buyer_identity']
        seller_identity = item['seller_identity']

        if buyer_identity == "公海用户":
            if seller_identity == "个人焕商" or seller_identity == "非焕商且已绑定个人焕商":
                self.driver.find_element(*MyIndex.myIndex).click()
                time.sleep(5)

                # 充值
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((MyIndex.serviceRecharge))).click()
                time.sleep(3)
                self.driver.find_element(*MyIndex.recharge_amount).click()
                time.sleep(2)
                self.driver.find_element(*MyIndex.input_amount).send_keys(100)
                time.sleep(2)
                self.driver.find_element(*MyIndex.queren).click()
                time.sleep(3)
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((MyIndex.rechare_now))).click()
                time.sleep(3)
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((MyIndex.querenzhifu))).click()
                time.sleep(2)

                # 支付按键
                BuyGoods(self.driver).pay()
                time.sleep(2)

                # 写回储备池和充值金额
                user_id = eval(item['data'])["买家"]
                reserve_fund = SQL(ip).reserve_fund(user_id)
                DoExcel.reserve_fund(test_case_path, item['sheet_name'], item['case_id'], str(reserve_fund))
                # time.sleep(5)

                self.driver.get(H5_home_url)
                time.sleep(2)

        # 选择商品
        self.driver.find_element(*Home.search).click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Home.input))).send_keys(
            item['goodsname'])
        time.sleep(2)
        self.driver.find_element(*Home.input).send_keys(Keys.ENTER)
        time.sleep(3)
        # 点击【商品】
        self.driver.find_element(*Home.real_goods).click()
        time.sleep(3)

        # 购买流程
        BuyGoods(self.driver).BuyGood(item['payment_method'])
        time.sleep(3)
        BuyGoods(self.driver).pay()
        time.sleep(2)

        # 卖家操作
        self.driver.get(H5_Login_url)
        lg = LoginPage(self.driver)
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
        # 确认订单
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((MyIndex.confirm_Order))).click()
        time.sleep(6)

        # 根据商品名判断流程
        if item['goodsname'].find('实物商品') != -1:  # 商品名字包含实物商品
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
            lg = LoginPage(self.driver)
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

        elif item['goodsname'].find('本地生活') != -1:
            # 本地生活
            self.driver.get(H5_Login_url)
            lg = LoginPage(self.driver)
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
            lg = LoginPage(self.driver)
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

        elif item['goodsname'].find('商企服务') != -1:
            # 买家
            self.driver.get(H5_Login_url)
            lg = LoginPage(self.driver)
            lg.login(buyer_phone)
            time.sleep(2)
            # 点击【采购订单】
            self.driver.find_element(*MyIndex.purchase).click()
            time.sleep(4)

            # 确认签约
            self.driver.find_element(*BG.qianyue).click()

            # 支付按键
            BuyGoods(self.driver).pay()
            time.sleep(2)

        # 写回订单号
        buyerid = eval(item['data'])['买家']
        order = DoExcel.get_order(ip, test_case_path, item['sheet_name'], item['case_id'], int(buyerid))
        # time.sleep(5)

        # 获取绑定关系，写回Excel
        if item['payment_method'] in ["易贝", "易贝券"]:
            superior = SuperiorTemplate().superior_template(ip, item['payment_method'], item['data'],
                                                            item['sheet_name'],
                                                            item['case_id'],
                                                            buyer_phone)

        elif item['payment_method'] in ["抵工资", "家人购"]:
            disanfang_phone = eval(item['data'])['disanfang_phone']
            superior = SuperiorTemplate().superior_template(ip, item['payment_method'], item['data'],
                                                            item['sheet_name'],
                                                            item['case_id'],
                                                            buyer_phone, disanfang_phone)

        else:
            seller_phone = eval(item['data'])['seller_phone']
            superior = SuperiorTemplate().superior_template(ip, item['payment_method'], item['data'],
                                                            item['sheet_name'],
                                                            item['case_id'],
                                                            buyer_phone, seller_phone)

        # time.sleep(5)
        # print('shangji',shangji)

        if item['payment_method'] in ["易贝", "易贝券"]:
            buyer_province_id = superior[1]['省代理商']
            buyer_city_id = superior[1]['市代理商']
            buyer_area_id = superior[1]['区代理商']
            buyer_personal_id = superior[0]['个人焕商']
        else:
            buyer_province_id = superior['储备池分佣'][1]['省代理商']
            buyer_city_id = superior['储备池分佣'][1]['市代理商']
            buyer_area_id = superior['储备池分佣'][1]['区代理商']
            buyer_personal_id = superior['储备池分佣'][0]['个人焕商']

            disanfang_province_id = superior['支付服务费分佣'][1]['省代理商']
            disanfang_city_id = superior['支付服务费分佣'][1]['市代理商']
            disanfang_area_id = superior['支付服务费分佣'][1]['区代理商']
            disanfang_personal_id = superior['支付服务费分佣'][0]['个人焕商']

        # print(buyer_province_id,buyer_city_id,buyer_area_id,buyer_personal_id)
        # 获取上级分佣比例，写回Excel
        if item['payment_method'] in ["易贝", "易贝券"]:
            proportion = SuperiorTemplate().fenyong_template(ip, item['payment_method'], item['sheet_name'],
                                                             item['case_id'], buyer_province_id,
                                                             buyer_city_id, buyer_area_id, buyer_personal_id)


        elif item['payment_method'] in ["抵工资", "家人购"]:
            proportion = SuperiorTemplate().fenyong_template(ip, item['payment_method'], item['sheet_name'],
                                                             item['case_id'], buyer_province_id,
                                                             buyer_city_id, buyer_area_id, buyer_personal_id,
                                                             disanfang_province_id, disanfang_city_id,
                                                             disanfang_area_id, disanfang_personal_id)

        else:
            proportion = SuperiorTemplate().fenyong_template(ip, item['payment_method'], item['sheet_name'],
                                                             item['case_id'], buyer_province_id,
                                                             buyer_city_id, buyer_area_id, buyer_personal_id,
                                                             disanfang_province_id, disanfang_city_id,
                                                             disanfang_area_id, disanfang_personal_id)

        # time.sleep(5)

        if buyer_identity == "公海用户":
            if seller_identity == "个人焕商" or seller_identity == "非焕商且已绑定个人焕商":
                # 跳回卖家，解除伙伴绑定
                self.driver.get(H5_Login_url)
                lg = LoginPage(self.driver)
                if seller_identity == "个人焕商":
                    lg.login(seller_phone)
                elif seller_identity == "非焕商且已绑定个人焕商":
                    bangding_phone = eval(item['data'])['bangding_phone']
                    lg.login(bangding_phone)
                time.sleep(2)
                self.driver.get(H5_home_url)
                time.sleep(2)
                self.driver.find_element(*MyIndex.myIndex).click()
                time.sleep(2)
                self.driver.find_element(*MyIndex.myPartner).click()
                time.sleep(3)
                if item['surroundings'] == "test":
                    self.driver.find_element(*MyIndex.delete1).click()
                elif item['surroundings'] == "mtest":
                    self.driver.find_element(*MyIndex.delete2).click()
                elif item['surroundings'] == "dev1":
                    self.driver.find_element(*MyIndex.delete3).click()
                time.sleep(2)
                self.driver.find_element(*MyIndex.queren).click()
                time.sleep(5)

        my_logger.info("----------前端操作执行完毕----------")

        ip = IP[item['surroundings']]
        data = eval(item['data'])

        buyer_id = data['买家']
        platform_id = data['平台']

        # 查询买家是否绑定销售/业务焕商/TCO
        if item['payment_method'] in ["易贝", "易贝券"]:
            # 获取买家绑定的销售/业务焕商/TCO dict
            bind_buyer_relationship = SQL(ip).bind_user_relationship(buyer_id)
            if bind_buyer_relationship != None:
                bind_buyer_relationship_data = bind_user_relationship_id(ip, bind_buyer_relationship)
            else:
                bind_buyer_relationship_data = None

            # 把买家上级销售/业务焕商的上级写回Excel
            DoExcel().bing_sale_id(test_case_path, item['sheet_name'], item['case_id'],
                                   str(bind_buyer_relationship_data))

        if item['payment_method'] in ["抵工资", "家人购","现金"]:
            if item['payment_method'] =="现金":
                payer_id=data['卖家']
            else:
                payer_id = data['出钱方']

            # 获取买家绑定的销售/业务焕商/TCO dict
            bind_buyer_relationship = SQL(ip).bind_user_relationship(buyer_id)
            if bind_buyer_relationship != None:
                bind_buyer_relationship_data = bind_user_relationship_id(ip, bind_buyer_relationship)
            else:
                bind_buyer_relationship_data = None

            # 获取出钱人绑定的销售/业务焕商/TCO dict
            bind_payer_relationship = SQL(ip).bind_user_relationship(payer_id)
            if bind_payer_relationship != None:
                bind_payer_relationship_data = bind_user_relationship_id(ip, bind_payer_relationship)
            else:
                bind_payer_relationship_data = None

            # 买家上级销售/业务焕商的上级，写回模板
            bind_buyer_relationship_id = {"储备金二级分佣对象": bind_buyer_relationship_data,
                                          "支付服务费二级分佣对象": bind_payer_relationship_data}
            DoExcel().bing_sale_id(test_case_path, item['sheet_name'], item['case_id'],
                                   str(bind_buyer_relationship_id))

        # 生成易贝、抵工资、家人购流水模板
        if item['payment_method'] in ['易贝', '抵工资', '家人购']:

            if item['payment_method'] == "易贝":
                reserve_fund_bind_area_id = superior[1]['区代理商']
                reserve_fund_bind_city_id = superior[1]['市代理商']
                reserve_fund_bind_province_id = superior[1]['省代理商']
                service_fee_bind_area_id = superior[1]['区代理商']
                service_fee_bind_city_id = superior[1]['市代理商']
                service_fee_bind_province_id = superior[1]['省代理商']


            # 抵工资 家人购
            else:
                service_fee_bind_area_id = superior['支付服务费分佣'][1]['区代理商']
                service_fee_bind_city_id = superior['支付服务费分佣'][1]['市代理商']
                service_fee_bind_province_id = superior['支付服务费分佣'][1]['省代理商']
                reserve_fund_bind_area_id = superior['储备池分佣'][1]['区代理商']
                reserve_fund_bind_city_id = superior['储备池分佣'][1]['市代理商']
                reserve_fund_bind_province_id = superior['储备池分佣'][1]['省代理商']

        # 生成易贝券流水模板
        elif item['payment_method'] == "易贝券":
            reserve_fund_bind_area_id = superior[1]['区代理商']
            reserve_fund_bind_city_id = superior[1]['市代理商']
            reserve_fund_bind_province_id = superior[1]['省代理商']

        # 生成现金账户、微信、支付宝流水模板
        else:
            reserve_fund_bind_area_id = superior['储备池分佣'][1]['区代理商']
            reserve_fund_bind_city_id = superior['储备池分佣'][1]['市代理商']
            reserve_fund_bind_province_id = superior['储备池分佣'][1]['省代理商']
            service_fee_bind_area_id = superior['支付服务费分佣'][1]['区代理商']
            service_fee_bind_city_id = superior['支付服务费分佣'][1]['市代理商']
            service_fee_bind_province_id = superior['支付服务费分佣'][1]['省代理商']

        # 获取这笔订单应该【使用】的二级分佣比例
        reserve_fund_second_payagent_ratio = second_payagent_ratio_data(ip, reserve_fund_bind_province_id,
                                                                        reserve_fund_bind_city_id,
                                                                        reserve_fund_bind_area_id,
                                                                        platform_id)
        if item['payment_method'] == "易贝券":
            # 交易服务费二级分佣比例
            transaction_second_payagent_ratio = {"储备金二级分佣比例": reserve_fund_second_payagent_ratio,
                                                 "支付服务费二级分佣比例": None}
            # 把这笔订单所使用的二级分佣比例写回Excel
            DoExcel().second_payagent_ratio(test_case_path, item['sheet_name'], item['case_id'],
                                            str(transaction_second_payagent_ratio))

        if item['payment_method'] != "易贝券":
            # 获取出钱方所使用的二级分佣比例
            service_fee_second_payagent_ratio = second_payagent_ratio_data(ip, service_fee_bind_province_id,
                                                                           service_fee_bind_city_id,
                                                                           service_fee_bind_area_id,
                                                                           platform_id)

            # 交易服务费二级分佣比例
            transaction_second_payagent_ratio = {"储备金二级分佣比例": reserve_fund_second_payagent_ratio,
                                                 "支付服务费二级分佣比例": service_fee_second_payagent_ratio}
            # 把这笔交易时用的二级分佣比例写回Excel
            DoExcel().second_payagent_ratio(test_case_path, item['sheet_name'], item['case_id'],
                                            str(transaction_second_payagent_ratio))

        my_logger.info("----------开始进行对比----------")

        try:
            ip = IP[item['surroundings']]

            if item['payment_method'] in ["易贝", "易贝券"]:
                buyer_province_proportion = proportion['省分佣比例']
                buyer_city_proportion = proportion['市分佣比例']
                buyer_area_proportion = proportion['区分佣比例']
                buyer_personal_proportion = proportion['个人分佣比例']
                disanfang_province_proportion = None
                disanfang_city_proportion = None
                disanfang_area_proportion = None
                disanfang_personal_proportion = None
            else:
                buyer_province_proportion = proportion['储备池分佣']['省分佣比例']
                buyer_city_proportion = proportion['储备池分佣']['市分佣比例']
                buyer_area_proportion = proportion['储备池分佣']['区分佣比例']
                buyer_personal_proportion = proportion['储备池分佣']['个人分佣比例']

                disanfang_province_proportion = proportion['支付服务费分佣']['省分佣比例']
                disanfang_city_proportion = proportion['支付服务费分佣']['市分佣比例']
                disanfang_area_proportion = proportion['支付服务费分佣']['区分佣比例']
                disanfang_personal_proportion = proportion['支付服务费分佣']['个人分佣比例']

            if item['buyer_identity'] == "公海用户":
                if item['seller_identity'] == "个人焕商" or item['seller_identity'] == "非焕商且已绑定个人焕商":
                    charge_amount = reserve_fund['charge_amount']
                    reserve_fund = reserve_fund['reserve_fund']
                else:
                    charge_amount = None
                    reserve_fund = None
            else:
                charge_amount = None
                reserve_fund = None

            # 计算出来的（商品价格，需要支付的易贝服务费，需要支付的现金服务费）（储备池分佣）（服务费分佣）
            calculation = A(item['buyer_identity'], item['seller_identity'],
                            buyer_province_proportion=buyer_province_proportion,
                            buyer_city_proportion=buyer_city_proportion,
                            buyer_area_proportion=buyer_area_proportion,
                            buyer_personal_proportion=buyer_personal_proportion,
                            disanfang_province_proportion=disanfang_province_proportion,
                            disanfang_city_proportion=disanfang_city_proportion,
                            disanfang_area_proportion=disanfang_area_proportion,
                            disanfang_personal_proportion=disanfang_personal_proportion, ).transaction(ip, item[
                'member_level'], item['payment_method'], order, charge_amount, reserve_fund)

            if item['payment_method'] in ["易贝", "易贝券"]:
                expected_moban = MoBan(item['buyer_identity'], item['seller_identity'], item['member_level'],
                                       item['payment_method'], order).moban(eval(item['data']),
                                                                            superior,
                                                                            ip, calculation,
                                                                            order,
                                                                            transaction_second_payagent_ratio,
                                                                            bind_buyer_relationship_data,
                                                                            reserve_fund=reserve_fund)
            else:
                expected_moban = MoBan(item['buyer_identity'], item['seller_identity'], item['member_level'],
                                       item['payment_method'], order).moban(eval(item['data']),
                                                                                    superior,
                                                                                    ip, calculation,
                                                                                    order,
                                                                                    transaction_second_payagent_ratio,
                                                                                    bind_buyer_relationship_data,
                                                                                    bind_payer_relationship_data,
                                                                                    reserve_fund=reserve_fund)

            # 写回Excel用
            fanhui = GeShiHua(item['buyer_identity'], item['seller_identity'], item['member_level'],
                              item['payment_method'], order).fanhui(ip, superior)

            sql_data = SQL(ip).wallet_detail(order)

            shuju = Title(item['buyer_identity'], item['seller_identity'],
                          item['payment_method']).title(superior)

            for i in range(0, len(shuju)):
                self.assertEqual(expected_moban[i], sql_data[i])

            self.assertEqual(expected_moban, sql_data)
            my_logger.info("用例{0}正确！{1}".format(item['case_id'], item['title']))
            TestResult = 'Pass'
            Error = None

        except AssertionError as e:
            my_logger.info("用例错误！错误原因是第{0}行，{1}：".format(i + 1, e))
            TestResult = 'Failed'
            Error = "用例错误！错误原因是：第{0}行，{1}：".format(i + 1, e)
            raise e  # 异常处理完后记得抛出

        finally:  # 不管怎样都得写入Excel
            DoExcel().write_back(test_case_path, item['sheet_name'], item['case_id'] + 1,
                                 str(fanhui[0]), str(fanhui[2]), str(expected_moban),
                                 str(sql_data), TestResult, str(Error))

        # time.sleep(2)
        my_logger.info("----------对比结束----------")
        my_logger.info("----------用例{0}执行完毕----------".format(item['case_id']))

    def tearDown(cls):
        cls.driver.quit()
        my_logger.info("----------结束----------")


if __name__ == '__main__':
    unittest.main(verbosity=2)
