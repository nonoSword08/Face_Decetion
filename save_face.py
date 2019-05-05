#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 9:10
# @Author  : Chensijie
# @Site    : 
# @File    : save_face.py
# @Software: PyCharm


import numpy
import tkinter as tk
import cv2
import os
import face_recognition as fr

username = None
save_path = 'pic_lib_txt'
label2 = None
username_val = None
second = None


def save_face():
    global save_path
    global label2
    global username_val
    global second
    if save_path not in os.listdir('.'):
        os.mkdir(save_path)

    second = tk.Toplevel()
    second.title('请输入用户名')

    username_val = tk.Variable()
    username_input = tk.Entry(second, textvariable=username_val)
    label1 = tk.Label(second, text='请输入用户名')
    label2 = tk.Label(second, text='名字已经存在，请重试')
    username_button = tk.Button(second, text='确定', command=get_username)

    label1.grid(row=0, column=0)
    username_input.grid(row=0, column=1)
    username_button.grid(row=0, column=2)

    second.mainloop()


def get_username():
    global username
    global save_path
    global label2
    global username_val
    global second
    if (username_val.get() + '.txt') in os.listdir('./' + save_path):
        label2.grid(row=1)
    else:
        second.destroy()
        username = username_val.get()

        # new摄像机对象
        cap = cv2.VideoCapture(0)

        while True:
            # 获取一帧
            ret, frame = cap.read()

            # 显示这一帧
            cv2.imshow("LOOK ME!!", frame)

            # 获取键盘输入，执行操作
            key_in = cv2.waitKey(1) & 0xFF
            if key_in == ord('s'):
                if len(fr.face_encodings(frame)) == 0:
                    print('没有脸，请重拍')
                    continue
                    # 将未知脸位置进行编码
                face_locations = fr.face_locations(frame)
                unknown_face = fr.face_encodings(frame, face_locations)
                numpy.savetxt(save_path + '/' + username + '.txt', unknown_face[0], fmt='%.6f')
                # cv2.imencode('.jpg', frame)[1].tofile(save_path + '/' + username + '.jpg')
                # cv2.imwrite(username + '.jpg', frame)
                break
            if key_in == ord('q'):
                break
        # 关闭资源
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    save_face()
