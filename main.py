#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 9:07
# @Author  : Chensijie
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import tkinter as tk
from save_face import save_face
from face_detection2 import face_detection2

username_list = []


def face_det():
    username = face_detection2()
    if username in username_list:
        print('请不要重复打卡'.center(40, '*'))
        return None
    username_list.append(username)


def show_stu():
    if len(username_list) == 0:
        print('还没有学生刷脸')
    else:
        print(username_list, end='已经刷脸\n')


if __name__ == '__main__':
    top = tk.Tk()
    top.title('人脸识别')
    top.geometry('300x300')

    save_face_button = tk.Button(top, text='录入人脸信息', command=save_face)
    face_detection2_button = tk.Button(top, text='人脸打卡', command=face_det)
    show_stu_button = tk.Button(top, text='点名', command=show_stu)

    # 布局
    save_face_button.grid(row=1, column=5, pady=10, ipadx=100, ipady=10, sticky=tk.E)
    face_detection2_button.grid(row=2, column=5, pady=10, ipadx=100, ipady=10)
    show_stu_button.grid(row=3, column=5, pady=10, ipadx=100, ipady=10)

    # 运行
    top.mainloop()
