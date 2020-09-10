#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 17:17
# @Author :春衫
# @File :test_BuyGoods.py

from selenium import webdriver
# from Handle.za.H5_Login_page2 import H5_LoginPage
# from PageObjects import Location
from PageLocators.Android import MyIndex
import time
from selenium.webdriver.common.action_chains import ActionChains
# from Handle.Android.za.BuyGood_page import BuyGoods
# from Handle.za.Untie_Partner import UntiePartner
from Common.fengyong.Superior.Superior_template import SuperiorTemplate
from Common.URL import url
import unittest
from ddt import ddt, data
from Common.DoExcel import DoExcel
from Common.DoMySQL import SQL
from Common.fengyong.Calculation_Data import CalculationData
from TestData.test_data import IP
from Common.project_path import *
from Common.user_log import UserLog
import warnings
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.fengyong.new_muban.moban2 import MoBan
from Common.fengyong.boss_setting import BossSetting
# from PageObjects import Recharge
# from Handle.za.Seach_Goods import Seach_Goods
# from Handle.za.Receipt_Delivery import ReceiptDelivery
from Common.fengyong.bing_relationship_data import BingRelationshipData
from Common.fengyong.TransactionSecondPayagentRatio import TransactionSecondPayagentRatio
from Common.fengyong.new_muban.Fan_Hui import FanHui
import HTMLTestReportCN

my_logger = UserLog()
test_data = DoExcel().get_data(test_case_path)


@ddt
class TestBuyGoods(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.report_dir = HTMLTestReportCN.ReportDirectory(path="./Report/")
        # 用setUpClass就能只打开浏览器一次，setUp则是每条用例都执行一次
        warnings.simplefilter("ignore", ResourceWarning)
        # 窗口最大化
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @data(*test_data)
    # 购买实物商品
    def test_1_buy_goods(self, item):

        my_logger.info("----------开始执行用例{0}，环境是{1}----------".format(item['case_id'], item['surroundings']))

        ip = IP[item['surroundings']]

        H5_Login_url = url(item['surroundings'])[0]
        H5_home_url = url(item['surroundings'])[1]

        buyer_phone = eval(item['data'])['buyer_phone']
        seller_phone = eval(item['data'])['seller_phone']

        # 获取绑定关系
        superior = SuperiorTemplate().superior_template_main(ip, item['payment_method'], item['data'], buyer_phone)

        Boss_login_url = url(item['surroundings'])[2]

        operational_setting = eval(item['operational_setting'])
        print("----------开始BOSS后台设置运营分佣比例操作----------")
        try:

            self.driver.get(Boss_login_url)
            #Boss后台设置运营分佣比例
            BossSetting(self.driver).main(ip, item['payment_method'], superior, operational_setting)

            print("----------BOSS后台运营分佣比例设置完毕----------")

        except Exception as e:
            # 截图
            self.report_dir.get_screenshot(self.driver)

            raise e  # 异常处理完后记得抛出

        finally:
            self.driver.quit()

        print("----------开始Web操作----------")
        try:
            mobile_emulation = {'deviceName': 'iPhone X'}
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            driver = webdriver.Chrome(options=chrome_options)

            driver.get(H5_Login_url)
            self.lg = H5_LoginPage(driver)

            self.lg.login(buyer_phone)

            #定位
            time.sleep(5)
            Location().location(driver)

            buyer_identity = item['buyer_identity']
            seller_identity = item['seller_identity']

            #充值服务费，增加储备池
            if buyer_identity == "公海用户":
                if seller_identity == "个人焕商" or seller_identity == "非焕商且已绑定个人焕商":
                    driver.find_element(*MyIndex.myIndex).click()
                    time.sleep(6)

                    # # 充值
                    Recharge().recharge(driver)
                    time.sleep(2)
                    # 支付按键
                    BuyGoods(driver).pay()
                    time.sleep(2)

                    # 写回储备池和充值金额
                    user_id = eval(item['data'])["买家"]
                    reserve_fund_data = SQL(ip).reserve_fund_data(user_id)
                    DoExcel.reserve_fund(test_case_path, item['sheet_name'], item['case_id'], str(reserve_fund_data))
                    # time.sleep(5)

                    driver.get(H5_home_url)
                    time.sleep(2)

            # 选择商品
            Seach_Goods().seach_goods(driver, item['goodsname'])

            # 购买流程
            BuyGoods(driver).BuyGood(item['payment_method'])
            time.sleep(3)

            # 卖家操作
            driver.get(H5_Login_url)
            lg = H5_LoginPage(driver)
            lg.login(seller_phone)
            time.sleep(2)
            driver.get(H5_home_url)
            time.sleep(2)
            driver.find_element(*MyIndex.myIndex).click()
            time.sleep(2)
            # 滚动至元素【销售订单】可见，点击
            ActionChains(driver).move_to_element(driver.find_element(*MyIndex.saleOrderList)).perform()
            driver.execute_script('window.scrollBy(0,500)')
            time.sleep(2)
            driver.find_element(*MyIndex.saleOrderList).click()
            time.sleep(5)
            # 确认订单
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MyIndex.confirm_Order))).click()
            time.sleep(6)

            # 根据商品名判断流程
            if "实物商品" in item['goodsname']:
                ReceiptDelivery(driver).entity_good(H5_Login_url, buyer_phone)

            elif "本地服务" in item['goodsname']:
                ReceiptDelivery(driver).coupon_good(H5_Login_url, H5_home_url, buyer_phone, seller_phone)

            elif "商企服务" in item['goodsname']:
                ReceiptDelivery(driver).Business_Services(H5_Login_url,buyer_phone)

            # 写回订单号
            buyerid = eval(item['data'])['买家']
            order = DoExcel.get_order(ip, test_case_path, item['sheet_name'], item['case_id'], buyerid)

            # 获取绑定关系，写回Excel
            superior = SuperiorTemplate().superior_template_main(ip, item['payment_method'], item['data'], buyer_phone)
            DoExcel.superior(test_case_path, item['sheet_name'], item['case_id'], str(superior))

            # 获取上级分佣比例，写回Excel
            proportion = SuperiorTemplate().fenyong_template_main(ip, item['payment_method'], superior)
            DoExcel.fenyong_bili(test_case_path, item['sheet_name'], item['case_id'], str(proportion))

            if buyer_identity == "公海用户":
                if seller_identity == "个人焕商" or seller_identity == "非焕商且已绑定个人焕商":
                    # 跳回卖家，解除伙伴绑定
                    driver.get(H5_Login_url)
                    lg = H5_LoginPage(driver)
                    if seller_identity == "个人焕商":
                        lg.login(seller_phone)
                    elif seller_identity == "非焕商且已绑定个人焕商":
                        bangding_phone = eval(item['data'])['bangding_phone']
                        lg.login(bangding_phone)
                    time.sleep(2)
                    driver.get(H5_home_url)
                    time.sleep(2)
                    driver.find_element(*MyIndex.myIndex).click()
                    time.sleep(2)
                    driver.find_element(*MyIndex.myPartner).click()
                    time.sleep(3)
                    # 解绑
                    UntiePartner().untie_partner(driver, item['surroundings'])

            my_logger.info("----------前端操作执行完毕----------")

            ip = IP[item['surroundings']]
            data = eval(item['data'])

            buyer_id = data['买家']

            # 查询买家是否绑定销售/业务焕商/TCO
            if item['payment_method'] in ["易贝", "易贝券"]:
                # 获取买家绑定的销售/业务焕商/TCO dict
                bind_buyer_relationship_data = BingRelationshipData().bing_relationship_data(ip, item['payment_method'],
                                                                                             data, buyer_id)

                # 把买家上级销售/业务焕商的上级写回Excel
                DoExcel().bing_sale_id(test_case_path, item['sheet_name'], item['case_id'],
                                       str(bind_buyer_relationship_data))

            elif item['payment_method'] in ["抵工资", "家人购", "现金"]:
                bind_relationship_data = BingRelationshipData().bing_relationship_data(ip, item['payment_method'], data,
                                                                                       buyer_id)
                bind_buyer_relationship_data = bind_relationship_data[0]
                bind_payer_relationship_data = bind_relationship_data[1]
                # 买家上级销售/业务焕商的上级，写回模板
                bind_buyer_relationship_id = {"储备金二级分佣对象": bind_buyer_relationship_data,
                                              "支付服务费二级分佣对象": bind_payer_relationship_data}
                DoExcel().bing_sale_id(test_case_path, item['sheet_name'], item['case_id'],
                                       str(bind_buyer_relationship_id))

            # 获取这笔订单应该【使用】的二级分佣比例
            transaction_second_payagent_ratio = TransactionSecondPayagentRatio().transaction_second_payagent_ratio(ip, item[
                'payment_method'], superior, data)
            # 把这笔订单所使用的二级分佣比例写回Excel
            DoExcel().second_payagent_ratio(test_case_path, item['sheet_name'], item['case_id'],
                                            str(transaction_second_payagent_ratio))
        except Exception as e:
            # 截图
            self.report_dir.get_screenshot(driver)
            driver.quit()
            raise e  # 异常处理完后记得抛出
        # finally:
        #     driver.quit()



        try:
            my_logger.info("----------开始进行对比----------")


            ip = IP[item['surroundings']]
            if buyer_identity == "公海用户":
                if seller_identity == "个人焕商" or seller_identity == "非焕商且已绑定个人焕商":
                    charge_amount = reserve_fund_data['charge_amount']
                    reserve_fund = reserve_fund_data['reserve_fund']
                else:
                    charge_amount = None
                    reserve_fund = None
            else:
                charge_amount = None
                reserve_fund = None

            calculation_data = CalculationData().calculation_data(ip, item['payment_method'], item['member_level'],
                                                                  buyer_identity, seller_identity, proportion,
                                                                  charge_amount,reserve_fund, order)

            if item['payment_method'] in ["易贝", "易贝券"]:
                expected_moban = MoBan(buyer_identity, seller_identity, item['member_level'], item['payment_method'],
                                       order).expected_moban(ip, data,superior,reserve_fund, calculation_data, transaction_second_payagent_ratio,
                                                             bind_buyer_relationship_data)
            elif item['payment_method'] in ["抵工资", "家人购", "现金"]:
                expected_moban = MoBan(buyer_identity, seller_identity, item['member_level'], item['payment_method'],
                                       order).expected_moban(ip, data,superior,reserve_fund, calculation_data, transaction_second_payagent_ratio,
                                                             bind_buyer_relationship_data, bind_payer_relationship_data)

            # 写回Excel用
            fanhui = FanHui().fan_hui(ip, order, expected_moban)

            sql_data = SQL(ip).wallet_detail(order)

            for i in range(0, len(expected_moban)):
                self.assertEqual(expected_moban[i], sql_data[i])

            self.assertEqual(expected_moban, sql_data)
            my_logger.info("用例{0}正确！{1}".format(item['case_id'], item['title']))
            TestResult = 'Pass'
            Error = None

        except Exception as e:
            #截图
            self.report_dir.get_screenshot(driver)
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
        my_logger.info("----------结束----------")


if __name__ == '__main__':
    unittest.main(verbosity=2)
