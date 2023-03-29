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
        self.groupbox2 = QGroupBox("环境配置",self)
        self.groupbox3 = QGroupBox("软件安装/激活",self)
        self.groupbox4 = QGroupBox("辅助功能",self)
        self.groupbox5 = QGroupBox("屏显",self)

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
#第二个横向布局
        navbox = QHBoxLayout()
#横向布局内部的第一个横向布局
#内部为纵向布局
        leftnav = QVBoxLayout()
        fun1 = QPushButton("显示设备") 
        # fun1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # fun1.setMaximumWidth(50)
        # fun1.setMaximumHeight(50)
        fun2 = QPushButton("2")
        leftnav.addWidget(fun1)
        leftnav.addWidget(fun2)
        self.groupbox2.setLayout(leftnav)
        
        rightnav = QHBoxLayout()
        fun3 = QPushButton("jkasdfj")
        fun4 = QPushButton("huds")
        rightnav.addWidget(fun3)
        rightnav.addWidget(fun4)
        # navbox.addLayout(navboxleft)
        self.groupbox3.setLayout(rightnav)
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
            button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
            button.setMaximumWidth(250)
            leftcon.addWidget(button,*position)

        self.groupbox4.setLayout(leftcon)
        
#横向布局第二个横向布局
        rightcon = QHBoxLayout()
        self.textdisplay = QTextEdit()
        rightcon.addWidget(self.textdisplay)
        self.groupbox5.setLayout(rightcon)

        fun1.clicked.connect(self.cmd1)
        fun2.clicked.connect(self.cmd2)



        vbox.addLayout(butbox)
        vbox.addWidget(self.groupbox1)


        vbox.addLayout(navbox)
        navbox.addLayout(leftnav)
        navbox.addWidget(self.groupbox2)
        navbox.addLayout(rightnav)
        navbox.addWidget(self.groupbox3)
        vbox.addLayout(contbox)
        contbox.addLayout(leftcon)
        contbox.addWidget(self.groupbox4)
        contbox.addLayout(rightcon)
        contbox.addWidget(self.groupbox5)
        # vbox.addItem(vboxspac)
        self.setLayout(vbox)


    def cmd1(self):
        findev = ADBCommand("adb devices")
        findev_output = findev.execute()
        self.textdisplay.setText(findev_output)
    def cmd2(self):
        findev = ADBCommand("adb shell  settings list system")
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