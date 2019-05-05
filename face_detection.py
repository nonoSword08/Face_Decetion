#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cv2
import face_recognition as fr
import os


def face_detection():
    # 将图片库的文件的列表拿出来
    pic_list = os.listdir('./pic_lib')

    # 首先将图片库中所有脸进行编码
    face_lib_coding = []
    for i in pic_list:
        img = fr.load_image_file("pic_lib/" + i)
        face_location = fr.face_locations(img)
        face_lib_coding.append(fr.face_encodings(img, face_location)[0])

    # new摄像机对象
    cap = cv2.VideoCapture(0)

    # 搞个值来控制读摄像头次数防止死机
    process_this_frame = True

    while True:

        # 退出模块
        key_in = cv2.waitKey(1) & 0xFF
        if key_in == ord('q'):
            break

        # 获取这一帧并处理
        ret, frame = cap.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        cv2.imshow("LOOK ME!!", frame)

        if process_this_frame:
            # 获取这一帧未知脸的位置
            face_locations = fr.face_locations(small_frame)
            # 将未知脸位置进行编码
            unknown_face = fr.face_encodings(small_frame, face_locations)
            if len(unknown_face) == 0:
                continue
            # 将未知脸放入已知脸图片库中进行比较得到结果数组
            result = fr.compare_faces(face_lib_coding, unknown_face[0], tolerance=0.5)

            # 遍历结果数组如果里面有True则break
            for i in range(len(result)):
                if result[i]:
                    username = pic_list[i].split('.')[0]
                    print('{}同学打卡成功'.format(username).center(80, '~'))
                    cap.release()
                    cv2.destroyAllWindows()
                    return username
        process_this_frame = not process_this_frame
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    face_detection()
