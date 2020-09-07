import os
import logging
from interface_auto.common.project_path import log_dir
from interface_auto.common.read_config import ReadConfig

m_level = ReadConfig().read_config('LOG', 'level')
c_level = ReadConfig().read_config('LOG', 'c_level')
f_level = ReadConfig().read_config('LOG', 'f_level')
filename = ReadConfig().read_config('LOG', 'filename')
# 拼接日志文件的路径
file_path = os.path.join(log_dir, filename)


class MyLog:
    """封装打印日志的方法"""

    def create_logger(self, message, level):
        # 定义一个日志收集器
        my_logger = logging.getLogger('api_auto')
        # 设定日志的级别
        my_logger.setLevel(m_level)
        # 设置输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        # 指定输出到控制台
        control_handler = logging.StreamHandler()
        control_handler.setLevel(c_level)
        control_handler.setFormatter(formatter)
        my_logger.addHandler(control_handler)

        # 指定输出到文件
        file_hander = logging.FileHandler(file_path, encoding='utf-8')
        file_hander.setLevel(f_level)
        file_hander.setFormatter(formatter)
        my_logger.addHandler(file_hander)

        # 收集日志
        if level == 'DEBUG':
            my_logger.debug(message)
        elif level == 'INFO':
            my_logger.info(message)
        elif level == 'WARNING':
            my_logger.warning(message)
        elif level == 'ERROR':
            my_logger.error(message)
        elif level == 'CRITICAL':
            my_logger.critical(message)

        # 关闭渠道
        my_logger.removeHandler(control_handler)
        my_logger.removeHandler(file_hander)

    def debug(self, message):
        self.create_logger(message, 'DEBUG')

    def info(self, message):
        self.create_logger(message, 'INFO')

    def warning(self, message):
        self.create_logger(message, 'WARNING')

    def error(self, message):
        self.create_logger(message, 'ERROR')

    def critical(self, message):
        self.create_logger(message, 'CRITICAL')

if __name__ == '__main__':
    MyLog().error('aixinxin...')
    MyLog().critical('youarethebest...')
