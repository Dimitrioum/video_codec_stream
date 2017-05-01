# -*- coding: utf-8 -*-
import cv2
import re
import subprocess
import os
import threading

i_o_c = [] #cameras' indexes
n_o_c = ['stationary'] #cameras' names

def _video_stream(number, index):
    global caps, rets, frames, cameras
    while (c.isOpened() for c in caps):
        for j in range(number):
            rets[j], frames[j] = caps[j].read()
        if (rets[p] for p in range(number)) is True:
            cv2.imshow('camera%d' % (index), frames[index - 1])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    for i in range(number):
        caps[i].release()

    cv2.destroyAllWindows()


def _input():
    global choose_cam, caps, cameras
    choose_cam = int(raw_input('Вывести данные с видеокамеры под номером: '))


for i in range(3):
    cap = cv2.VideoCapture(i)
    while cap.isOpened():
        i_o_c.append(i+1)
        cap.release()
print i_o_c

caps = []
frames = [i for i in range(len(i_o_c))]
rets = [i for i in range(len(i_o_c))]
cameras = []

for i in range(len(i_o_c)):
    caps.append(cv2.VideoCapture(i))

device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
df = subprocess.check_output("lsusb", shell=True)
for i in df.split('\n'):
    if i:
        info = device_re.match(i)
        if info:
            dinfo = info.groupdict()
            if int(dinfo['bus']) in [001, 003] and 'root' not in dinfo['tag'].split(' '):
                n_o_c.append(dinfo['tag'])
print n_o_c
print dict(zip(i_o_c, n_o_c))


choose_cam = int(raw_input('Вывести данные с видеокамеры под номером: '))

thread1 = threading.Thread(target=_video_stream, args=(len(i_o_c), choose_cam,))
thread2 = threading.Thread(target=_input, args=())

thread1.start()
thread2.start()

thread1.join()
thread2.join()

