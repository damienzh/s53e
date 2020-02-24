#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

import face_recognition as fr
import cv2
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont


class RecogFace:
    def __init__(self):
        self.known_faces_names = []
        self.known_faces_encodings = []
        self.known_faces_path = os.path.abspath('./data/known_faces/')
        self.detection_model = 'hog'
        self.scale_ratio = 4
        self.recognition_thresh = 0.6

    def detection(self, frame):
        small_rgb = cv2.resize(frame, (0, 0), fx=1.0 / self.scale_ratio, fy=1.0 / self.scale_ratio)[:, :, ::-1]
        locations = fr.face_locations(small_rgb, model=self.detection_model)
        for (top, right, bottom, left) in locations:
            top *= self.scale_ratio
            right *= self.scale_ratio
            bottom *= self.scale_ratio
            left *= self.scale_ratio
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        return frame

    # 生成已知脸部数据
    def load_known_faces(self):
        # 读取所有个人数据文件夹
        names = os.listdir(self.known_faces_path)
        # 读取个人文件夹
        for n in names:
            if os.path.isdir(n):
                # 生成个人照片文件夹路径
                face_path = os.path.join(self.known_faces_path, n)
                # 读取个人文件夹内所有照片
                face_imgs = os.listdir(face_path)
                # 根据个人照片生成脸部数据编码
                for image in face_imgs:
                    image_path = os.path.join(face_path, image)
                    if os.path.isfile(image_path):
                        image_ = fr.load_image_file(image_path)
                        encodings = fr.face_encodings(image_,)[0]

            # 将生成数据存入内存
            self.known_faces_names.append(n)
            self.known_faces_encodings.append(encodings[0])

    def reload_known_faces(self):
        self.known_faces_names = []
        self.known_faces_encodings = []
        self.load_known_faces()

    def recognition(self, face):
        known = 'unknown'
        if not len(self.known_faces_names):
            results = fr.compare_faces(self.known_faces_encodings, face, tolerance=self.recognition_thresh)
            if True in ret:
                known = self.known_faces_names[results.index(True)]
        else:
            return known

    # 添加用户照片到已知数据文件夹
    def add_face(self, frame, name):
        # 如果为新用户则创建文件夹
        if not name in self.known_faces_names:
            os.mkdir(os.path.join(self.known_faces_path, name))

        num = len(os.listdir(os.path.join(self.known_faces_path, name)))
        image_name = os.path.join(self.known_faces_path,
                                  name,
                                  '{:4}.png'.format(num).replace(' ', '0'))
        cv2.imwrite(image_name, frame)

    def draw_text_cn(self, frame, pos, name):
        """
        put text on cv image with support of Chinese character
        :param frame: cv image
        :param pos: text coordinates top left
        :param name: string to put on image
        :return: cv image with text
        """
        font_size = 40
        # 字体颜色 RGB
        font_color = (255, 0, 0)
        # 转换cv图片到PIL图片
        pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        # 定义画笔
        draw = ImageDraw.Draw(pil_img)
        # 设定字体
        font = ImageFont.truetype('uming.ttc', font_size, encoding='utf-8')
        # 转换中文字符串编码成unicode
        name = unicode(name, encoding='utf-8')
        # 将中文文字画至图片上
        draw.text(pos, name, font_color, font=font)

        # 返回cv图片
        return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    f = RecogFace()
    while True:
        ret, frame = cap.read()
        if ret:
            frame = f.detection(frame)

        name = 'unknown'
        # names = os.listdir('.')
        # for n in names:
        #     if 'txt' in n:
        #         name = n.split('.')[0]
        frame = f.draw_text_cn(frame, (50, 100), name)
        cv2.imshow('live', frame)

        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    cv2.destroyAllWindows()
    cap.release()
