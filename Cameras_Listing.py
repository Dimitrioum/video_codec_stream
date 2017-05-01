# -*- coding: utf-8 -*-
import cv2
import re
import subprocess
import os
import threading

i_o_c = [] #cameras' indexes
n_o_c = ['stationary'] #cameras' names

for i in range(3):
    cap = cv2.VideoCapture(i)
    while cap.isOpened():
        i_o_c.append(i+1)
        cap.release()
print i_o_c

caps = []
frames = []
videos = []

# for i in range(len(i_o_c)):
#     caps.append(cv2.VideoCapture(i))
#     frames.append(caps[i].read())
#
# while caps[1].isOpened:
#     frame = caps[1].read()
#     if frame[0] is True:
#         cv2.imshow('camera1', frame[1])
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break



def createCaptures(number, index):
    global caps, frames
    # event_for_wait.wait()
    # event_for_wait.clear()
    for i in range(number):
        caps.append(cv2.VideoCapture(i))
    while (c.isOpened for c in caps):
        frames.append(caps[index].read())
        # if (frames[j][0] for j in range(number) is True):
        cv2.imshow('Camera%d' % (index), frames[index][1])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break







# def createCaptures(number, index): #index = choose_cam - 1
#     global caps, frames, videos
#     for i in range(number):
#         caps.append(cv2.VideoCapture(i))
#         frames.append(caps[i].read())
#
#
#     while caps[index].isOpened():
#         if frames[index][0] is True:
#             return videos[index]
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
# def num_writer(event_for_wait, event_for_set):
#     global m
#     while m < 10:
#         event_for_wait.wait() # method blocks until the flag is true
#         event_for_wait.clear() # flag --> false
#         print m
#         m += 1
#         event_for_set.set() # flag --> true
#
# def _video_writer(frame):
#     return cv2.imshow('OpenCV_Training', frame)
#
# def _input():
#

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


createCaptures(len(i_o_c), 1)
# createCaptures(len(i_o_c), 1)
# cameras_left = i_o_c
# print caps, videos
# #
# event1 = threading.Event()
# event2 = threading.Event()
#
# thread1 = threading.Thread(target=FUNCTION, args=(e1, e2))
# thread2 = threading.Thread(target=FUNCTION, args=(e2, e1))
#
# thread1.start()
# thread2.start()
#
# event1.set()
#
# thread1.join()
# thread2.join()
# #
# captures = []
#
# # first stream
# if len(cameras_left) > 0:
#
#     while True:
#         choose_cam = int(raw_input('Вывести данные с видеокамеры под номером: '))
#         captures.append(createCapture(choose_cam))
#
# # second stream
# while len(captures) > 0:
#     for cap in captures:
#        ret, frame = cap.read()
#        if ret == True:
#            cv2.imshow('camera1', frame)
#
#

# if cameras_left > 0:
#     for i in range(len(cameras_left)):
#         choose_cam = int(raw_input('Вывести данные с видеокамеры под номером: '))
#
#         cap = [cap1, cap2, cap3]
#         frame = [frame1, frame2, frame3]
#         ret = [ret1, ret2, ret3]
#         cameras_left.remove(choose_cam)
#         while cap[choose_cam-1].isOpened():
#             ret[choose_cam - 1], frame[choose_cam - 1] = cap[choose_cam-1].read()
#             if ret[choose_cam - 1] is True:
#                 cv2.imshow('Camera%d' % (choose_cam), frame[choose_cam - 1])
#                 if cv2.waitKey(1) & 0xFF == ord('q'):
#                     break
#                 continue
#         continue
#
#
# else:
#     print 'Выведены данные со всех установленных камер'
#
# cap1.release()
# cap2.release()
# cap3.release()
# cv2.destroyAllWindows()




# device_index = None
# for file in os.listdir("/sys/class/video4linux"):
#     real_file = os.path.realpath("/sys/class/video4linux/" + file)
#     print real_file
#     print "/" + str(bus[-1]) + "-" + str(device[-1]) + "/"
#     if "/" + str(bus[-1]) + "-" + str(device[-1]) + "/" in real_file:
#         device_index = real_file[-1]
#         print "Hurray, device index is " + str(device_index)
