from irc import *
import argparse

# Connection parameters
server="irc.freenode.net"
botnick="TestBot9919"
channel="##superhiddenchannel576"

# password to accept commands
password="@!!@"

irc = IRC(server, botnick, channel) # create irc object
irc.connect() # connect to server

# """
# Command functions
# """

def do_something():
    print("doing something")
    irc.send(channel, "Doing it!")

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
                if str(commands[0]) == "something":
                    do_something()

                print "found it"
                text =""

    except KeyboardInterrupt:
        print "KeyboardInterrupt"
    finally:
        # clean up
        irc.close_connection()

if __name__ == "__main__":
    main()
