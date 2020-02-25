#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage
import cv2
from cvqt_helper import cv_to_qimg


class LiveCamera(QThread):
    img_signal = pyqtSignal(QImage)

    def run(self):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        while True:
            ret, frame = cap.read()
            if ret:
                img = cv_to_qimg(frame)
                self.img_signal.emit(img)
