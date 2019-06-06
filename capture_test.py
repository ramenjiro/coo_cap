# -*- coding:utf-8 -*-

import cv2
import os
import tkinter as tk
import sys

# 座標を入力するためのウィンドウを表示する関数
def input_form():

    # 確定ボタンが押された時のコールバック関数
    def coord_get():

        # Entryウィジェットのテキストを読み取るgetメソッド
        global coord
        coord = txt.get()

        if not coord:
            # 空欄だったら処理しない
            pass

        root.destroy()

    # ウィンドウの定義
    root = tk.Tk()
    root.title(u"Coordinate input")
    root.geometry("300x300")

    # フレームの定義
    frame =tk.Frame(root, pady=10)
    frame.pack()

    # ラベル
    label = tk.Label(frame, font=("",14), text="座標->")
    label.pack(side="left")

    # テキストボックス
    txt = tk.Entry(frame, font=("",14), justify="center", width=10)
    txt.focus()
    txt.pack(side="left")

    # エンターキーで入力
    root.bind("<Return>", coord_get)

    # ボタンでも入力できるように
    button = tk.Button(root, text="確定", font=("",15), width=10, bg="gray", command=coord_get)
    button.pack()

    # メインループ
    root.mainloop()

def save_frame_camera_key(device_num, dir_path, basename,cycle, ext='jpg', delay=1, window_name='frame'):

    cap = cv2.VideoCapture(device_num)
    base_path="/home/user/Documents/data/"
    id = 35
    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay)
        if key == ord('q'):
            break
        elif key == ord('c'):
            strngr = "CYM"
            input_form()
            print("画像を保存します。ファイル名" + base_path + strngr + "_" + coord + "_"+str(id)+"." + ext)
            cv2.imwrite('{}{}_{}_{}.{}'.format(base_path,strngr, coord, id, ext), frame)
            id += 1
    cv2.destroyWindow(window_name)

#データの保存場所
#3つ目の項目が撮影間隔（cycle）fps30で撮影しているため、cycle/30=撮影間隔（秒）となる　例cycle=60 60/30= 2 (秒間隔)
save_frame_camera_key(0, 'data', 'xK_',60)
