# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vending_demo_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 768)
        self.groupBoxIdentity = QtWidgets.QGroupBox(Dialog)
        self.groupBoxIdentity.setGeometry(QtCore.QRect(30, 20, 961, 371))
        self.groupBoxIdentity.setObjectName("groupBoxIdentity")
        self.LabelVideo = QtWidgets.QLabel(self.groupBoxIdentity)
        self.LabelVideo.setGeometry(QtCore.QRect(40, 30, 480, 320))
        self.LabelVideo.setFrameShape(QtWidgets.QFrame.Box)
        self.LabelVideo.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelVideo.setObjectName("LabelVideo")
        self.pushButtonRegister = QtWidgets.QPushButton(self.groupBoxIdentity)
        self.pushButtonRegister.setGeometry(QtCore.QRect(550, 40, 101, 31))
        self.pushButtonRegister.setObjectName("pushButtonRegister")
        self.groupBoxVending = QtWidgets.QGroupBox(Dialog)
        self.groupBoxVending.setGeometry(QtCore.QRect(30, 400, 961, 351))
        self.groupBoxVending.setObjectName("groupBoxVending")
        self.pushButtonRefreshStatus = QtWidgets.QPushButton(self.groupBoxVending)
        self.pushButtonRefreshStatus.setGeometry(QtCore.QRect(800, 20, 75, 23))
        self.pushButtonRefreshStatus.setObjectName("pushButtonRefreshStatus")
        self.layoutWidget = QtWidgets.QWidget(self.groupBoxVending)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 50, 961, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxCoke1 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBoxCoke1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxCoke1.setObjectName("groupBoxCoke1")
        self.labelCoke1 = QtWidgets.QLabel(self.groupBoxCoke1)
        self.labelCoke1.setGeometry(QtCore.QRect(20, 25, 120, 200))
        self.labelCoke1.setText("")
        self.labelCoke1.setPixmap(QtGui.QPixmap("img/coke.jpg"))
        self.labelCoke1.setScaledContents(True)
        self.labelCoke1.setObjectName("labelCoke1")
        self.labelCoke1_status = QtWidgets.QLabel(self.groupBoxCoke1)
        self.labelCoke1_status.setGeometry(QtCore.QRect(20, 240, 20, 20))
        self.labelCoke1_status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelCoke1_status.setScaledContents(True)
        self.labelCoke1_status.setObjectName("labelCoke1_status")
        self.pushButtonCoke1Order = QtWidgets.QPushButton(self.groupBoxCoke1)
        self.pushButtonCoke1Order.setGeometry(QtCore.QRect(50, 240, 75, 23))
        self.pushButtonCoke1Order.setObjectName("pushButtonCoke1Order")
        self.horizontalLayout.addWidget(self.groupBoxCoke1)
        self.groupBoxCoke2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBoxCoke2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxCoke2.setObjectName("groupBoxCoke2")
        self.labelCoke2 = QtWidgets.QLabel(self.groupBoxCoke2)
        self.labelCoke2.setGeometry(QtCore.QRect(20, 25, 120, 200))
        self.labelCoke2.setText("")
        self.labelCoke2.setPixmap(QtGui.QPixmap("img/coke.jpg"))
        self.labelCoke2.setScaledContents(True)
        self.labelCoke2.setObjectName("labelCoke2")
        self.labelCoke2_status = QtWidgets.QLabel(self.groupBoxCoke2)
        self.labelCoke2_status.setGeometry(QtCore.QRect(20, 240, 20, 20))
        self.labelCoke2_status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelCoke2_status.setScaledContents(True)
        self.labelCoke2_status.setObjectName("labelCoke2_status")
        self.pushButtonCoke2Order = QtWidgets.QPushButton(self.groupBoxCoke2)
        self.pushButtonCoke2Order.setGeometry(QtCore.QRect(50, 240, 75, 23))
        self.pushButtonCoke2Order.setObjectName("pushButtonCoke2Order")
        self.horizontalLayout.addWidget(self.groupBoxCoke2)
        self.groupBoxSprite1 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBoxSprite1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxSprite1.setObjectName("groupBoxSprite1")
        self.labelSprite1 = QtWidgets.QLabel(self.groupBoxSprite1)
        self.labelSprite1.setGeometry(QtCore.QRect(20, 25, 120, 200))
        self.labelSprite1.setText("")
        self.labelSprite1.setPixmap(QtGui.QPixmap("img/sprite.jpg"))
        self.labelSprite1.setScaledContents(True)
        self.labelSprite1.setObjectName("labelSprite1")
        self.labelSprite1_status = QtWidgets.QLabel(self.groupBoxSprite1)
        self.labelSprite1_status.setGeometry(QtCore.QRect(20, 240, 20, 20))
        self.labelSprite1_status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelSprite1_status.setScaledContents(True)
        self.labelSprite1_status.setObjectName("labelSprite1_status")
        self.pushButtonSprite1Order = QtWidgets.QPushButton(self.groupBoxSprite1)
        self.pushButtonSprite1Order.setGeometry(QtCore.QRect(50, 240, 75, 23))
        self.pushButtonSprite1Order.setObjectName("pushButtonSprite1Order")
        self.horizontalLayout.addWidget(self.groupBoxSprite1)
        self.groupBoxSprite2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBoxSprite2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxSprite2.setObjectName("groupBoxSprite2")
        self.labelSprite2 = QtWidgets.QLabel(self.groupBoxSprite2)
        self.labelSprite2.setGeometry(QtCore.QRect(20, 25, 120, 200))
        self.labelSprite2.setText("")
        self.labelSprite2.setPixmap(QtGui.QPixmap("img/sprite.jpg"))
        self.labelSprite2.setScaledContents(True)
        self.labelSprite2.setObjectName("labelSprite2")
        self.labelSprite2_status = QtWidgets.QLabel(self.groupBoxSprite2)
        self.labelSprite2_status.setGeometry(QtCore.QRect(20, 240, 20, 20))
        self.labelSprite2_status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelSprite2_status.setScaledContents(True)
        self.labelSprite2_status.setObjectName("labelSprite2_status")
        self.pushButtonSprite2Order = QtWidgets.QPushButton(self.groupBoxSprite2)
        self.pushButtonSprite2Order.setGeometry(QtCore.QRect(50, 240, 75, 23))
        self.pushButtonSprite2Order.setObjectName("pushButtonSprite2Order")
        self.horizontalLayout.addWidget(self.groupBoxSprite2)
        self.groupBoxFanta1 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBoxFanta1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxFanta1.setObjectName("groupBoxFanta1")
        self.labelFanta1 = QtWidgets.QLabel(self.groupBoxFanta1)
        self.labelFanta1.setGeometry(QtCore.QRect(20, 25, 120, 200))
        self.labelFanta1.setText("")
        self.labelFanta1.setPixmap(QtGui.QPixmap("img/fanta.jpg"))
        self.labelFanta1.setScaledContents(True)
        self.labelFanta1.setObjectName("labelFanta1")
        self.labelFanta1_status = QtWidgets.QLabel(self.groupBoxFanta1)
        self.labelFanta1_status.setGeometry(QtCore.QRect(20, 240, 20, 20))
        self.labelFanta1_status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelFanta1_status.setScaledContents(True)
        self.labelFanta1_status.setObjectName("labelFanta1_status")
        self.pushButtonFanta1Order = QtWidgets.QPushButton(self.groupBoxFanta1)
        self.pushButtonFanta1Order.setGeometry(QtCore.QRect(50, 240, 75, 23))
        self.pushButtonFanta1Order.setObjectName("pushButtonFanta1Order")
        self.horizontalLayout.addWidget(self.groupBoxFanta1)
        self.groupBoxFanta2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBoxFanta2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxFanta2.setObjectName("groupBoxFanta2")
        self.labelFanta2 = QtWidgets.QLabel(self.groupBoxFanta2)
        self.labelFanta2.setGeometry(QtCore.QRect(20, 25, 120, 200))
        self.labelFanta2.setText("")
        self.labelFanta2.setPixmap(QtGui.QPixmap("img/fanta.jpg"))
        self.labelFanta2.setScaledContents(True)
        self.labelFanta2.setObjectName("labelFanta2")
        self.labelFanta2_status = QtWidgets.QLabel(self.groupBoxFanta2)
        self.labelFanta2_status.setGeometry(QtCore.QRect(20, 240, 20, 20))
        self.labelFanta2_status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelFanta2_status.setScaledContents(True)
        self.labelFanta2_status.setObjectName("labelFanta2_status")
        self.pushButtonFanta2Order = QtWidgets.QPushButton(self.groupBoxFanta2)
        self.pushButtonFanta2Order.setGeometry(QtCore.QRect(50, 240, 75, 23))
        self.pushButtonFanta2Order.setObjectName("pushButtonFanta2Order")
        self.horizontalLayout.addWidget(self.groupBoxFanta2)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBoxVending)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 20, 141, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lcdNumberTemp = QtWidgets.QLCDNumber(self.layoutWidget1)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lcdNumberTemp.setPalette(palette)
        self.lcdNumberTemp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lcdNumberTemp.setAutoFillBackground(False)
        self.lcdNumberTemp.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lcdNumberTemp.setSmallDecimalPoint(False)
        self.lcdNumberTemp.setDigitCount(6)
        self.lcdNumberTemp.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumberTemp.setObjectName("lcdNumberTemp")
        self.horizontalLayout_2.addWidget(self.lcdNumberTemp)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBoxIdentity.setTitle(_translate("Dialog", "Identity"))
        self.LabelVideo.setText(_translate("Dialog", "VideoLablel"))
        self.pushButtonRegister.setText(_translate("Dialog", "Register"))
        self.groupBoxVending.setTitle(_translate("Dialog", "Drinks"))
        self.pushButtonRefreshStatus.setText(_translate("Dialog", "Refresh"))
        self.groupBoxCoke1.setTitle(_translate("Dialog", "可口可乐"))
        self.labelCoke1_status.setText(_translate("Dialog", "TextLabel"))
        self.pushButtonCoke1Order.setText(_translate("Dialog", "Order"))
        self.groupBoxCoke2.setTitle(_translate("Dialog", "可口可乐"))
        self.labelCoke2_status.setText(_translate("Dialog", "TextLabel"))
        self.pushButtonCoke2Order.setText(_translate("Dialog", "Order"))
        self.groupBoxSprite1.setTitle(_translate("Dialog", "雪碧"))
        self.labelSprite1_status.setText(_translate("Dialog", "TextLabel"))
        self.pushButtonSprite1Order.setText(_translate("Dialog", "Order"))
        self.groupBoxSprite2.setTitle(_translate("Dialog", "雪碧"))
        self.labelSprite2_status.setText(_translate("Dialog", "TextLabel"))
        self.pushButtonSprite2Order.setText(_translate("Dialog", "Order"))
        self.groupBoxFanta1.setTitle(_translate("Dialog", "芬达"))
        self.labelFanta1_status.setText(_translate("Dialog", "TextLabel"))
        self.pushButtonFanta1Order.setText(_translate("Dialog", "Order"))
        self.groupBoxFanta2.setTitle(_translate("Dialog", "芬达"))
        self.labelFanta2_status.setText(_translate("Dialog", "TextLabel"))
        self.pushButtonFanta2Order.setText(_translate("Dialog", "Order"))
        self.label.setText(_translate("Dialog", "饮料温度"))
