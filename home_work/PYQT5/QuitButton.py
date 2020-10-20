# -*- coding: utf-8 -*-
"""用按钮关闭程序"""
import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class QuitButton(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("我的关闭程序")

        #创建一个按钮并将其放在QWidget部件上，就像我们将QWidget部件放在屏幕上一样
        quit_button = QtWidgets.QPushButton("关闭", self)
        quit_button.setGeometry(10, 10, 60, 35)

        #QtCore.QObject.connect()方法可以将信号和槽函数连接起来
        quit_button.clicked.connect(QtWidgets.qApp.quit)


app = QtWidgets.QApplication(sys.argv)
quitbutton = QuitButton()
quitbutton.show()
sys.exit(app.exec_())
