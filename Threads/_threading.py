import threading

t = threading.current_thread().getName()
if threading.current_thread() == threading.main_thread():
    for x in range(10):
        if x % 2.5 == 0:
            print(x)

print(t)
print(threading.main_thread())

threading.current_thread().name = "Rahul Kumar"
print(threading.current_thread().name)
