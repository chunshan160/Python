#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/10/20 13:07
# @Author :春衫
# @File :run3.py


import sys
from PyQt5.QtWidgets import *
from pyqt5za.ui import Ui_Form


class ComboxDemo(QDialog,Ui_Form):
    def __init__(self):
        super(ComboxDemo,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("显示matplotlib绘制图形")
        self.setMinimumSize(0,0)

    # 定义搜索按钮的功能
    def onclick(self):
        print(self.comboBox_2.currentText())
        print(self.comboBox_2.currentText())
        print(self.label_3.selectedDate())
        #第五步：定义MyFigure类的一个实例
        self.F = MyFigure(width=3, height=2, dpi=100)
        # self.F.plotsin()
        self.plotcos()
        #第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.F,0,1)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    comboxDemo=ComboxDemo()
    comboxDemo.show()
    comboxDemo.pushButton.clicked.connect(comboxDemo.onclick)
    sys.exit(app.exec_())