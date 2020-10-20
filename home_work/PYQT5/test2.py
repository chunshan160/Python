# -*- coding: utf-8 -*-
"""网格布局跨行示例"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class GridLayout(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("网格布局跨行演示程序")

        main_ground = QtWidgets.QWidget()
        self.setCentralWidget(main_ground)

        #创建了一个网格布局，并将该布局中的部件间隔（同行的横向间隔）设为 20 个字距
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(20)

        grid.addWidget(QtWidgets.QLabel("标题:"), 1, 0)
        # grid.addWidget(QtWidgets.QLineEdit(), 1, 1)

        grid.addWidget(QtWidgets.QLabel("ceshi:"), 1, 2)
        # grid.addWidget(QtWidgets.QLineEdit(), 1, 3)

        grid.addWidget(QtWidgets.QLabel("作者:"), 2, 0)
        # grid.addWidget(QtWidgets.QLineEdit(), 2, 1)

        grid.addWidget(QtWidgets.QLabel("评论:"), 3, 0)
        #为加入网格布局的部件设置行列跨度，在上面的语句中，我们将 reviewEdit部件的行跨度设置为 5，列跨度设置为 1
        # grid.addWidget(QtWidgets.QTextEdit(), 3, 1, 5, 1)#行 列 行跨度 列跨度


        main_ground.setLayout(grid)
        self.resize(350, 300)

app = QtWidgets.QApplication(sys.argv)
grid_layout = GridLayout()
grid_layout.show()
sys.exit(app.exec_())

currentText()