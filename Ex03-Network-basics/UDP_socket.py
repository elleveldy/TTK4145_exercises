#haakoneh & erlendvd

import socket 
import select

UDP_PORT_IP = 30000
UDP_PORT = 20009
UDP_IP = "129.241.187.156"
buffer_size = 1024


def socket_send(sock, msg):
	sock.sendto(msg, (UDP_IP, UDP_PORT))

def socket_receive(sock):
	data, addr = sock.recvfrom(buffer_size)
	print data
	print addr
	

def main():
	#localIP = socket.gethostbyname(socket.gethostname())

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

	sock.bind((UDP_IP, UDP_PORT))

	msg = 'Ey, this broadcast is sponsored by Erlend gangstaboy'

	socket_send(sock, msg)
	sock.close()

main()
