# coding=utf-8

""""" 运行 “.” (当前)目录下的所有测试用例，并生成HTML测试报告 """""


import unittest
import HTMLTestReportCN
# from TestCases.test_buygoods4 import TestBuyGoods
from TestCases.H5.PublishGood.test_publish_good import PublishGood



class RunTests(object):

    def __init__(self):
        self.test_case_path = "../TestCases"
        self.title = "自动化测试报告"
        self.description = "测试报告"

    def run_one(self):
        test_suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        # 购买、确认收货、写回订单、解绑、处理数据、对比
        test_suite.addTest(loader.loadTestsFromTestCase(PublishGood))

        # 启动测试时创建文件夹并获取报告的名字
        report_dir = HTMLTestReportCN.ReportDirectory(path="../Report/")
        report_dir.create_dir(title=self.title)
        report_path = HTMLTestReportCN.GlobalMsg.get_value("report_path")

        fp = open(report_path, "wb")

        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=self.title, description=self.description,
                                                 tester="春衫")
        runner.run(test_suite)
        fp.close()

if __name__ == "__main__":
    RunTests().run_one()
