#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/9 9:55
# @Author :春衫
# @File :do_excel.py


# 存到Excel里面  python去操作Excel
# 只支持 .xlsx  后缀     openpyxl库只支持该后缀


# from openpyxl import load_workbook
#
# # 打开Excel
# wb = load_workbook("../../learn/xh.xlsx")  # Open the given filename and return the workbook
#
# # 定位表单
# sheet = wb['test']  # 传表单名
#
# # 定位单元格  行列值
# # res=sheet.cell(1,1).value
#
# print("最大行：{}".format(sheet.max_row))
# print("最大列：{}".format(sheet.max_column))
# # print("拿到的结果是:",res)
#
# # 数据从Excel里面拿出来是
# # 数字还是int   其他都是字符串
# print("url:{}，类型是{}".format(sheet.cell(2, 1).value, type(sheet.cell(2, 1).value)))

# eval()把数据类转换成原本数据类型
s = 'True'
print(eval(s),type(eval(s)))
