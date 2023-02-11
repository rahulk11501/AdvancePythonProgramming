from threading import Thread
import threading
from time import sleep

def naturalNum():
    print(threading.current_thread().getName(), "Started")
    sleep(2)
    for x in range(10):
        print(x)
    print(threading.current_thread().getName(), "Ended")


thread_ = Thread(target=naturalNum())
thread_2 = Thread(target=naturalNum())

thread_.start()
thread_2.start()