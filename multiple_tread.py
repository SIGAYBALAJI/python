import threading
def print_numbers():
    for i in range(1,10,2):
        print(threading.current_thread().name,i)
thread1=threading.Thread(target=print_numbers,name="thread1")
thread2=threading.Thread(target=print_numbers,name="thread2")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("multiple thread example is completed")



