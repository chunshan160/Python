# -*- coding: utf-8 -*-
"""图标"""
import sys
from PyQt5 import QtWidgets, QtGui


class Icon(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        #设置窗口在屏幕上的位置和设置窗口本身的大小,前两个参数是窗口在屏幕上的x和y坐标,后两个参数是窗口本身的宽和高
        self.setGeometry(300, 300, 250, 150)

        self.setWindowTitle("图标")
        #设置程序图标,传路径
        self.setWindowIcon(QtGui.QIcon(r'sample.ico'))


app = QtWidgets.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())
