import os
import msgClass
import sleep

UDP_PORT_IP = 30000
UDP_PORT = 20009
UDP_IP = "129.241.187.156"
UDP_IP_2 = "129.241.187.159"
buffer_size = 1024


def createBackup():
	os.system('python main.py')

def main():
	msg = msgClass.MessageClass(1, UDP_PORT, UDP_IP, buffer_size)

	while True:
		counter = msg.retrieveMsg()
		if counter < 0:
			counter = 0
			createBackup()

		counter += 1
		msg.setMsg(str(counter))
		msg.sendMsg()
		sleep(1)

main()