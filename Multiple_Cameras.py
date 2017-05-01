import cv2

cap1 = cv2.VideoCapture(0)

cap2 = cv2.VideoCapture(1)

cap3 = cv2.VideoCapture(2)

caps = [cap1, cap2, cap3]


while cap1.isOpened():
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()

    if ret1 is True and ret2 is True and ret3 is True:
        cv2.imshow('camera1', frame1)
        cv2.imshow('camera2', frame2)
        cv2.imshow('camera3', frame3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()



