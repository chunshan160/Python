#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/10 17:38
# @Author :春衫
# @File :Run.py
import os
import pytest
from Common.project_path import allure_report

from Common.project_path import TestCases

pytest.main(
    ["-v", "-s", TestCases + "/test_commission.py", "--alluredir", allure_report + "/result", "--clean-alluredir"])

# # 失败重跑
# pytest.main(
#     ["-v", "-s", "--reruns", "1", "--reruns-delay", "1", "test_commission.py", "--alluredir",
#      allure_report + "/result", "--clean-alluredir"])

#生成测试报告
os.system(f"allure generate {allure_report}/result -o {allure_report}/html --clean")
