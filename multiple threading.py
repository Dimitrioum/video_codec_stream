import threading

def num_writer(event_for_wait, event_for_set):
    global m

    while m < 10:
        event_for_wait.wait() # method blocks until the flag is true
        event_for_wait.clear() # flag --> false
        print m
        m += 1
        event_for_set.set() # flag --> true

e1 = threading.Event()
e2 = threading.Event()

m = 0

t1 = threading.Thread(target=num_writer, args=(e1, e2))
t2 = threading.Thread(target=num_writer, args=(e2, e1))

t1.start()
t2.start()

e1.set()

t1.join()
t2.join()

print m














# import threading
#
# def writer(x, event_for_wait, event_for_set):
#     for i in xrange(10):
#         event_for_wait.wait() # wait for event
#         event_for_wait.clear() # clean event for future
#         print x
#         event_for_set.set() # set event for neighbor thread
#
# # init events
# e1 = threading.Event()
# e2 = threading.Event()
#
# # init threads
# t1 = threading.Thread(target=writer, args=(0, e1, e2))
# t2 = threading.Thread(target=writer, args=(1, e2, e1))
#
# # start threads
# t1.start()
# t2.start()
#
# e1.set() # initiate the first event
#
# # join threads to the main thread
# t1.join()
# t2.join()
