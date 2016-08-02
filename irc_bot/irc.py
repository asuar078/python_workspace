import sys
import time
import socket

class IRC:

    irc = socket.socket()

    def __init__(self, server, botnick, channel):
            self.server = server
            self.botnick = botnick
            self.channel = channel

    def connect(self):
            #Establish connection 
            self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.irc.connect((self.server,6667))
            self.irc.setblocking(False)
            time.sleep(1)
            self.irc.send("USER "+self.botnick+" "+self.botnick+" "+self.botnick+" :Hello! I am a test bot!\r\n")
            time.sleep(1)
            self.irc.send("NICK "+self.botnick+"\n")
            time.sleep(1)
            self.irc.send("JOIN "+self.channel+"\n")

    def close_connection(self):
        self.irc.shutdown(socket.SHUT_RDWR)
        self.irc.close()
        sys.exit()

    def send(self, chan, msg):
        self.irc.send("PRIVMSG "+chan+" :" + str(msg)+ "\r\n")

    def get_text(self):
        text=self.irc.recv(2040)  #receive the text

        if text.find('PING') != -1:
            self.irc.send('PONG ' + text.split() [1] + 'rn')

        return text
