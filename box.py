import sys
import os
import subprocess
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from comset import ADBCommand


class mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.archui()
    def archui(self):
        self.setGeometry(300, 200, 1280, 720)
        self.setWindowTitle("super box")
        self.setWindowIcon(QIcon('PyQtBox\logo.png'))

        self.groupbox1 = QGroupBox("功能切换",self)
        self.groupbox2 = QGroupBox("Adb命令",self)
        self.groupbox3 = QGroupBox("辅助功能",self)
        self.groupbox4 = QGroupBox("屏显",self)

#总体布局，竖向
        vbox = QVBoxLayout()

#第一个横向布局
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
        self.groupbox1.setLayout(butbox)
        #多功能
#第二个垂直布局
        navbox = QVBoxLayout()
#垂直布局内部的第一个横向布局
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
#垂直布局内部的第二个横向布局
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

        self.groupbox2.setLayout(navbox)
#第三个横向布局
        contbox = QHBoxLayout()
#横向布局内部的第一个网格布局
        leftcon = QGridLayout()
        names = ["g1","g2","g3","g4",
                 "g5","g6","g7","g8",
                 "g9","g21","g32","g43",
                 "g12","g23","g34","g45"
                 ]
        positions = [(i,j) for i in range(4) for j in range(4)]
        for position,name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            leftcon.addWidget(button,*position)

        self.groupbox3.setLayout(leftcon)
        
#横向布局第二个横向布局
        rightcon = QHBoxLayout()
        self.textdisplay = QTextEdit()
        rightcon.addWidget(self.textdisplay)

        self.groupbox4.setLayout(rightcon)

        fun1.clicked.connect(self.cmd1)
        fun2.clicked.connect(self.cmd2)
        fun3.clicked.connect(self.cmd3)
        fun4.clicked.connect(self.cmd4)
        fun5.clicked.connect(self.cmd5)
        fun6.clicked.connect(self.cmd6)
        fun7.clicked.connect(self.cmd7)
        fun8.clicked.connect(self.cmd8)
        fun11.clicked.connect(self.cmd11)
        fun12.clicked.connect(self.cmd12)
        fun13.clicked.connect(self.cmd13)
        fun14.clicked.connect(self.cmd14)
        fun15.clicked.connect(self.cmd15)
        fun16.clicked.connect(self.cmd16)
        fun17.clicked.connect(self.cmd17)
        fun18.clicked.connect(self.cmd18)


        vbox.addLayout(butbox)
        vbox.addWidget(self.groupbox1)

        vbox.addWidget(self.groupbox2)
        vbox.addLayout(navbox)
        navbox.addLayout(navboxup)
        navbox.addLayout(navboxdown)

        vbox.addLayout(contbox)
        contbox.addWidget(self.groupbox3)
        contbox.addLayout(leftcon)
        contbox.addWidget(self.groupbox4)
        contbox.addLayout(rightcon)
        # vbox.addItem(vboxspac)
        self.setLayout(vbox)


    def cmd1(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd2(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd3(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd4(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd5(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd6(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd7(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd8(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd11(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd12(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd13(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd14(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd15(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd16(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd17(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd18(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mainwin()
    win.show()
    sys.exit(app.exec_())