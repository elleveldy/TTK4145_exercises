import threading 

i = 0

lock = threading.Lock()

def thread_func1():
	lock.acquire()
	global i
	for j in range(0, 1000000):
		i += 1
	lock.release()

def thread_func2():
	lock.acquire()
	global i
	for j in range(1, 1000000):
		i -= 1
	lock.release()

def main():
	print("Before thread join: " + str(i))

	thread_1 = threading.Thread(target = thread_func1, args = (),)
	thread_2 = threading.Thread(target = thread_func2, args = (),)
	thread_1.start()
	thread_2.start()

	thread_1.join()
	thread_2.join()
	
	print("After thread join: " + str(i))

main()