# -*- coding: utf-8 -*-
"""我的程序"""
import sys
from PyQt5 import QtWidgets, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(350, 250)
        self.setWindowTitle("我的程序")
        text_edit = QtWidgets.QTextEdit()
        self.setCentralWidget(text_edit)

        exit_action = QtWidgets.QAction(QtGui.QIcon(r"sample.png"), "退出", self)
        exit_action.setStatusTip("退出程序")
        exit_action.setShortcut("Ctrl+Q")
        #将 action 对象的triggered()信号连接到预定义的quit()槽函数
        exit_action.triggered.connect(QtWidgets.qApp.quit)

        self.statusBar()

        self.menu_bar = self.menuBar()
        file = self.menu_bar.addMenu("文件")
        file.addAction(exit_action)
        #创建一个工具栏
        self.toolbar = self.addToolBar("退出")
        #使用语句 self.toolbar.addAction(self.exit)将 action 对象（这里是 exit）添加到该工具栏
        self.toolbar.addAction(exit_action)

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
