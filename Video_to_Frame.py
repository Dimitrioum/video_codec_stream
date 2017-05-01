import cv2
_FRAME_WIDTH = 640
_FRAME_HEIGHT = 480
cap = cv2.VideoCapture(0)

ret, frame = cap.read()

B = [[frame[i][j][0] for i in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]
G = [[frame[i][j][1] for i in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]
R = [[frame[i][j][2] for i in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]

print(B[0][0])
print(G[143][123])
print(R[12][0])

