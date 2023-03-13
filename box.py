import sys
import os
# from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.archui()
    def archui(self):
        self.setGeometry(300, 200, 1280, 720)
        self.setWindowTitle("super box")
        self.setWindowIcon(QIcon('PyQtBox\logo.png'))
        vbox = QVBoxLayout()
        #切换page
        butbox = QHBoxLayout()
        bt1 = QPushButton("设备控制")
        bt2 = QPushButton("还没想好")
        bt3 = QPushButton("高级模式")
        bt4 = QPushButton("作者信息")
        butbox.addWidget(bt1)
        butbox.addWidget(bt2)
        butbox.addWidget(bt3)
        butbox.addWidget(bt4)
        vboxspac = QSpacerItem(20,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        #多功能
        navbox = QVBoxLayout()
        navboxup = QHBoxLayout()
        fun1 = QPushButton("fun1")
        fun2 = QPushButton("fun1")
        fun3 = QPushButton("fun1")
        fun4 = QPushButton("fun1")
        fun5 = QPushButton("fun1")
        fun6 = QPushButton("fun1")
        fun7 = QPushButton("fun1")
        fun8 = QPushButton("fun1")
        navboxup.addWidget(fun1)
        navboxup.addWidget(fun2)
        navboxup.addWidget(fun3)
        navboxup.addWidget(fun4)
        navboxup.addWidget(fun5)
        navboxup.addWidget(fun6)
        navboxup.addWidget(fun7)
        navboxup.addWidget(fun8)
        navboxdown = QHBoxLayout()
        fun11 =QPushButton("fun1")
        fun12 =QPushButton("fun1")
        fun13 =QPushButton("fun1")
        fun14 =QPushButton("fun1")
        fun15 =QPushButton("fun1")
        fun16 =QPushButton("fun1")
        fun17 =QPushButton("fun1")
        fun18 =QPushButton("fun1")
        navboxdown.addWidget(fun11)
        navboxdown.addWidget(fun12)
        navboxdown.addWidget(fun13)
        navboxdown.addWidget(fun14)
        navboxdown.addWidget(fun15)
        navboxdown.addWidget(fun16)
        navboxdown.addWidget(fun17)
        navboxdown.addWidget(fun18)
        contbox = QHBoxLayout()
        vbox.addLayout(butbox)
        vbox.addLayout(navbox)
        navbox.addLayout(navboxup)
        navbox.addLayout(navboxdown)
        vbox.addLayout(contbox)
        vbox.addItem(vboxspac)
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mainwin()
    win.show()
    sys.exit(app.exec_())