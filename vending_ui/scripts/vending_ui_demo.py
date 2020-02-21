#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from ui_resources.vending_demo_ui import *
from LiveCamera import LiveCamera
import sys
import os
import rospy
import rosgraph
from std_msgs.msg import String, Float32


class VendingUI(QDialog):
    # 定义本地图片地址
    COKE_PIC = './ui_resources/img/coke.jpg'
    SPRITE_PIC = './ui_resources/img/sprite.jpg'
    FANTA_PIC = './ui_resources/img/fanta.jpg'
    STATUS_GREEN = './ui_resources/img/indicator_green.jpg'
    STATUS_RED = './ui_resources/img/indicator_red.jpg'

    # 创建信号
    DRINK_TEMP_SIGNAL = pyqtSignal(str)
    DRINK_STATS_SIGNAL = pyqtSignal()
    DRINK_READY_SIGNAL = pyqtSignal(str)

    def __init__(self):
        super(VendingUI, self).__init__()
        # 初始化内部参数
        self.drink_status = '000000'
        self.drink_temp = 20.0
        # 初始化ui界面
        self.init_ui()
        # 初始化ROS节点
        self.ros_init()

    def init_ui(self):
        # 实例化Dialog界面
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 实例化视频线程
        video_thread = LiveCamera(self)

        # 启动线程
        video_thread.start()

        # 设定饮料显示图片
        self.ui.labelCoke1.setPixmap(QPixmap(self.COKE_PIC))
        self.ui.labelCoke2.setPixmap(QPixmap(self.COKE_PIC))
        self.ui.labelFanta1.setPixmap(QPixmap(self.FANTA_PIC))
        self.ui.labelFanta2.setPixmap(QPixmap(self.FANTA_PIC))
        self.ui.labelSprite1.setPixmap(QPixmap(self.SPRITE_PIC))
        self.ui.labelSprite2.setPixmap(QPixmap(self.SPRITE_PIC))

        # 连接信号与槽
        self.DRINK_TEMP_SINGAL.connect(self.update_drink_temp)
        self.DRINK_STATS_SIGNAL.connect(self.update_drink_status)
        self.DRINK_READY_SIGNAL.connect(self.update_drink_ready)
        video_thread.img_signal.connect(self.display_video)

        # 连接预设动作
        self.ui.pushButtonRefreshStatus.clicked.connect(self.update_drink_status)
        self.update_drink_status()

    # 创建饮料状态更新接收槽
    @pyqtSlot()
    def update_drink_status(self):
        # 定义子程序，更新label图片
        def update_label_pixmap(label, status):
            if status == '0':
                label.setPixmap(QPixmap(self.STATUS_RED))
            else:
                label.setPixmap(QPixmap(self.STATUS_GREEN))
        update_label_pixmap(self.ui.labelCoke1_status, self.drink_status[0])
        update_label_pixmap(self.ui.labelCoke2_status, self.drink_status[1])
        update_label_pixmap(self.ui.labelSprite1_status, self.drink_status[2])
        update_label_pixmap(self.ui.labelSprite2_status, self.drink_status[3])
        update_label_pixmap(self.ui.labelFanta1_status, self.drink_status[4])
        update_label_pixmap(self.ui.labelFanta2_status, self.drink_status[5])

    # 创建更新饮料温度接收槽
    @pyqtSlot(str)
    def update_drink_temp(self, t):
        self.ui.lcdNumberTemp.display(t)

    # 创建更新饮料提取状态接收槽
    @pyqtSlot(str)
    def update_drink_ready(self, ready):
        if ready == '1':
            self.ui.labelPickReadyStats.setPixmap(QPixmap(self.STATUS_GREEN))
        else:
            self.ui.labelPickReadyStats.setPixmap(QPixmap(self.STATUS_RED))

    # 创建视频显示更新槽
    @pyqtSlot(QImage)
    def display_video(self, qimg):
        # 转换QImage到Pixmap
        img = QPixmap.fromImage(qimg)
        self.ui.labelVideo.setPixmap(img)

    # 检测ROS启动状态，更新ROS状态显示label
    def check_ros_master(self):
        if rosgraph.is_master_online():
            self.ui.labelROSConnectionStats.setPixmap(QPixmap(self.STATUS_GREEN))
        else:
            self.ui.labelROSConnectionStats.setPixmap(QPixmap(self.STATUS_RED))

    # 获取ROS Master地址系统环境变量
    def get_ros_master(self):
        uri = os.getenv('ROS_MASTER_URI')
        return uri.split('//')[1]

    # ROS节点
    def ros_init(self):
        # 启动ui节点
        rospy.init_node('ui', anonymous=True)
        # 设定消息订阅
        rospy.Subscriber('drink_temp', Float32, self.update_temp_cb)
        rospy.Subscriber('drink_stats', String, self.update_drink_status_cb)
        rospy.Subscriber('drink_ready', String, self.update_drink_ready_cb)

    # 温度更新
    def update_temp_cb(self, msg):
        # 提取数据并保留小数点后2位
        self.drink_temp = round(msg.data, 2)
        # 转换数字为字符串，通过信号发送
        self.DRINK_TEMP_SIGNAL.emit(str(self.drink_temp) + "'C")
        #self.update_drink_temp()

    # 饮料状态更新
    def update_drink_status_cb(self, msg):
        self.drink_status = msg.data
        # 通过消息触发状态更新ui
        self.DRINK_STATS_SIGNAL.emit()
        #self.update_drink_status()

    # 提取状态更新
    def update_drink_ready_cb(self, msg):
        self.DRINK_READY_SIGNAL.emit(msg.data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vending_ui = VendingUI()
    vending_ui.show()
    sys.exit(app.exec_())
