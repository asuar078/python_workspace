import socket

target_host = "10.108.229.24"
target_port = 5000
number_of_connections = 5

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

for i in range(number_of_connections):
	# send some data
	client.send("GET / HTTP/1.1\r\nHost: {0}\r\n\r\n".format(target_host))

	# receive data
	response = client.recv(4096)

	print response
