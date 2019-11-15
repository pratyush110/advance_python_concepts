#simple python program to demonstrate multi threading capabilities in python
#threading module is used for multithreading in python
#importing the required modules
import threading 
import os 
import time

#simple method which prints certain messages
def method1(argument):
	#current_thread method will return the object of the current running thread 
	print("Method 1 called from thread: {}".format(threading.current_thread().name))
	#getpid method will return the ID of the current executing process 
	print("ID of process running Method 1: {}".format(os.getpid()))
	#thread will sleep for 5 seconds 
	time.sleep(argument)
	print('Exiting from thread:{}'.format(threading.current_thread().name))

def method2(argument): 
	print("Method 2 called from thread: {}".format(threading.current_thread().name)) 
	print("ID of process running Method 2: {}".format(os.getpid()))
	time.sleep(argument)
	print('Exiting from thread:{}'.format(threading.current_thread().name))

if __name__ == "__main__": 

	#will the print ID of the current executing process 
	print("ID of process running main program: {}".format(os.getpid())) 

	#will the print name of the main thread 
	print("Main thread name: {}".format(threading.main_thread().name)) 

	#we can create a thread object of the Thread class
	#takes two arguments:target->method to be executed by the thread object
	#and args->which takes the argument to be passed for the method being executed by the thread object 
	t1 = threading.Thread(target=method1, name='t1',args=(5,),daemon=True) 
	t2 = threading.Thread(target=method2, name='t2',args=(5,)) 

	# starting threads 
	t1.start() 
	t2.start() 

	# wait until all threads finish 
	t1.join() 
	#t2.join() 

