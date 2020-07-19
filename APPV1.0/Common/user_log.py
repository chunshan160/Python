#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/19 19:03
# @Author :春衫
# @File :user_log.py
import logging
from Common.project_path import *

class UserLog:

    def user_log(self, msg, level):

        # 定义一个日志收集器my_logger
        my_logger = logging.getLogger('春衫')

        # 设置级别 全收集
        my_logger.setLevel('DEBUG')

        # 设置输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - 日志信息:%(message)s')

        # 创建一个输出渠道 打印级别
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)

        #日志文件名格式
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        log_name = log_path + "/" + log_file

        #创建日志文件 写入级别
        fh = logging.FileHandler(log_name, encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        # 收集输出对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)

        elif level == 'INFO':
            my_logger.info(msg)

        elif level == 'WARNING':
            my_logger.warning(msg)

        elif level == 'ERROR':
            my_logger.error(msg)

        elif level == 'CRITICAL':
            my_logger.critical(msg)

        # 关闭日志收集器(渠道)
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.user_log(msg, 'DEBUG')

    def info(self, msg):
        self.user_log(msg, 'INFO')

    def error(self, msg):
        self.user_log(msg, 'ERROR')


if __name__ == '__main__':
    pass
    my_logger=UserLog()
    my_logger.debug('测试')
    # my_logger.info('测试')
    # UserLog().user_log('测试一下1', 'ERROR')
    # UserLog().user_log('测试一下2', 'ERROR')
