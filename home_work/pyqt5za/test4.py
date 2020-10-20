#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/10/20 12:57
# @Author :春衫
# @File :test4.py


#
# QCalendarWidget
#               日期日历控件，直接继承自QWidget

from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QCalendarWidget')
        self.resize(1500, 800)
        self.iniUI()

    def iniUI(self):
        cw = QCalendarWidget(self)
        cw.setDateRange(QDate(2000, 1, 1), QDate(2099, 10, 10))  # 设置日期范围
        cw.setDateEditAcceptDelay(3000)  # 直接输入年月日所接受的延迟毫秒数
        # cw.setDateEditEnabled(False)#设置 是否可以 通过键盘输入年月日快速修改日期焦点

        ##############################################日期获取
        #
        # cw.monthShown()   #展示当前月份
        # cw.yearShown()    #展示当前年份
        # cw.selectedDate() #已选中的日期（很有可能不是当前的年月，因为可能选中之后 又翻页了换了月份）
        btn = QPushButton(self)
        btn.setText('当前展示年月')
        btn.move(140, 400)
        btn.clicked.connect(lambda: print('当前页面是', cw.yearShown(), '年', cw.monthShown(), '月'))
        btnn = QPushButton(self)
        btnn.setText('打印选中日期')
        btnn.move(250, 400)
        btnn.clicked.connect(lambda: print('选中的日期为:', cw.selectedDate()))
        #############################日期获取

        ########################################################设置日历外观
        cw.setNavigationBarVisible(True)  # 设置导航条是否显示
        cw.setFirstDayOfWeek(Qt.Sunday)  # 设置一周的第一天为周日
        cw.setGridVisible(True)  # 设置日期之间网格显示
        #######################################################设置日历外观

        ##############################################日历文本格式设置
        tcf = QTextCharFormat()
        tcf.setFontFamily('华文新魏')
        tcf.setFontPointSize(20)
        tcf.setFontUnderline(True)
        cw.setHeaderTextFormat(tcf)

        cw.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)  # 不显示第一列的周数编号
        cw.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)  # 将周几改成星期几

        tcf1 = QTextCharFormat()
        tcf1.setFontPointSize(30)
        tcf1.setFontFamily('隶书')
        cw.setWeekdayTextFormat(Qt.Monday, tcf1)  # 设置所有星期一的字符格式

        cw.setDateTextFormat(QDate(2020, 1, 1), tcf1)  # 设置具体某一天的日期格式显示
        #############################日历文本格式设置

        ##############################################日历的常用功能
        btn1 = QPushButton(self)
        btn1.setText('跳转到今天')
        btn1.move(30, 400)
        btn1.clicked.connect(cw.showToday)

        btn2 = QPushButton(self)
        btn2.setText('跳转到选中日期')
        btn2.move(30, 450)
        btn2.clicked.connect(cw.showSelectedDate)

        btn3 = QPushButton(self)
        btn3.setText('上一年')
        btn3.move(30, 500)
        btn3.clicked.connect(cw.showPreviousYear)

        btn4 = QPushButton(self)
        btn4.setText('下一年')
        btn4.move(30, 550)
        btn4.clicked.connect(cw.showNextYear)

        btn5 = QPushButton(self)
        btn5.setText('上个月')
        btn5.move(150, 500)
        btn5.clicked.connect(cw.showPreviousMonth)

        btn6 = QPushButton(self)
        btn6.setText('下个月')
        btn6.move(150, 550)
        btn6.clicked.connect(cw.showNextMonth)

        btn7 = QPushButton(self)
        btn7.setText('跳转到2015年7月')
        btn7.move(100, 600)
        btn7.clicked.connect(lambda: cw.setCurrentPage(2015, 7))

        #############################日历的常用功能

        ##############################################日历控件 信号相关
        #
        # cw.activated.connect(lambda QDate():)
        # cw.clicked.connect(lambda QDate():)
        # cw.currentPageChanged.connect( lambda intYear,intMonth:)
        # cw.selectionChanged.connect(lambda:)  鼠标代码皆能触发
        #
        cw.activated.connect(lambda date: print('鼠标双击（单机+Enter）日期', date))
        cw.clicked.connect(lambda date: print('鼠标单机日期', date))
        cw.currentPageChanged.connect(lambda year, month: print('跳转到了', year, '年', month, '月'))
        cw.selectionChanged.connect(lambda: print('选中了新日期'))
        #############################日历控件 信号相关


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    win = MyWindow()
    win.show()
    sys.exit(app.exec_())