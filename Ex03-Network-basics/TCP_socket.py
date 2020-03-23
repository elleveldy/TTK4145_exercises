#haakoneh & erlendvd

import socket 
import select

TCP_PORT_IP = 30000
TCP_PORT = 20008
TCP_PORT1 = 34933 			#Fixed length
TCP_PORT2 = 33546			#\0 - terminated
TCP_IP = "129.241.187.23"

buffer_size = 1024

def socket_send(sock, msg):
	sock.send(msg)

def socket_receive(sock):
	data, addr = sock.recvfrom(buffer_size)
	print data

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

	sock.connect((TCP_IP, TCP_PORT2))
	socket_receive(sock)

	msg = 'Hello galaxy, this is a needlessly long message made to test this code!\0'

	socket_send(sock, msg) #Redundancy ftw!
	socket_receive(sock)
	sock.close()

main()

