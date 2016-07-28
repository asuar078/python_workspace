from irc import *
import argparse

server="irc.freenode.net"
botnick="thorsHammer"
channel="##superhiddenchannel576"

# irc = IRC(server, botnick, channel)
# irc.connect()

def do_something():
    print("doing something")

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', 'server', type=str, required=True)
    parser.add_argument('n', 'nickname', type=str, required=True)
    parser.add_argument('c', 'channel', help="a nickname or channel", type=str, required=True)
    parser.add_argument('-p', '--port', default=6667, type=int)
    return parser.parse_args()

def main():

    while 1:
        time.sleep(0.1)
        try:
            text = irc.get_text()
            print(text)
        except Exception:
            pass

        if "PRIVMSG" in text and channel in text and "hello" in text:
                irc.send(channel, "Hello!")
                text =""

if __name__ == "__main__":
    main()
