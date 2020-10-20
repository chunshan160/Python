# -*- coding: utf-8 -*-
"""网格布局示例"""

import sys
from PyQt5 import QtWidgets


class GridLayout(QtWidgets.QMainWindow):
    def __init__(self):
        super(GridLayout, self).__init__()

        self.setWindowTitle("网格布局演示程序")
        buttton_names = ['Cls', 'Bck', '', 'Close',
                         '7', '8', '9', '/',
                         '4', '5', '6', '*',
                         '1', '2', '3', '-',
                         '0', '.', '=', '+']

        #创建了一个QtWidgets.QWidget类的实例main_ground，然后setCentralWidget方法将它置为中心部件
        main_ground = QtWidgets.QWidget()
        self.setCentralWidget(main_ground)

        #创建了一个网格布局
        grid = QtWidgets.QGridLayout()

        #使用 addWidget()方法，我们将部件加入到网格布局中。addWidget()方法的参数依次为要加入到局部的部件，行号和列号
        for [n, (x, y)] in enumerate([(i, j) for i in range(5) for j in range(4)]):
            if (x, y) == (0, 2):
                grid.addWidget(QtWidgets.QLabel(buttton_names[n]), x, y)
            else:
                grid.addWidget(QtWidgets.QPushButton(buttton_names[n]), x, y)
        main_ground.setLayout(grid)

app = QtWidgets.QApplication(sys.argv)
grid_layout = GridLayout()
grid_layout.show()
sys.exit(app.exec_())
