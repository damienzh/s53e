#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap, QImage, QCloseEvent
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread, QSignalMapper
from ui_resources.vending_demo_ui import *
from cvqt_helper import *
from LiveCamera import LiveCamera
from RecogFace import RecogFace
import sys
import os
import subprocess
import time
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
    DRINK_READY_SIGNAL = pyqtSignal()

    # 初始化ui
    def __init__(self):
        super(VendingUI, self).__init__()
        # 初始化内部参数
        self.drink_status = '000000'
        self.drink_temp = 20.0
        self.user_login_status = False
        self.ros_connection = False
        self.drink_order = None
        self.drink_ready = '0'
        # 初始化ui界面
        self.init_ui()
        # 初始化ROS节点
        #self.ros_init()
        # 初始化人脸识别
        self.recognition_init()

    def init_ui(self):
        # 实例化Dialog界面
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 实例化视频线程
        video_thread = LiveCamera(self)

        # 启动线程
        video_thread.start()

        # 设定初始显示文字
        self.ui.labelLoginStatus.setText('未登录')

        # 建立指示与按钮列表
        self.drink_status_list = [self.ui.labelCoke1_status,
                                  self.ui.labelCoke2_status,
                                  self.ui.labelSprite1_status,
                                  self.ui.labelSprite2_status,
                                  self.ui.labelFanta1_status,
                                  self.ui.labelFanta2_status]
        self.drink_button_list = [self.ui.pushButtonCoke1Order,
                                  self.ui.pushButtonCoke2Order,
                                  self.ui.pushButtonSprite1Order,
                                  self.ui.pushButtonSprite2Order,
                                  self.ui.pushButtonFanta1Order,
                                  self.ui.pushButtonFanta2Order]

        # 设定饮料显示图片
        self.ui.labelCoke1.setPixmap(QPixmap(self.COKE_PIC))
        self.ui.labelCoke2.setPixmap(QPixmap(self.COKE_PIC))
        self.ui.labelFanta1.setPixmap(QPixmap(self.FANTA_PIC))
        self.ui.labelFanta2.setPixmap(QPixmap(self.FANTA_PIC))
        self.ui.labelSprite1.setPixmap(QPixmap(self.SPRITE_PIC))
        self.ui.labelSprite2.setPixmap(QPixmap(self.SPRITE_PIC))

        # 连接信号与槽
        self.DRINK_TEMP_SIGNAL.connect(self.update_drink_temp)
        self.DRINK_STATS_SIGNAL.connect(self.update_drink_status)
        self.DRINK_READY_SIGNAL.connect(self.update_drink_ready)
        video_thread.img_signal.connect(self.update_video_frame)

        # 设定饮料订单发送Mapper
        self.order_mapper = QSignalMapper()
        for button in self.drink_button_list:
            button.clicked.connect(self.order_mapper.map)
        for i in range(6):
            self.order_mapper.setMapping(self.drink_button_list[i], str(i))
        self.order_mapper.mapped[str].connect(self.drink_order_ros)

        # 连接预设动作
        self.ui.pushButtonRefreshStatus.clicked.connect(self.update_drink_status)
        self.ui.pushButtonRegister.clicked.connect(self.register_name)
        self.ui.pushButtonLogin.clicked.connect(self.user_login)
        self.ui.pushButtonLogout.clicked.connect(self.user_logout)
        self.ui.pushButtonROSInit.clicked.connect(self.ros_init)

        # 更新初始化状态
        self.update_drink_status()
        self.update_drink_ready()
        self.check_ros_connection()

    # ============================== Slots ===================================
    # 创建饮料状态更新接收槽
    @pyqtSlot()
    def update_drink_status(self):
        # 定义子程序，更新label图片
        def update_label_pixmap(label, status):
            if status == '0':
                label.setPixmap(QPixmap(self.STATUS_RED))
            else:
                label.setPixmap(QPixmap(self.STATUS_GREEN))
        for i in range(6):
            update_label_pixmap(self.drink_status_list[i], self.drink_status[i])

    # 创建更新饮料温度接收槽
    @pyqtSlot(str)
    def update_drink_temp(self, t):
        self.ui.lcdNumberTemp.display(t)

    # 创建更新饮料提取状态接收槽
    @pyqtSlot()
    def update_drink_ready(self):
        if self.drink_ready == '1':
            self.ui.labelPickReadyStats.setPixmap(QPixmap(self.STATUS_GREEN))
        else:
            self.ui.labelPickReadyStats.setPixmap(QPixmap(self.STATUS_RED))

    # 创建视频显示更新槽
    @pyqtSlot(QImage)
    def update_video_frame(self, qimg):
        self.display_video(qimg)

    def closeEvent(self, QCloseEvent):
        if self.ros_master:
            rospy.signal_shutdown('closing ui')
            self.ros_master.terminate()
    # ============================  Video / Face Recognition ========================
    # 初始化人脸识别
    def recognition_init(self):
        self.face_recognition = RecogFace()
        self.face_detected = False
        self.face_recognition.load_known_faces()

    # 侦测识别当前帧中的人脸
    def recognize_face(self, qimg):
        cv_img = qimage_to_cv(qimg)
        face_img = self.face_recognition.detection(cv_img)
        return cv_to_qimg(face_img)

    # 视频显示更新
    def display_video(self, qimg):
        if self.ui.checkBoxFaceRecognition.isChecked():
            # 执行人脸识别，并转换QImage到Pixmap
            img = QPixmap.fromImage(self.recognize_face(qimg))
        else:
            img = QPixmap.fromImage(qimg)
        self.ui.labelVideo.setPixmap(img)

    # 创建注册用户弹出输入窗口
    def register_name(self):
        (name, ok) = QInputDialog.getText(self, '注册新用户', '请输入用户名', QLineEdit.Normal)
        if self.face_recognition.face_detected:
            print 'face detected'
            self.face_recognition.add_face(qimage_to_cv(self.video_frame), name)

    def user_login(self):
        if not self.user_login_status:
            if self.face_recognition.face_detected:
                if not self.face_recognition.detected_name == '':
                    self.user_login_status = True
                    self.ui.labelLoginStatus.setText(self.face_recognition.detected_name)

    def user_logout(self):
        if self.user_login_status:
            self.user_login_status = False
            self.ui.labelLoginStatus.setText('未登录')

    # ===============================  ROS ====================================
    # 获取ROS Master地址系统环境变量
    def get_ros_master(self):
        uri = os.getenv('ROS_MASTER_URI')
        return uri.split('//')[1]

    def set_ros_master(self):
        uri = self.ui.lineEdit.text()
        os.putenv('ROS_MASTER_URI', 'http://'+uri)

    def start_ros_master(self):
        self.ros_master = subprocess.Popen('roscore', stdin=subprocess.PIPE,
                                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(2)

    # 检测ROS启动状态，更新ROS状态显示label
    def check_ros_connection(self):
        if rosgraph.is_master_online():
            self.ui.labelROSConnectionStats.setPixmap(QPixmap(self.STATUS_GREEN))
            return True
        else:
            self.ui.labelROSConnectionStats.setPixmap(QPixmap(self.STATUS_RED))
            return False

    # 启动ROS节点
    def ros_init(self):
        self.start_ros_master()
        if rosgraph.is_master_online():
            # 启动ui节点
            rospy.init_node('ui', anonymous=True, disable_signals=True)
            if self.check_ros_connection():
                self.ros_connection = True
            # 设定消息订阅
            rospy.Subscriber('drink_temp', Float32, self.update_temp_cb)
            rospy.Subscriber('drink_stats', String, self.update_drink_status_cb)
            rospy.Subscriber('drink_ready', String, self.update_drink_ready_cb)
            # 设定消息发布
            self.pick_cmd = rospy.Publisher('drink_order', String, queue_size=1)
        else:
            QMessageBox.warning(self, 'ROS Warning', 'No ROS Master', QMessageBox.Ok)

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
        self.drink_ready = msg.data
        self.DRINK_READY_SIGNAL.emit()

    # 发布饮料订单
    def drink_order_ros(self, cmd):
        msg = String()
        msg.data = cmd
        self.pick_cmd.publish(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vending_ui = VendingUI()
    vending_ui.show()
    sys.exit(app.exec_())
