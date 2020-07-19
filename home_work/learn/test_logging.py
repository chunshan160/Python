#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/19 18:00
# @Author :春衫
# @File :test_logging.py


import logging

# logger 收集日志 debug info error
# handdler 输出日志的渠道  指定的文件   还是控制台

# logging.debug('lalala')
# logging.info("77777777")
# logging.warning('小白')
# logging.error('ASDF')
# logging.critical('saaafafa')

# 定义一个日志收集器my_logger
my_logger = logging.getLogger('春衫')

# 设置级别
my_logger.setLevel('DEBUG')

# 设置输出格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - 日志信息:%(message)s')

# 创建一个输出渠道
ch = logging.StreamHandler()
ch.setLevel('DEBUG')
ch.setFormatter(formatter)

fh = logging.FileHandler('python11.txt', encoding='utf-8')
fh.setLevel('DEBUG')
fh.setFormatter(formatter)

# 收集输出对接
my_logger.addHandler(ch)
my_logger.addHandler(fh)

# 收集日志
my_logger.debug("python学习logging")
my_logger.error("Python是最棒的")
