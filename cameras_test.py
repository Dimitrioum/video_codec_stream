# -*- coding: utf-8 -*-
import threading
import time
import sys
import cv2
import re
import subprocess
import os
import warnings


def _get_cameras(numbers, devices):
    global cameras_names, dict_of_cameras, dict_of_active_cams
    cameras_names = []
    dict_of_active_cams = {}
    for i in devices.split('\n'):
        if i:
            cameras_names.append()

    dict_of_cameras = dict(zip([(i+1) for i in range(len(numbers))], cameras_names))
    return dict_of_cameras

def _get_all_devices(check_stat):
    df = subprocess.check_output("ls -ltrh /dev/video*", shell=True)
    return df


def _video_stream():
    global cameras, videoLock, inputLock, dict_of_active_cams, choose_cam

    def _is_opened(video_obj):
        return video_obj.isOpened()

    while True:
        if len(dict_of_active_cams.values()) > 0:
            videoLock.wait()
            inputLock.clear()
            for num in range(len(dict_of_active_cams.values())):
                if map(_is_opened, dict_of_active_cams.values()):
                    rets, frames = dict_of_active_cams.values()[num].read()
                    if(rets):
                        cv2.imshow('camera%d' % (num + 1), frames)
                        cv2.waitKey(1)
            inputLock.set()
        else:
            pass



def _stream_initialization(list_of_cameras):
    global choose_cam, caps, cameras
    caps = [] # all devices available
    cameras = [] # displayed devices
    for item in range(len(list_of_cameras)):
        caps.append(cv2.VideoCapture(item))

def _user_input():
    global choose_cam, cameras, caps, videoLock, inputLock, dict_of_active_cams
    while True:
        input = raw_input('Введите add для добавления камеры, del - для удаления камеры с дисплея: ')
        if input == 'add':
            if len(cameras) == len(caps):
                print('Выведены все камеры')

            else:
                inputLock.wait()
                videoLock.clear()
                print('Список доступных камер: ', dict_of_cameras)
                choose_cam = int(raw_input('Введите номер камеры: '))

                if caps[choose_cam - 1] in cameras:
                    print('Камера уже выведена на дисплей!')
                    videoLock.set()
                else:
                    cameras.append(caps[choose_cam - 1])
                    dict_of_cameras.__delitem__(choose_cam)
                    dict_of_active_cams = dict(zip([(i+1) for i in range(len(cameras))], cameras))
                    cv2.destroyAllWindows()
                    videoLock.set()

        elif input == 'del':
            inputLock.wait()
            videoLock.clear()
            print('Список активных камер: ', dict_of_active_cams)
            choose_del = int(raw_input('Введите номер камеры, чтобы удалить её с дисплея: '))
            cameras.remove(cameras[choose_del - 1])
            caps[choose_del - 1].release()
            dict_of_active_cams.__delitem__(choose_del)
            dict_of_cameras[choose_del] = cameras_names[choose_del - 1]
            cv2.destroyAllWindows()
            videoLock.set()
        elif not ((input == 'add') and (input == 'del')):
            inputLock.wait()
            videoLock.clear()
            print('Некоректный ввод')
            videoLock.set()


def _threading_initialization():

    thread1 = threading.Thread(target=_video_stream)
    thread2 = threading.Thread(target=_user_input)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    return thread1, thread2


if __name__ == '__main__':
    videoLock = threading.Event()
    inputLock = threading.Event()
    videoLock.set()
    inputLock.set()


    devices = _get_all_devices()
    print(devices)

    numbers = raw_input('Введите номера USB-портов видеокамер через запятую для дальнейшей работы: ').split(',')
    numbers = [int(i) for i in numbers]

    print(_get_cameras(numbers, devices, check_stat))

    _stream_initialization(cameras_names)
    #check if there is a stationary camera

    _threading_initialization()
