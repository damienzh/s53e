# -*- coding: utf-8 -*-

import cv2
import numpy as np
from PyQt5.QtGui import QImage


def qimage_to_cv(qimage):
    b = qimage.bits()
    b.setsize(qimage.byteCount())
    height = qimage.height()
    width = qimage.width()
    img_arr = np.array(b).reshape(height, width, 3)
    return cv2.cvtColor(img_arr, cv2.COLOR_RGB2BGR)


def cv_to_qimg(cvimg):
    frame_rgb = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
    h, w, ch = frame_rgb.shape
    bytesPerLine = w * ch
    return QImage(frame_rgb.data, w, h, bytesPerLine, QImage.Format_RGB888)
