import os
"""
该模块用来存放整个项目目录的路径
"""

# 当前项目目录的路径
project_dir = os.path.dirname(os.path.dirname(__file__))

# 配置文件的目录路径
config_dir = os.path.join(project_dir, 'conf')
# 测试用例的目录路径
cases_dir = os.path.join(project_dir, 'test_cases')
# 测试数据的目录路径
data_dir = os.path.join(project_dir, 'data')
# 测试日志的目录路径
log_dir = os.path.join(project_dir, 'log')
# 测试报告的目录路径
report_dir = os.path.join(project_dir, 'report')
