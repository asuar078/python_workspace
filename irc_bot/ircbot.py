from irc import *
import random
import argparse

rand = random.randint(1, 9999)  # Integer from 1 to 10, endpoints included
print rand

# Connection parameters
server="irc.freenode.net"
botnick="TestBot" + str(rand)
channel="##superhiddenchannel576"

# password to accept commands
password="@!!@"

irc = IRC(server, botnick, channel) # create irc object
irc.connect() # connect to server
irc.send(channel, "New Bot Online!")

# """
# Command functions
# """

def roll_call():
    print("Roll Call: Here!")
    irc.send(channel, "Here!")

def say_hello():
    print("Hello!")
    irc.send(channel, "Hello!")

def main():

    try:

        while 1:
            time.sleep(0.1)
            try:
                # get text from irc channel
                text = irc.get_text()
                print(text)
            except Exception:
                pass

            # check for message with correct format
            if "PRIVMSG" in text and channel in text and password in text:
                command = text.split(password,1)[1]
                command = command.strip("\r\n")
                commands = command.split(" ")

                print command + "end"
                print "hi" == command
                print type(command)
                print type(commands)
                print commands

                if str(commands[0]) == "hi":
                    say_hello()
                if str(commands[0]) == "RollCall":
                    roll_call()

                print "found it"
                text =""

    except KeyboardInterrupt:
        print "KeyboardInterrupt"
    finally:
        # clean up
        irc.close_connection()

if __name__ == "__main__":
    main()
