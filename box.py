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
        fun1 = QPushButton("一键环境部署") 
        fun1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        fun2 = QPushButton("取消所有部署")
        fun2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        leftnav.addWidget(fun1)
        leftnav.addWidget(fun2)
        self.groupbox2.setLayout(leftnav)
        
        rightnav = QVBoxLayout()

        rightnav1 = QHBoxLayout()
        fun3 = QPushButton("Shizuku安装/激活")
        fun3.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        fun4 = QPushButton("权限管理ops安装/激活")
        fun4.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        rightnav1.addWidget(fun3)
        rightnav1.addWidget(fun4)
        rightnav.addLayout(rightnav1)

        rightnav2 = QHBoxLayout()
        fun5 = QPushButton("冰箱安装/激活")
        fun5.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        fun6 = QPushButton("无障碍管理安装/激活")
        fun6.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        rightnav2.addWidget(fun5)
        rightnav2.addWidget(fun6)
        rightnav.addLayout(rightnav2)
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
#功能绑定
        fun1.clicked.connect(self.cmd1)
        fun2.clicked.connect(self.cmd2)
        fun3.clicked.connect(self.shizuku)
        fun4.clicked.connect(self.ops)
        fun5.clicked.connect(self.icebox)
        fun6.clicked.connect(self.allin)



        vbox.addLayout(butbox)
        vbox.addWidget(self.groupbox1)


        vbox.addLayout(navbox)
        navbox.addLayout(leftnav)
        navbox.addWidget(self.groupbox2)
        navbox.addLayout(rightnav)
        rightnav.addLayout(rightnav1)
        rightnav.addLayout(rightnav2)
        navbox.addWidget(self.groupbox3)
        vbox.addLayout(contbox)
        contbox.addLayout(leftcon)
        contbox.addWidget(self.groupbox4)
        contbox.addLayout(rightcon)
        contbox.addWidget(self.groupbox5)
        # vbox.addItem(vboxspac)
        self.setLayout(vbox)


    def shizuku(self):
        try:
            name = "moe.shizuku.privileged.api"
            findev = ADBCommand('adb shell "pm list packages | grep moe.shizuku.privileged.api"')
            findev_output = findev.execute()
            self.textdisplay.setText(findev_output)
            if name in findev_output:
                print("shizuku已安装")
                self.textdisplay.setText("激活管理程序已安装")
                reply = QMessageBox.question(self, '应用程序已安装', 'shizuku已安装,是否激活?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.textdisplay.setText("激活中...")
                    cmd = f'adb shell am start -n {name}/moe.shizuku.manager.MainActivity'
                    subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                    active_icebox = f'adb shell sh /storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh'
                    subprocess.check_output(active_icebox, shell=True, stderr=subprocess.STDOUT)
                    self.textdisplay.setText("shizuku已激活,现在可以对程序统一进行激活了")
                else:
                    self.textdisplay.setText("激活失败，请确认无误后再试")

            else:
                raise Exception()
        except:
            print("Shizuku未安装")

            self.textdisplay.setText("检测到Shizuku未安装")
            reply = QMessageBox.question(self, '应用程序未安装', 'Shizuku未安装,是否要安装?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.textdisplay.setText("安装中...")
                apk_path = '.\\PyQtBox\\apk\\shizuku.apk'
                apk_path = os.path.abspath(apk_path)
                cmd = f'adb install "{apk_path}"'
                try:
                    subprocess.check_output(cmd, shell=True,stderr=subprocess.STDOUT)
                    print('安装成功')
                    self.textdisplay.setText("shizuku安装成功")
                except subprocess.CalledProcessError as e:
                    print(e.output.decode('utf-8'))
                    print('shizuku安装失败')
            else:
                print('取消安装')


    def ops(self):
        try:
            name = "rikka.appops"
            findev = ADBCommand('adb shell "pm list packages | grep rikka.appops"')
            findev_output = findev.execute()
            self.textdisplay.setText(findev_output)
            if name in findev_output:
                print("ops已安装")
                self.textdisplay.setText("权限管理程序已安装,请确认shizuku也已经安装")
                reply = QMessageBox.question(self, '应用程序已安装', 'ops已安装,是否激活?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.textdisplay.setText("激活中...")
                    cmd = f'adb shell am start -n {name}/rikka.appops.home.HomeActivity'
                    subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                    # active_icebox = f'adb shell sh /storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh'
                    # subprocess.check_output(active_icebox, shell=True, stderr=subprocess.STDOUT)
                    self.textdisplay.setText("点击以[shizuku模式]激活程序")
                    self.textdisplay.setText("已激活,现在可以对程序统一进行激活了")
                else:
                    self.textdisplay.setText("激活失败，请确认无误后再试")

            else:
                raise Exception()
        except:
            print("ops未安装")

            self.textdisplay.setText("检测到权限管理程序未安装")
            reply = QMessageBox.question(self, '应用程序未安装', '权限管理程序未安装,是否要安装?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.textdisplay.setText("安装中...")
                apk_path = '.\\PyQtBox\\apk\\shizuku.apk'
                apk_path = os.path.abspath(apk_path)
                cmd = f'adb install "{apk_path}"'
                try:
                    subprocess.check_output(cmd, shell=True,stderr=subprocess.STDOUT)
                    print('安装成功')
                    self.textdisplay.setText("权限管理程序安装成功")
                except subprocess.CalledProcessError as e:
                    print(e.output.decode('utf-8'))
                    print('权限管理程序安装失败')
            else:
                print('取消安装')



    def icebox(self):
        # name = "com.merxury.blocker"
        
        try:
            name = "com.catchingnow.icebox"
            findev = ADBCommand('adb shell "pm list packages | grep com.catchingnow.icebox"')
            findev_output = findev.execute()
            self.textdisplay.setText(findev_output)
            if name in findev_output:
                print("冰箱已安装")
                self.textdisplay.setText("冰箱已安装")
                reply = QMessageBox.question(self, '应用程序已安装', '冰箱已安装，是否激活?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.textdisplay.setText("激活中...")
                    cmd = f'adb shell am start -n {name}/com.catchingnow.icebox.activity.mainActivity.MainAppActivity'
                    subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                    active_icebox = f'adb shell sh /sdcard/Android/data/com.catchingnow.icebox/files/start.sh'
                    subprocess.check_output(active_icebox, shell=True, stderr=subprocess.STDOUT)
                    self.textdisplay.setText("冰箱已激活，请点击[普通adb]完成操作")
                else:
                    self.textdisplay.setText("激活失败，请确认无误后再试")

            else:
                raise Exception()
        except:
            print("冰箱未安装")
            # self.textdisplay.setText("检测到冰箱未安装，正在安装中...")
            self.textdisplay.setText("检测到冰箱未安装")
            # findev = ADBCommand("adb install '.\apk\icebox.apk'")
            # findev_output = findev.execute()
            reply = QMessageBox.question(self, '应用程序未安装', '冰箱未安装，是否要安装?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.textdisplay.setText("安装中...")
                apk_path = '.\\PyQtBox\\apk\\icebox.apk'
                apk_path = os.path.abspath(apk_path)
                cmd = f'adb install "{apk_path}"'
                try:
                    subprocess.check_output(cmd, shell=True,stderr=subprocess.STDOUT)
                    print('安装成功')
                    self.textdisplay.setText("冰箱安装成功")
                except subprocess.CalledProcessError as e:
                    print(e.output.decode('utf-8'))
                    print('冰箱安装失败')
            else:
                print('取消安装')
            # self.textdisplay.setText(findev_output)
                # print("冰箱未安装,开始安装...")
                # self.textdisplay.setText("wei")


    def allin(self):
        try:
            name = "com.accessibilitymanager"
            findev = ADBCommand('adb shell "pm list packages | grep com.accessibilitymanager"')
            findev_output = findev.execute()
            self.textdisplay.setText(findev_output)
            if name in findev_output:
                print("无障碍管理已安装")
                self.textdisplay.setText("无障碍功能管理及保活程序已安装,请确认shizuku也已经安装")
                reply = QMessageBox.question(self, '应用程序已安装', '无障碍管理已安装,是否激活?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.textdisplay.setText("激活中...")
                    cmd = f'adb shell am start -n {name}/com.accessibilitymanager.MainActivity'
                    subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                    # active_icebox = f'adb shell sh /storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh'
                    # subprocess.check_output(active_icebox, shell=True, stderr=subprocess.STDOUT)
                    self.textdisplay.setText("点击需要保活的无障碍应用后的开关,以shizuku模式激活")
                    self.textdisplay.setText("点击以[shizuku模式]激活程序")
                    self.textdisplay.setText("已激活,现在可以对无障碍程序统一进行操作了")
                else:
                    self.textdisplay.setText("激活失败，请确认无误后再试")

            else:
                raise Exception()
        except:
            print("无障碍管理未安装")

            self.textdisplay.setText("检测到权限管理程序未安装")
            reply = QMessageBox.question(self, '应用程序未安装', '无障碍应用管理程序未安装,是否要安装?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.textdisplay.setText("安装中...")
                apk_path = '.\\PyQtBox\\apk\\wuzhangai.apk'
                apk_path = os.path.abspath(apk_path)
                cmd = f'adb install "{apk_path}"'
                try:
                    subprocess.check_output(cmd, shell=True,stderr=subprocess.STDOUT)
                    print('安装成功')
                    self.textdisplay.setText("无障碍管理程序安装成功")
                except subprocess.CalledProcessError as e:
                    print(e.output.decode('utf-8'))
                    print('无障碍管理程序安装失败')
            else:
                print('取消安装')


    
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