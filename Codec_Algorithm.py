# -*- coding: utf-8 -*-
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
_FRAME_WIDTH = 640
_FRAME_HEIGHT = 480
_FRAME_FPS = 30
out = cv2.VideoWriter('Video_from_Camera.avi', cv2.VideoWriter_fourcc(*'X264'), _FRAME_FPS, (_FRAME_WIDTH,_FRAME_HEIGHT))

ret, frame = cap.read()

B = [[frame[i][j][0] for i in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]
G = [[frame[i][j][1] for i in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]
R = [[frame[i][j][2] for i in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]

#RGB to YUV
Y = [[int(frame[i][j][2]*0.299 + frame[i][j][1]*0.587 + frame[i][j][0]*0.114) for i in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]
U = [[int(-frame[i][j][2]*0.14713 - frame[i][j][1]*0.28886 + frame[i][j][0]*0.436 + 128) for j in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]
V = [[int(frame[i][j][2]*0.615 - frame[i][j][1]*0.51499 - frame[i][j][0]*0.10001 + 128) for j in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]

f = open('raw_data.txt','w')


f.write(str(Y[0][0]))

# for i in range(_FRAME_WIDTH/10):
#     for j in range(_FRAME_HEIGHT/10):
#         f.write(str(Y[i][j]))

