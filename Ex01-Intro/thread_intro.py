from threading import Thread

i = 0

def thread_func1():
	global i
	for j in range(0, 1000000):
		i += 1

def thread_func2():
	global i
	for j in range(0, 1000000):
		i -= 1

def main():
	print("Before thread join: " + str(i))

	thread_1 = Thread(target = thread_func1, args = (),)
	thread_2 = Thread(target = thread_func2, args = (),)
	thread_1.start()
	thread_2.start()

	thread_1.join()
	thread_2.join()
	
	print("After thread join: " + str(i))

main()