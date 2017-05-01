from threading import Thread
from time import sleep

def a():
    while True:
        print('hi')
        sleep(1.0)

def b():
    while True:
        print(raw_input())

ta = Thread(target=a)
tb = Thread(target=b)

ta.start()
tb.start()

ta.join()
