# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from ui_resources.vending_demo_ui import *
import sys
import os
import rospy
import rosgraph
from std_msgs.msg import String, Float32


class VendingUI(QDialog):
    # define picture locations
    COKE_PIC = './ui_resources/img/coke.jpg'
    SPRITE_PIC = './ui_resources/img/sprite.jpg'
    FANTA_PIC = './ui_resources/img/fanta.jpg'
    STATUS_GREEN = './ui_resources/img/indicator_green.jpg'
    STATUS_RED = './ui_resources/img/indicator_red.jpg'

    # define signals
    DRINK_TEMP_SIGNAL = pyqtSignal(str)
    DRINK_STATS_SIGNAL = pyqtSignal()
    DRINK_READY_SIGNAL = pyqtSignal(str)

    def __init__(self):
        super(VendingUI, self).__init__()
        # initialize parameters
        self.drink_status = '000000'
        self.drink_temp = 20.0
        # initialize ui
        self.init_ui()
        # initialize ROS node
        self.ros_init()

    def init_ui(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # setup drink pictures
        self.ui.labelCoke1.setPixmap(QPixmap(self.COKE_PIC))
        self.ui.labelCoke2.setPixmap(QPixmap(self.COKE_PIC))
        self.ui.labelFanta1.setPixmap(QPixmap(self.FANTA_PIC))
        self.ui.labelFanta2.setPixmap(QPixmap(self.FANTA_PIC))
        self.ui.labelSprite1.setPixmap(QPixmap(self.SPRITE_PIC))
        self.ui.labelSprite2.setPixmap(QPixmap(self.SPRITE_PIC))

        # link signals and slots
        self.DRINK_TEMP_SINGAL.connect(self.update_drink_temp)
        self.DRINK_STATS_SIGNAL.connect(self.update_drink_status)
        self.DRINK_READY_SIGNAL.connect(self.update_drink_ready)

        # link actions
        self.ui.pushButtonRefreshStatus.clicked.connect(self.update_drink_status)
        self.update_drink_status()

    @pyqtSlot(name='update drink status trigger')
    def update_drink_status(self):
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

    @pyqtSlot(str, name='drink temperature string')
    def update_drink_temp(self, t):
        self.ui.lcdNumberTemp.display(t)

    @pyqtSlot(str, name='drink ready to pick')
    def update_drink_ready(self, ready):
        if ready == '1':
            self.ui.labelPickReadyStats.setPixmap(QPixmap(self.STATUS_GREEN))
        else:
            self.ui.labelPickReadyStats.setPixmap(QPixmap(self.STATUS_RED))

    def check_ros_master(self):
        if rosgraph.is_master_online():
            self.ui.labelROSConnectionStats.setPixmap(QPixmap(self.STATUS_GREEN))
        else:
            self.ui.labelROSConnectionStats.setPixmap(QPixmap(self.STATUS_RED))

    def get_ros_master(self):
        uri = os.getenv('ROS_MASTER_URI')
        return uri.split('//')[1]

    # ROS interface setup
    def ros_init(self):
        rospy.init_node('ui', anonymous=True)
        temp_sub = rospy.Subscriber('drink_temp', Float32, self.update_temp_cb)
        stats_sub = rospy.Subscriber('drink_stats', String, self.update_drink_status_cb)
        ready_sub = rospy.Subscriber('drink_ready', String, self.update_drink_ready_cb)

    def update_temp_cb(self, msg):
        self.drink_temp = round(msg.data, 2)
        self.DRINK_TEMP_SIGNAL.emit(str(self.drink_temp) + "'C")
        #self.update_drink_temp()

    def update_drink_status_cb(self, msg):
        self.drink_status = msg.data
        self.DRINK_STATS_SIGNAL.emit()
        #self.update_drink_status()

    def update_drink_ready_cb(self, msg):
        self.DRINK_READY_SIGNAL.emit(msg.data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vending_ui = VendingUI()
    vending_ui.show()
    sys.exit(app.exec_())
