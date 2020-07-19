#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/13 16:55
# @Author :春衫
# @File :test_pandas.py

import pandas as pd
import numpy as np
from API_AUTO.tools.project_path import *

# df = pd.read_excel(test_case_path,sheet_name='init')
# # print(df.values)#输出嵌套列表
# print(df.iloc[1,2])#原ix方法已经废弃  输出 一维矩阵

# loc——通过行标签索引行数据
# iloc——通过行号索引行数据  替换ix

# print(df.loc[[0,0],'tel'].values)#转换输出格式
# print(df.loc[:,'tel'].values)#输出全部匹配标签的数据
# print(df.loc[0,['tel']].values)
# print(df.loc[0,['tel']].to_dict())#以字典形式输出第一行
# print(df.loc[:,['tel']].to_dict())

# print(df.index.values)#索引  从0开始
# test_data = []
# for i in df.index.values:
#     row_data = df.loc[
#         i, ['tel', 'title', 'url', 'data', 'http_method', 'expected_status', 'expected_code',
#             'expected_msg']].to_dict()
#     test_data.append(row_data)
#
# print(test_data)


data = {'name': ['Joe', 'Mike', 'Jack', 'Rose', 'David', 'Marry', 'Wansi', 'Sidy', 'Jason', 'Even'],

        'age': [25, 32, 18, np.nan, 15, 20, 41, np.nan, 37, 32],

        'gender': [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],

        'isMarried': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)

# print(df)
# print(df[:])#全部
# print(df[0:1])#输出前（第）一行
# print(df[0:2])#输出前两行
# print(df[:"a"])#输出该行
# print(df["a":])#输出全部
# print(df["a":"d"])#输出a 到 d 行
# print(df[[True,True,True,False,False,False,False,False,False,False]])#选取前三行  True和False控制是否输出这一行
# print(df[[each > 30 for each in df['age']]])  # 选取所有age大于30的行
# print(df[df['age']>30])# 选取所有age大于30的行
# print(df[(df['age']>30) & (df['isMarried']=='no')])#选取出所有age大于30，且isMarried为no的行
# print(df[(df['age'] == 20) | (df['age'] == 32)])  # 选取出所有age为20或32的行

# print(df.loc[:, ['name','age','isMarried']])
print(df.loc[:, 'name'])