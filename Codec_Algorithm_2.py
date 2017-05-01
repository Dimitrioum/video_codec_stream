import cv2

cap = cv2.VideoCapture(0)

_FRAME_WIDTH = 640
_FRAME_HEIGHT = 480
_FRAME_FPS = 60

out = cv2.VideoWriter('2.avi', cv2.VideoWriter_fourcc(*'X264'), _FRAME_FPS, (_FRAME_WIDTH,_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('OpenCV_Training', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
print type(frame)
cap.release()
out.release()
cv2.destroyAllWindows()



