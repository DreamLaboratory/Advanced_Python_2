# multi_threaded.py
import time
from threading import Thread

COUNT = 50_000_000

# GIL 

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()

t1.start()
t2.start()
t1.join()
t2.join()

# countdown(COUNT//2)

end = time.time()

print('Time taken in seconds -', end - start)
