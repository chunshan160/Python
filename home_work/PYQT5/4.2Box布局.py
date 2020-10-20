# -*- coding: utf-8 -*-
"""Box定位演示"""

import sys
from PyQt5 import QtWidgets


class BoxLayout(QtWidgets.QWidget):
    def __init__(self):
        super(BoxLayout, self).__init__()

        self.setWindowTitle("Box定位演示程序")
        #创建两个按钮（确定和取消按钮）
        self.ok_button = QtWidgets.QPushButton("确定")
        self.cancel_button = QtWidgets.QPushButton("取消")

        #创建一个水平 box 布局，然后加入一个伸缩间隔元素与两个按钮
        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addStretch(1)
        self.h_box.addWidget(self.ok_button)
        self.h_box.addWidget(self.cancel_button)

        #创建了一个垂直 box 布局并将水平 box 布局放入水平 box 布局中
        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addStretch(1)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

        self.resize(300, 150)

app = QtWidgets.QApplication(sys.argv)
box_layout = BoxLayout()
box_layout.show()
sys.exit(app.exec_())
