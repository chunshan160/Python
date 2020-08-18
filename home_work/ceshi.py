#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/18 11:29
# @Author :春衫
# @File :ceshi.py


# coding = utf-8


import csv
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

"""提取并读取数据：获取日期和最高气温"""

filename = 'D:\Pycharm_workspace\home_work\sitka_weather_2014.csv'

# 打开这个文件，将文件对象存储在f中
with open(filename) as f:
    # 创建一个与该文件相关联的阅读器
    reader = csv.reader(f)

    # 返回文件的下一行，前面的代码中，我们只调用了next()一次，因此得到的是文件第一行
    header_row = next(reader)

    # 创建两个为dates和max_temperature的空列表,用来存储从文件中提取的日期和最高气温
    dates, max_temperature = [], []
    # 遍历文件中余下的各行
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        # 每次执行该循环时，我们都将索引1（第二列）的数据附加到max_temperature的末尾
        max = int(row[1])
        max_temperature.append(max)

    """根据数据绘制图形"""
    # dpi:每英寸的点数 figsize:宽高
    fig = plt.figure(dpi=100, figsize=(10, 6))
    # 将日期和最高气温传给plot
    plt.plot(dates, max_temperature, c='red')

    # 设置图形的格式
    plt.title("Daily max temperature,--2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.xticks(pd.date_range('2014-01-01','2014-12-30'),rotation=90)
    #使用autofmt_xdate来绘制倾斜的日期标签，以免彼此重叠
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()