import sys
import time
import socket

# server="irc.freenode.net"
# botnick="thorsWarhammer"
# channel="##superhiddenchannel576"

class IRC:

    # def __init__(self, server, botnick, channel):
        #     self.server = server
        #     self.botnick = botnick
        #     self.channel = channel

    # def connect(self):
        #     #Establish connection 
        #     self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #     self.irc.connect((self.server,6667))
        #     self.irc.setblocking(False)
        #     time.sleep(1)
        #     self.irc.send("USER "+self.botnick+" "+self.botnick+" "+self.botnick+" :Hello! I am a test bot!\r\n")
        #     time.sleep(1)
        #     self.irc.send("NICK "+self.botnick+"\n")
        #     time.sleep(1)
        #     self.irc.send("JOIN "+self.channel+"\n")

    #     return self.irc

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

    def send(self, chan, msg):
        self.irc.send("PRIVMSG "+chan+" :Hello!\r\n")

    def get_text(self):
        text=self.irc.recv(2040)  #receive the text

        if text.find('PING') != -1:
            self.irc.send('PONG ' + text.split() [1] + 'rn')

        return text
