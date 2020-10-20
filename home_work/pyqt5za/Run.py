#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/28 16:48
# @Author :春衫
# @File :runceshi.py


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import numpy as np
from pyqt5za.ui import Ui_Form

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from read import get_data

#创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self,width=5, height=4, dpi=100):
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #第二步：在父类中激活Figure窗口
        super(MyFigure,self).__init__(self.fig) #此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)


class MainDialogImgBW(QDialog,Ui_Form):
    def __init__(self):
        super(MainDialogImgBW,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("显示matplotlib绘制图形")
        self.setMinimumSize(0,0)

    def plotcos(self):
        data=get_data("D:\Pycharm_workspace\home_work\data.xlsx", "ceshi", None, "修复中")
        x_data = data[0]
        y_data = data[1]
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
        self.F.axes.plot(x_data, y_data)
        plt.xticks(rotation=45)
        self.F.fig.suptitle("cos")

    # 定义搜索按钮的功能
    def onclick(self):
        # 第五步：定义MyFigure类的一个实例
        self.F = MyFigure(width=3, height=2, dpi=100)
        self.plotcos()
        # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.F, 0, 1)

    def save_date(self):
        with open("date.txt","w")as f:
            f.write(self.click_date)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainDialogImgBW()
    main.show()
    main.pushButton.clicked.connect(main.onclick)
    sys.exit(app.exec_())
