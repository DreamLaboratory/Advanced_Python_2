"""
Python GIL is a mutex that allows only one thread to hold the control of the Python interpreter.
This means that only one thread can be in a state of execution at any point in time.
This simplifies the CPython implementation by making the object model inherently thread-safe.
However, the GIL makes multi-threaded programming more difficult in Python because the majority of the threads cannot run in parallel.
This is because they are blocked by the GIL.
The GIL is necessary mainly because CPython’s memory management is not thread-safe.
The GIL exists even though most modern processors have multiple cores.

"""

import threading
import time

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n*n*n)

arr = [2,3,8,9]

t = time.time()
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
print("done in : ", time.time()-t)
print("Hah... I am done with all my work now!")


# Example 2 Increasing variable value using threads and GIL in Python

INCREMENT_NUMBER = 1000000

def increment_with_gil():
    x = 0
    for i in range(INCREMENT_NUMBER):
        x += 1

def increment_without_gil():
    x = 0
    for i in range(INCREMENT_NUMBER):
        x += 1

def main():
    t1 = threading.Thread(target=increment_with_gil)
    t2 = threading.Thread(target=increment_without_gil)

    # starting threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
