# -*- coding: utf-8 -*-
import cv2
import re
import subprocess
import os
import threading

i_o_c = [] #cameras' indexes
n_o_c = ['stationary'] #cameras' names


def _video_stream(number):
    global caps, cameras, stop
    while (c.isOpened() for c in cameras):
        for j in range(number):
            rets, frames = cameras[j].read()
            if(rets):
                event_for_wait.wait()
                event_for_wait.clear()
                cv2.imshow('camera%d' % (j), frames)
                event_for_set.set()

        # if stop:
        #                         #cv2.waitKey(1) & 0xFF == ord('q'):
        #     for i in range(number):
        #         caps[i].release()
        #     cv2.destroyAllWindows()
        #     break

def _input():
    global choose_cam, caps, cameras
    event_for_wait.wait()
    event_for_wait.clear()
    choose_cam = int(raw_input('Укажите номер камеры: '))
    event_for_set.set()
    cameras.append(caps[choose_cam - 1])



for i in range(3):
    cap = cv2.VideoCapture(i)
    while cap.isOpened():
        i_o_c.append(i+1)
        cap.release()
print i_o_c

caps = [] # all devices available
# frames = [i for i in range(len(i_o_c))]
# rets = [i for i in range(len(i_o_c))]
cameras = [] # displayed devices

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
print caps

choose_cam = 0
cameras.append(caps[0])
#
# event1 = threading.Event()
# event2 = threading.Event()

thread1 = threading.Thread(target=_video_stream, args=(len(cameras), ))
thread2 = threading.Thread(target=_input)

thread1.start()
thread2.start()

# event1.set()

thread1.join()
thread2.join()
