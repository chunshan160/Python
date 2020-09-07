import unittest
import time
import os
from HTMLTestRunner import HTMLTestRunner
from interface_auto.common.send_email import SendEmail
from interface_auto.common.project_path import report_dir, cases_dir

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = now + 'report.html'
# 拼接测试报告的路径
report_path = os.path.join(report_dir, report_name)

# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# # suite.addTest(loader.loadTestsFromModule(cases_dir))
discover = unittest.defaultTestLoader.discover(cases_dir, pattern='test*.py', top_level_dir=None)

with open(report_path, 'wb') as file:
    runner = HTMLTestRunner(stream=file,
                            verbosity=2,
                            title='自动化测试报告',
                            description='注册、登录、充值接口的所有用例')
    runner.run(discover)
    # SendEmail.send_mail(report_path)