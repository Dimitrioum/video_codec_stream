import threading
import time

def race(name, event_for_wait, event_for_set):
    global winners
    for i in range(10):
        event_for_wait.wait() # method blocks until the flag is true
        event_for_wait.clear()
        print name, i
        event_for_set.set()
    winners.append(name)



winners = []

e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()

t1 = threading.Thread(target = race, args=('thread1', e1, e2,))
t2 = threading.Thread(target = race, args=('thread2', e2, e3,))
t3 = threading.Thread(target = race, args=('thread3', e3, e1,))

t1.start()
t2.start()
t3.start()

e1.set()

t1.join()
t2.join()
t3.join()

print 'The first thread that finished is ' + winners[0] + ', the second is ' + winners[1] + ' and the 3rd is ' + winners[2]
