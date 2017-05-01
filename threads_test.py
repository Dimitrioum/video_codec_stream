import threading
import cv2
threadLock=threading.Lock()
class myThread (threading.Thread):
    maxRetries=20
    def __init__(self, threadID, name,video_url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.video_url=video_url

    def attemptRead(self,cvVideo):
        threadLock.acquire()
        (isRead,cvImage)=cvVideo.read()
        threadLock.release()
        if isRead==False:
            count=1
            while isRead==False and count<myThread.maxRetries:
                threadLock.acquire()
                (isRead,cvImage)=cvVideo.read()
                threadLock.release()
                print self.name+' try no: ',count
                count+=1
        return (isRead,cvImage)

    def run(self):
        print "Starting " + self.name
        windowName = self.name
        cv2.namedWindow(windowName)
        cvVideo = cv2.VideoCapture(self.video_url)


        while True:
            (isRead,cvImage)=self.attemptRead(cvVideo)
            if isRead==False:
                break
            cv2.imshow(windowName,cvImage)
            key=cv2.waitKey(50)
            if key==27:
                break

        cv2.destroyWindow(windowName)
        print self.name + "Exiting"

def main():
    thread1 = myThread(1, "Thread1", '/home/malovdmitrij/test1.avi')
    thread2 = myThread(2, "Thread2", '/home/malovdmitrij/test2.avi')

    thread1.start()
    thread2.start()

print "Exiting Main Thread"

if __name__ == '__main__':
    main()
