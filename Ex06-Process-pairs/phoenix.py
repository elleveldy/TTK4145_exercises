from socket import *
import subprocess
import os
import time

UDP_IP = "localhost"
UDP_PORT = 30000


backup = socket(AF_INET, SOCK_DGRAM)
backup.bind((UDP_IP, UDP_PORT))
backup.settimeout(1.5)


def createBackup():
	#print subprocess.check_output("python phoenix.py", shell=True)
	os.system("gnome-terminal -e 'python phoenix.py'")


#Stay in this loop while main is running break after timeout
recvCount = 0
print 'Entering backuploop'
while True:
	try:
		recvCount = backup.recv(100)
	except timeout:
		print 'Timout detected'
		backup.close()
		createBackup()
		break

mainSocket  = socket(AF_INET, SOCK_DGRAM)
 
count = int(recvCount)

print'MainProcess:'
while True:
	count += 1
	print count

	mainSocket.sendto(str(count), (UDP_IP, UDP_PORT))
	time.sleep(1)


	#send to backup



