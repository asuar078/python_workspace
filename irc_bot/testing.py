# string = ":bigby_!4931096b@gateway/web/freenode/ip.73.49.9.107 PRIVMSG ##superhiddenchannel576 :@!!@attack 192.168.1.111"

# password = "@!!@"

# print(password in string)

# commands = string.split(password,1)[1]
# print commands

# words = commands.split(" ")

# # for word in words:
# #     print word

# print words[0]
# print words[1]


import subprocess as sp

extProc = sp.Popen(['python','myPyScript.py', "hello"]) # runs myPyScript.py 

status = sp.Popen.poll(extProc) # status should be 'None'

print status
try:
    while 1:
        status = sp.Popen.poll(extProc) # status should be 'None' 
        print status

except KeyboardInterrupt:
    print "KeyboardInterrupt"
finally:
        # clean up
    sp.Popen.terminate(extProc) # closes the process
    sp.Popen.wait(extProc) # closes the process

    status = sp.Popen.poll(extProc) # status should now be something other than 'None' ('1' in my testing)

    print status
