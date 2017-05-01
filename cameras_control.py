# -*- coding: utf-8 -*-
from __future__ import print_function
import threading
import time
import sys
import cv2
import re
import subprocess
import os
import warnings

dict_of_cap_cameras = {}
array_active_cameras = []

VIDEO_CONST = '/dev/video'


def _check_cam(index):
    return cv2.VideoCapture(index) if cv2.VideoCapture(index).read()[0] else None

def _get_video_devices():
    names = subprocess.check_output("ls -ltrh /dev/video*", shell=True)
    if names:
        devices = {}

        def add_in_device(line):
            start_index = line.find(VIDEO_CONST)
            devices[line[start_index+len(VIDEO_CONST)]] = line[start_index:]
        map(lambda line: add_in_device(line), list(filter(None, names.split('\n'))))

    return devices if devices else None

def _cameras_initialization(list_of_cameras):
    return {key: cv2.VideoCapture(int(key)) for (key, value) in list_of_cameras.items()}

def add_camera(number):
    array_active_cameras.append(number)

def _video_stream(inputLock, videoLock):
    while True:
        videoLock.wait()
        inputLock.clear()

        for camera_number in array_active_cameras:
            cap = dict_of_cap_cameras[camera_number]
            if cap.isOpened():
                rets, frames = cap.read()
                if rets:
                    cv2.imshow('camera%s' % (camera_number), frames)
                    cv2.waitKey(1)
        inputLock.set()



def _user_input(inputLock, videoLock):
   while True:

        input = raw_input('Введите add для добавления камеры, del - для удаления камеры с дисплея: ')
        if input.isalpha() and input == 'add':

            if len(array_active_cameras) == len(dict_of_cap_cameras):
                print('Введены все камеры')
            else:
                inputLock.wait()
                videoLock.clear()

                keys_avalible_cameras = list(set(dict_of_cap_cameras.keys()) - set(array_active_cameras))
                keys_avalible_cameras.sort()
                print('Список доступных камер: ')
                for key in keys_avalible_cameras: print('%s - %s' % (key, VIDEO_CONST + key))

                camera_number = raw_input('Введите номер камеры: ')
                if camera_number.isdigit() and bool(keys_avalible_cameras) and (camera_number in dict_of_cap_cameras.keys()):
                    if camera_number in array_active_cameras:
                        print('Камера уже выведена на дисплей!')
                    else:
                        add_camera(camera_number)
                        print(len(array_active_cameras))
                        cv2.destroyAllWindows()
                videoLock.set()

        elif input.isalpha() and input == 'del':
            inputLock.wait()
            videoLock.clear()
            if bool(array_active_cameras):
                print('Список активных камер: ')
                array_active_cameras.sort()
                for key in array_active_cameras: print('%s - %s' % (key, VIDEO_CONST + key))
                camera_number = raw_input('Введите номер камеры, чтобы удалить её с дисплея: ')
                if camera_number.isdigit() and (camera_number in array_active_cameras):
                    array_active_cameras.remove(camera_number)
                    cv2.destroyAllWindows()
            else:
                print('Нет активных камер!')

            videoLock.set()
        else:
            print('Некоректный ввод')


if __name__ == '__main__':

    videoLock = threading.Event()
    inputLock = threading.Event()
    videoLock.set()
    inputLock.set()

    dict_of_cap_cameras = _cameras_initialization(_get_video_devices())

    cameras_output = threading.Thread(target=_video_stream, args=(inputLock, videoLock))
    user_input = threading.Thread(target=_user_input, args=(inputLock, videoLock))

    cameras_output.start()
    user_input.start()

    cameras_output.join()
    user_input.join()
