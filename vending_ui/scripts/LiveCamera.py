# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
import cv2


class LiveCamera(QThread):
    img_signal = pyqtSignal(QImage)

    def run(self):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
        while True:
            ret, frame = cap.read()
            if ret:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame_rgb.shape
                bytesPerLine = w * ch
                img = QImage(frame_rgb.data, w, h, bytesPerLine, QImage.Format_RGB888)
                self.img_signal.emit(img)
