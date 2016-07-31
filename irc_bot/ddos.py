import socket
import sys

print "Target host: " + sys.argv[1]
print "Target port: " + sys.argv[2]
print "Number of connections: " + sys.argv[3]

target_host = sys.argv[1]
target_port = int(sys.argv[2])
number_of_connections = int(sys.argv[3])

for i in range(number_of_connections):
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    client.connect((target_host, target_port))

    # send some data
    client.send("GET / HTTP/1.1\r\nHost: {0}\r\n\r\n".format(target_host))

    # receive data
    response = client.recv(4096)

    print response

    client.close()
