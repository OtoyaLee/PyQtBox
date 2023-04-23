import sys
import os
import subprocess
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from comset import ADBCommand



class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        # 设置对话框标题和大小
        self.setWindowTitle("高级模式")
        self.setGeometry(300, 200, 1280, 720)
        self.fastbootbox = QGroupBox("Fastboot刷入")
        self.recoverybox = QGroupBox("Recovery刷入")
        # self.fastbootbox = QGroupBox("Fastboot刷入")

        vtbox = QVBoxLayout()
        #FASTBOOT刷入区域
        htbox = QHBoxLayout()
        # label = QLabel("path:")
        htvbox = QVBoxLayout()
        self.select_button = QPushButton("选择")
        # self.select_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.path_label = QLabel()
        # self.path_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.device_button = QPushButton("刷新设备")
        # self.device_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.flash_button = QPushButton("刷入")
        # self.flash_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        vtabox = QVBoxLayout()
        self.p1 = QLabel("1:点击【一键进入fastboot】,或者按住【音量-】和【电源键】5s进入fastboot模式")
        self.p2 = QLabel("2:点击【设备】按钮刷新设备")
        self.p3 = QLabel("3:点击【选择】按钮,选择已经解压后的线刷包")
        self.p4 = QLabel("4:点击【刷入】按钮")
        self.p5 = QLabel("5:等待大约5~20分钟,刷入后自动重启")

        vtabox.addWidget(self.p1)
        vtabox.addWidget(self.p2)
        vtabox.addWidget(self.p3)
        vtabox.addWidget(self.p4)
        vtabox.addWidget(self.p5)




        self.select_button.clicked.connect(self.select_file)
        self.device_button.clicked.connect(self.device_display)
        self.flash_button.clicked.connect(self.flash_device)


        htvbox.addWidget(self.select_button)
        # htbox.addWidget(label)
        htvbox.addWidget(self.path_label)
        htvbox.addWidget(self.device_button)
        htvbox.addWidget(self.flash_button)
        htbox.addLayout(htvbox)
        htbox.addLayout(vtabox)
        self.fastbootbox.setLayout(htbox)

        vtbox2 = QVBoxLayout()
        self.text1 = QLabel("1:点击【一键进入rec】,或者按住【音量+】和【电源键】5s进入rec模式")
        self.text1.setWordWrap(True)
        self.text2 = QLabel("2:进入rec后,点击【清除】按钮进入擦除与格式页面,如需【双清】,滑动[恢复出厂设置]按钮,或者在【高级清除选项】中勾选[data]和[cache]分区后,【滑动按钮确认清除】")
        self.text3 = QLabel("3:在【高级清除选项】中,如需[三清],则勾选[data]、[cache]、[dalvik cache]后,【滑动按钮确认清除】")
        self.text4 = QLabel("4:在【高级清除选项】中,如需[四清],则勾选[data]、[cache]、[dalvik cache],外加一个[system]分区后,【滑动按钮确认清除】")
        self.text5 = QLabel("5:如果在rec中遇到乱码、无法解密data等情况,需要在【清除】页面点击【格式化data分区】按钮后,根据提示输入[yes]再点击回车后完成操作")
        self.recbt = QPushButton("一键进入rec")

        self.recbt.clicked.connect(self.recflash)
        
        vtbox2.addWidget(self.text1)
        vtbox2.addWidget(self.text2)
        vtbox2.addWidget(self.text3)
        vtbox2.addWidget(self.text4)
        vtbox2.addWidget(self.text5)
        vtbox2.addWidget(self.recbt)

        self.recoverybox.setLayout(vtbox2)



        vtbox.addLayout(htbox)
        vtbox.addWidget(self.fastbootbox)
        vtbox.addLayout(vtbox2)
        vtbox.addWidget(self.recoverybox)
        self.setLayout(vtbox)


    def select_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "选择需要刷入的文件", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_path:
            self.path_label.setText(file_path)

    def device_display(self):
        print("你好！")

    def flash_device(self):
        print("大家好！")

    def recflash(self):
        print("youxi")


class mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.archui()
    def archui(self):
        self.setGeometry(300, 200, 1280, 720)
        self.setWindowTitle("super box")
        self.setWindowIcon(QIcon('PyQtBox\logo.png'))

        self.groupbox1 = QGroupBox("功能切换",self)
        self.groupbox2 = QGroupBox("环境配置",self)
        self.groupbox3 = QGroupBox("软件安装/激活",self)
        self.groupbox4 = QGroupBox("屏幕损坏辅助功能",self)
        self.groupbox5 = QGroupBox("屏显",self)

#总体布局，竖向
        vbox = QVBoxLayout()

#第一个横向布局
        butbox = QHBoxLayout()
        bt1 = QPushButton("设备控制")
        bt2 = QPushButton("高级模式")
        bt3 = QPushButton("还没想好")
        bt4 = QPushButton("作者信息")
        butbox.addWidget(bt1)
        butbox.addWidget(bt2)
        butbox.addWidget(bt3)
        butbox.addWidget(bt4)
        vboxspac = QSpacerItem(20,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        self.groupbox1.setLayout(butbox)
        bt2.clicked.connect(self.show_dialog)
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
        names = ["主页","返回","音量+","音量-",
                 "背光+","背光-","菜单","通知栏",
                 "点亮屏幕","滑动屏幕(左滑)","滑动屏幕(右滑)","滑动屏幕(上滑)",
                 "滑动屏幕(下滑)","关机","重启","截图"
                 ]
        for i in range(4):
            for j in range(4):
                index = i * 4 + j # 计算当前按钮在列表中的索引
                name = names[index]
                button = QPushButton(text=name) # 设置按钮的text属性
                button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                button.setMaximumWidth(250)
                button.clicked.connect(self.cmdall) # 添加clicked信号的槽函数
                leftcon.addWidget(button, i, j)
        # positions = [(i,j) for i in range(4) for j in range(4)]
        # for position,name in zip(positions,names):
        #     if name == '':
        #         continue
            # button = QPushButton(name)
            # button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
            # button.setMaximumWidth(250)
            # leftcon.addWidget(button,*position)

        self.groupbox4.setLayout(leftcon)

#横向布局第二个横向布局
        rightcon = QHBoxLayout()
        self.textdisplay = QTextEdit()
        rightcon.addWidget(self.textdisplay)
        self.groupbox5.setLayout(rightcon)
#功能绑定
        # fun1.clicked.connect(self.cmd1)
        # fun2.clicked.connect(self.cmd2)
        fun3.clicked.connect(self.shizuku)
        fun4.clicked.connect(self.ops)
        fun5.clicked.connect(self.icebox)
        fun6.clicked.connect(self.allin)




        # button.clicked.connect(self.cmd1)
        # fun7.clicked.connect(self.cmd2)
        # fun7.clicked.connect(self.cmd3)
        # fun7.clicked.connect(self.cmd4)
        # fun7.clicked.connect(self.cmd5)
        # fun7.clicked.connect(self.cmd6)
        # fun7.clicked.connect(self.cmd7)
        # fun7.clicked.connect(self.cmd8)
        # fun7.clicked.connect(self.cmd11)
        # fun7.clicked.connect(self.cmd12)
        # fun7.clicked.connect(self.cmd13)
        # fun7.clicked.connect(self.cmd14)
        # fun7.clicked.connect(self.cmd15)
        # fun7.clicked.connect(self.cmd16)
        # fun7.clicked.connect(self.cmd17)
        # fun7.clicked.connect(self.cmd18)



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


    def cmdall(self):
        btn = self.sender()
        if btn.text() == "主页":
            findev = ADBCommand("adb devices")
            findev_output = findev.execute()
            self.textdisplay.setText(findev_output)
        elif btn.text() == "返回":
            self.count += 1
            findev = ADBCommand("adb shell input keyevent 4")
            findev_output = findev.execute()
            # self.textdisplay.setText(findev_output)
            self.textdisplay.setText(f"返回{self.count}次")
        elif btn.text() == "音量+":
            self.count = 0
            findev = ADBCommand("adb shell input keyevent 24")
            findev_output = findev.execute()
            # self.textdisplay.setText(findev_output)
            self.textdisplay.setText(f"音量+1")
        elif btn.text() == "音量-":
            findev = ADBCommand("adb shell input keyevent 25")
            findev_output = findev.execute()
            # self.textdisplay.setText(findev_output)
            self.textdisplay.setText(f"音量-1")
        elif btn.text() == "背光+":
            findev = ADBCommand("adb shell input leyevent 224 && adb shell input keyevent 221")
            findev_output = findev.execute()
            # self.textdisplay.setText(findev_output)
            self.textdisplay.setText(f"背光+10")
        elif btn.text() == "背光-":
            findev = ADBCommand("adb shell input keyevent KEYCODE_BRIGHTNESS_DOWN")
            findev_output = findev.execute()
            # self.textdisplay.setText(findev_output)
            self.textdisplay.setText(f"背光-10")
        elif btn.text() == "菜单":
            findev = ADBCommand("adb shell input keyevent KEYCODE_MENU")
            findev_output = findev.execute()
            # self.textdisplay.setText(findev_output)
            self.textdisplay.setText(f"菜单显示")
        elif btn.text() == "通知栏":
            findev = ADBCommand("adb shell input keyevent KEYCODE_NOTIFICATION")
            findev_output = findev.execute()
            # self.textdisplay.setText(findev_output)
            self.textdisplay.setText(f"开启/关闭通知栏")
        elif btn.text() == "点亮/关闭屏幕":
            findev = ADBCommand("adb shell input keyevent KEYCODE_POWER")
            findev_output = findev.execute()
            self.textdisplay.setText(f"按下电源键")
        elif btn.text() == "滑动屏幕(左滑)":
            findev = ADBCommand("adb shell input swpie 960 540 50 540 500")
            findev_output = findev.execute()
            self.textdisplay.setText(f"左滑屏幕")
        elif btn.text() == "滑动屏幕(右滑)":
            findev = ADBCommand("adb shell input swipe 100 540 960 540 500")
            findev_output = findev.execute()
            self.textdisplay.setText(f"右滑屏幕")
        elif btn.text() == "滑动屏幕(上滑)":
            findev = ADBCommand("adb devices")
            findev_output = findev.execute()
            self.textdisplay.setText(findev_output)
        elif btn.text() == "滑动屏幕(下滑)":
            findev = ADBCommand("adb devices")
            findev_output = findev.execute()
            self.textdisplay.setText(findev_output)
        elif btn.text() == "关机":
            findev = ADBCommand("adb shell reboot -p")
            findev_output = findev.execute()
            self.textdisplay.setText(f"关机")
        elif btn.text() == "重启":
            findev = ADBCommand("adb reboot")
            findev_output = findev.execute()
            self.textdisplay.setText(f"重启")
        elif btn.text() == "截图":
            # findev = ADBCommand("adb shell screencap \\sdcard\\screenshot.png && adb pull \\sdcard\\screenshot.png .\\PyQtBox\\Screen")
            # findev_output = findev.execute()
            # self.textdisplay.setText(f"截图")
            img_path = '/data/local/tmp/screenshot.png'
            # img_path= os.path.abspath(img_path)
            to_path = '.\\PyQtBox\\img\\screen.png'
            to_path = os.path.abspath(to_path)
            cmd = f'adb shell screencap "{img_path}" && adb pull "{img_path}" "{to_path}" '
            try:
                subprocess.check_output(cmd, shell=True,stderr=subprocess.STDOUT)
                print('截图成功')
                self.textdisplay.setText("截图成功,并已传送至img文件夹")
            except subprocess.CalledProcessError as e:
                print(e.output.decode('utf-8'))
                print('截图失败')

    def show_dialog(self):
        # 创建并显示新对话框
        dialog = MyDialog()
        dialog.exec_()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mainwin()
    win.show()
    sys.exit(app.exec_())