# -*- coding: utf-8 -*-
"""消息窗口示例"""
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class MessageBox(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("消息窗口演示程序")

    #重写closeEvent()方法 关闭不直接退出
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self,'确认退出','你确定要退出么？',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

app = QtWidgets.QApplication(sys.argv)
qb = MessageBox()
qb.show()
sys.exit(app.exec_())