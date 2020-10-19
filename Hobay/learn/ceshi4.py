#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/10/19 17:17
# @Author :春衫
# @File :ceshi4.py

import sys,os
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate


class CalendarExample(QWidget):
    def __init__(self):
        super(CalendarExample, self).__init__()
        self.cal = QCalendarWidget(self)
        self.label = QLabel(self)
        self.click_date=""
        self.initUI()



    def initUI(self):
        self.setGeometry(100, 100, 400, 350)
        self.setWindowTitle("Calendar 例子")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.cal.setMinimumDate(QDate(1980, 1, 1))
        self.cal.setMaximumDate(QDate(3000, 1, 1))
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.cal.clicked[QtCore.QDate].connect(self.showDate)
        date = self.cal.selectedDate()
        self.label.setText(date.toString("yyyy-MM-dd"))
        self.label.move(20, 300)

        self.col = QColor(0, 0, 0)
        redb = QPushButton('确认', self)
        redb.setCheckable(True)
        redb.move(300, 300)
        # 添加按钮点击事件
        redb.clicked.connect(self.on_click)

    def showDate(self, date):
        self.label.setText(date.toString("yyyy-MM-dd"))

    # 按钮点击事件
    def on_click(self):
        self.click_date=self.label.text()
        self.close()
        self.save_date()


    def save_date(self):
        with open("date.txt","w")as f:
            f.write(self.click_date)


def select_date():
    app = QApplication(sys.argv)
    win=CalendarExample()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    select_date()
    #保存文件是为了后续程序能使用该选择的日期
