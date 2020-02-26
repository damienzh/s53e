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
        self.face_detected = False
        self.detected_name = ''
        self.detection_model = 'hog'
        self.scale_ratio = 2
        self.recognition_thresh = 0.6

    def detection(self, frame):
        """
        detect faces in given cv frame
        :param frame: cv frame to be detected
        :return: cv frame marked faces with rectangle
        """
        # 为了提高速度人脸识别全部在小尺寸图像上进行
        small_rgb = cv2.resize(frame, (0, 0), fx=1.0 / self.scale_ratio, fy=1.0 / self.scale_ratio)[:, :, ::-1]

        locations = fr.face_locations(small_rgb, model=self.detection_model)
        if len(locations) == 0:
            self.face_detected = False
        else:
            self.face_detected = True
            for (top, right, bottom, left) in locations:
                face_crop = small_rgb[top:bottom, left:right]
                face_name = self.recognition(face_crop)
                top *= self.scale_ratio
                right *= self.scale_ratio
                bottom *= self.scale_ratio
                left *= self.scale_ratio
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                frame = self.draw_text_cn(frame, (left, top-20), face_name)
                if face_name in self.known_faces_names:
                    self.detected_name = face_name
        return frame

    # 生成已知脸部数据
    def load_known_faces(self):
        """
        create known face encodings from all images stored in known_faces folder
        """
        # 读取所有个人数据文件夹
        names = os.listdir(self.known_faces_path)
        # 读取个人文件夹
        for n in names:
            # 生成个人照片文件夹路径
            face_path = os.path.join(self.known_faces_path, n)
            if os.path.isdir(face_path):
                # 读取个人文件夹内所有照片
                face_imgs = os.listdir(face_path)
                # 根据个人照片生成脸部数据编码
                for image in face_imgs:
                    image_path = os.path.join(face_path, image)
                    if os.path.isfile(image_path):
                        image_ = fr.load_image_file(image_path)
                        encoding = fr.face_encodings(image_)[0]

                        # 将生成数据存入内存
                        self.known_faces_names.append(n)
                        self.known_faces_encodings.append(encoding)
        # print self.known_faces_names
        # print self.known_faces_encodings

    def reload_known_faces(self):
        """
        reload known face encodings
        :return:
        """
        self.known_faces_names = []
        self.known_faces_encodings = []
        self.load_known_faces()

    def recognition(self, face_frame):
        """
        compare face encoding with known faces
        :param face_frame: frame contained one face
        :return: matched name or unknown
        """
        known = 'unknown'
        face = fr.face_encodings(face_frame)
        # 如有已知用户且有人脸特征值则对比侦测特征值与已知用户
        if len(self.known_faces_names) > 0 and len(face) > 0:
            results = fr.compare_faces(self.known_faces_encodings, face[0], tolerance=self.recognition_thresh)
            if True in results:
                known = self.known_faces_names[results.index(True)]
        # 如无特征值
        elif len(face) == 0:
            known = 'noEncoding'
        return known

    # 添加用户照片到已知数据文件夹
    def add_face(self, frame, name):
        """
        save user image under given named folder
        :param frame: cv frame to be saved
        :param name: user name
        """
        # 如果为新用户则创建文件夹
        if not name in self.known_faces_names:
            os.mkdir(os.path.join(self.known_faces_path, name))

        num = len(os.listdir(os.path.join(self.known_faces_path, name)))
        image_path = os.path.join(self.known_faces_path, name)
        image_name = '{:4}.png'.format(num).replace(' ', '0')
        os.chdir(image_path)
        cv2.imwrite(image_name, frame)
        self.reload_known_faces()

    def draw_text_cn(self, frame, pos, name):
        """
        put text on cv image with support of Chinese character
        :param frame: cv image
        :param pos: text coordinates top left
        :param name: string to put on image
        :return: cv image with text
        """
        # 字体大小
        font_size = 20
        # 字体颜色 RGB
        font_color = (0, 255, 0)
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
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    f = RecogFace()
    # f.load_known_faces()
    while True:
        ret, frame = cap.read()
        if ret:
            frame = f.detection(frame)

        # name = 'unknown'
        # # names = os.listdir('.')
        # # for n in names:
        # #     if 'txt' in n:
        # #         name = n.split('.')[0]
        # frame = f.draw_text_cn(frame, (50, 100), name)
        # frame = cv2.resize(frame, (480, 360))
        cv2.imshow('live', frame)

        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    cv2.destroyAllWindows()
    cap.release()
