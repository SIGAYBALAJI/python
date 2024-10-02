import threading
def cal_square():
    num=5
    print(threading.current_thread().name,num*num)

def cal_cube():
    num1=3
    print(threading.current_thread().name,num1**num1)

thread1=threading.Thread(target=cal_square,name="thread1")
thread2=threading.Thread(target=cal_cube,name="thread2")
thread1.start()#To begin the thread execution, we need to call each thread instance's start method separately. So, these two lines execute the square andcube threads concurrently
thread2.start()
thread1.join()#The last thing we need to do is call the join method, which tells one thread to wait until the other thread's execution is complete
thread2.join()
print("multiple threading is completed")


    
