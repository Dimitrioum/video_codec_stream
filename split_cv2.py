# -*- coding: utf-8 -*-
import cv2

cap = cv2.VideoCapture(0)

_FRAME_WIDTH = 640
_FRAME_HEIGHT = 480
_FRAME_FPS = 30
out = cv2.VideoWriter('Video_Streaming_example.avi', cv2.VideoWriter_fourcc(*'X264'), _FRAME_FPS,
                      (_FRAME_WIDTH, _FRAME_HEIGHT))

# NAL юниты
sps = [0x00, 0x00, 0x00, 0x01, 0x67, 0x42, 0x00, 0x0a, 0xf8, 0x41,
       0xa2]  # sequence_parameter_set , 1 / stream - адресует последовательность кодированных кадров
pps = [0x00, 0x00, 0x00, 0x01, 0x68, 0xce, 0x38,
       0x80]  # picture_parameter_set , 1 / stream - адресует расшифровку одного или несколько кадров в полученной последовательности
slice_header = [0x00, 0x00, 0x00, 0x01, 0x05, 0x88, 0x84, 0x21, 0xa0]  # 1 / video frame
macroblock_header = [0x0d, 0x00]  # 1 / macroblock

f = open('encoded_video.264', 'w')

def _video_writer(frame):
    cv2.imshow('OpenCV_Training', frame)
    return out.write(frame)


def _macroblock(i, j):
    if not ((i == 0) & (j == 0)):
        f.write(str(macroblock_header))  # спецификация h.264 ЗАЧЕМ ??

    for x in range(i * 16, (i + 1) * 16):
        for y in range(j * 16, (j + 1) * 16):
            f.write(str(frame[x][y][0]))  # Y'

    for x in range(i * 8, (i + 1) * 8):
        for y in range(j * 8, (j + 1) * 8):
            f.write(str(frame[x][y][1]))  # U

    for x in range(i * 8, (i + 1) * 8):
        for y in range(j * 8, (j + 1) * 8):
            f.write(str(frame[x][y][2]))  # V


if __name__ == '__main__':
    while cap.isOpened():
        ret, frame = cap.read()

        if ret is True:
            _video_writer(frame)
            while not file.closed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
out.release()
cv2.destroyAllWindows()
