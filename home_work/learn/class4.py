#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/10 22:10
# @Author :春衫
# @File :class4.py


# unittest的结合使用 +exce1结合使用--详细讲解注意课后复盘
# 总结:两种unittest+excel 1)超继承 2)ddt
# 类
# unittest 单元测试 通过单元测试 实现对自己写的类的测试
# TestCase self.assert异常处理
# 参数化80% Excel openpyxl
# 写成类方法一 方法二 方法三
# 超继承--->原理要懂  DDT 推荐DDT

# 三个区域
# [section]
# option value   key:value



#配置文件  configparser.ConfigParser()
#properties config ini log4j
#configparser可以 去读取配置信息

import configparser

cf=configparser.ConfigParser()
cf.read('case.config',encoding='utf-8')

# 读取配置文件的数据
print(cf.sections())
print(cf.items('MODE'))


res_1=cf.get('MODE','mode')
print(res_1)

res_2=cf['MODE']['mode']
print(res_2)


#不管是什么数据类型，返回回来的都是str  eval()

