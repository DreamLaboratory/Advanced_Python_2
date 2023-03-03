# ####################### Thread in Python ############################

# # Quetions:

# # 1. What is Thread?
# # 2. How to create a Thread?
# # 3. How to use Thread?
# # 4. Problems with Thread?
# # 5. How to solve the problems?

# # Answers:

# # 1. Thread is a light-weight process. It is a unit of execution.
# # 2. We can create a Thread by using Thread class.
# # 3. We can use Thread by creating an object of Thread class.
# # 4. Problems with Thread are: 
# #    a. We can't use Thread in GUI application.
# #    b. We can't use Thread in multi-threaded application.
# # 5. We can solve the problems by using Process.

# # Example:

# # 1. We can create a Thread by using Thread class.

# import threading
# import time

# def display(n_time):
#     for _ in range(n_time):
#         print("Thread 1")
#         #if user exsits and passwor is correct
#         # send email to user 
#         time.sleep(1)

# def display2(n_time):
#     for _ in range(n_time):
#         print("Thread 2")
#         time.sleep(1)


# t = threading.Thread(target=display, args=(1000,))
# t2 = threading.Thread(target=display2, args=(1000,))
# t.start()
# t2.start()



# # Example with arguments:

# # 2. We can pass arguments to Thread.

# import threading
# import time

# def display(name):
#     for _ in range(10):
#         print("Hello", name)
#         time.sleep(1)

# t = threading.Thread(target=display, args=("Python",))
# t.start()

# # Example with queue:

# # 3. We can use queue in Thread.

# import threading
# import time
# import queue

# def display(q):
#     counter = 0
#     while True:
#         print(q.get())
#         counter += 1
#         print(counter)
#         # time.sleep(1)

# q = queue.Queue()
# t1 = threading.Thread(target=display, args=(q,))
# t2 = threading.Thread(target=display, args=(q,))
# t1.start()
# t2.start()

# for _ in range(100):
#     q.put("Salom")
    

# # Example with daemon:

# # 4. We can use daemon in Thread.

# import threading
# import time
# list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
# def display(num):
#     for _ in range(10):
#         print([n**3 for n in num ])
        

# t = threading.Thread(target=display, args=(list_of_numbers,))
# t.start()
# t.join() # It will wait for the thread to terminate.
# print("Main thread")
# # Example with join:

# # 5. We can use join in Thread.

# import threading
# import time

# def display():
#     for _ in range(10):
#         print("Hello")
#         time.sleep(1)

# t = threading.Thread(target=display)
# t.start()
# t.join() # It will wait for the thread to terminate.


# # Exmaple with api request:

# # 6. We can use api request in Thread.

# import threading
# import time
# import requests

# def display():
#     for _ in range(10):
#         r = requests.get("https://api.github.com/users") #
#         print(r.status_code)
#         # time.sleep(1)

# t1 = threading.Thread(target=display) # I/O 
# t2 = threading.Thread(target=display)

# start = time.perf_counter()

# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()

# display() # syc

# end_time = start - time.perf_counter()
# print(end_time)



# Example Race problem

#GIL Global Interprent Lock
import time

class Race_c:

    def __init__(self, value) -> None:
        self.value = value

    def increace_int(self)->None:
        self.value +=1
    
    
    def reduce(self)->None:
        self.value -=1

def do_run(race):
    for _ in range(1_000_000):
        race.increace_int()
        race.reduce()
        time.sleep(0.0001)


import threading

race_c = Race_c(value=0)
print(race_c.value)

t1 = threading.Thread(target=do_run, args=(race_c,), name="Thread 1")
t2 = threading.Thread(target=do_run, args=(race_c,))

t1.start()
t2.start()
t1.join()
t2.join()


print(t1)
print(t2)

print(race_c.value)