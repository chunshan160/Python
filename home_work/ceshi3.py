#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/10/20 17:16
# @Author :春衫
# @File :ceshi3.py

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


fig,ax  = plt.subplots(1,1)
plt.xticks(rotation=120)   # 设置横坐标显示的角度，角度是逆时针，自己看
tick_spacing = 3    # 设置密度，比如横坐标9个，设置这个为3,到时候横坐标上就显示 9/3=3个横坐标，

x_list = [1,2,3,4,5,6,7,8,9]
y_list = '1 1 1 2 2 2 3 3 3'.split()
ax.plot(x_list,y_list)
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.show()
