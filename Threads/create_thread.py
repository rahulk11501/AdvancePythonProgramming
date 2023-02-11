# Create thread from function
import threading
import time
from threading import Thread


def primeNumber():
    for x in range(20):
        if x % 3 == 0:
            print("PrimeNum", x)


t_ = Thread(target=primeNumber)
t_.start()


def evenNumber():
    for x in range(20):
        if x % 2 == 0:
            print(x)
    thread1 = threading.current_thread().getName()
    print(thread1)
    threading.current_thread().name = "evenOdd Thread"
    print(threading.current_thread().getName())


a = threading.current_thread().getName()
print(a)


def oddNumber():
    for x in range(20):
        if x % 2 != 0:
            print(x)
    print(threading.current_thread().getName())


def evenOdd():
    time.sleep(0.5)
    evenNumber()
    oddNumber()


# evenOdd()
t_2 = Thread(target=evenOdd())
t_2.start()


class myThread(Thread):
    def run(self):
        time.sleep(0.5)
        print("Egyptian Pyramid")
        print(threading.current_thread().getName())
        for x in range(0, 5):
            for j in range(0, x + 1):
                print("*", end=" ")
            print("\r")


obj = myThread()
obj.start()
